import cv2
import numpy as np
import os
import time
 
def detect_user_marker_points(cimg):
    img = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a list to store valid corner points
    corner_points = []

    # Get the dimensions of the image
    height, width = img.shape

    # Iterate over each contour to find corner points
    for contour in contours:
        # Check if the contour area is not too small
        area = cv2.contourArea(contour)
        if area <= (width*height)/200.0:
            continue

        # Approximate the contour to get the corner points
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the polygon has exactly 4 vertices
        n = len(approx)
        if len(approx) == 4:
            # Check if contour is too large
            valid_polygon = True
            for i in range(4):
                pt1 = approx[i][0]
                pt2 = approx[(i + 1) % 4][0]
                side_length = np.linalg.norm(pt1 - pt2)
                if side_length > width / 2 or side_length > height / 2:
                    valid_polygon = False
                    break

            if valid_polygon:
                # Store valid corner points in a separate array
                polygon_points = []
                for point in approx:
                    x, y = point[0]
                    polygon_points.append((x, y))

                corner_points.append(polygon_points)

   # Convert the list of valid corner points to a numpy array with dtype int32
    if corner_points:
        corner_points_array = np.array(corner_points, dtype=np.float32)
    else:
        # Fill with default values if no valid polygon is detected
        corner_points_array = np.zeros((10, 4, 2), dtype=np.float32)

    ct, _, _ = np.shape(corner_points_array)
  
    return corner_points_array, ct


# Function to read camera calibration parameters
def read_calibration_params():
    # Reads camera intrinsic and distortion parameters from files.
    intrinsic_path = os.path.join("parameters", "camera_intrinsic.txt")
    distortion_path = os.path.join("parameters", "camera_distortion.txt")
    try:
        mtx = np.loadtxt(intrinsic_path)
        dist = np.loadtxt(distortion_path)
        return mtx, dist
    except FileNotFoundError:
        print(f"Error: Calibration files not found in 'parameters' directory.")
        return None, None


mcp = mcp_0 = np.array([[274, 0, 0], [0, 21, 0], [0, 106, 0], [274, 106, 0]], dtype = 'float32').reshape((4,1,3))
#mcp = mcp_1 = np.array([[0, 50, 0], [181, 100, 0], [365, 50, 0], [186, 0, 0]], dtype = 'float32').reshape((4,1,3))

mtx, dist = read_calibration_params()
print(f"Intrinsic:{mtx}")
print(f"Distortion:{dist}")

#img = cv2.imread('cammarker.png')
img = cv2.imread('usermarker.png')

corners, ids = detect_user_marker_points(img)

# 검출된 마커들의 꼭지점을 이미지에 그려 확인
for id, corner in enumerate(corners):
    corner = np.array(corner).reshape((4, 2))
    (topLeft, topRight, bottomRight, bottomLeft) = corner

    topRightPoint    = (int(topRight[0]),      int(topRight[1]))
    topLeftPoint     = (int(topLeft[0]),       int(topLeft[1]))
    bottomRightPoint = (int(bottomRight[0]),   int(bottomRight[1]))
    bottomLeftPoint  = (int(bottomLeft[0]),    int(bottomLeft[1]))

    cv2.circle(img, topLeftPoint, radius=5, color=(0, 0, 255), thickness=-1)
    cv2.circle(img, topRightPoint,  radius=5, color=(0, 0, 255), thickness=-1)
    cv2.circle(img, bottomRightPoint,  radius=5, color=(0, 0, 255), thickness=-1)
    cv2.circle(img, bottomLeftPoint, radius=5, color=(0, 0, 255), thickness=-1)
    
    # PnP
    if ids != 10:
        
        ret, rvec, tvec = cv2.solvePnP(mcp, corner, np.array(mtx), np.array(dist))

        # Visualize reprojected points
        projected_points, _ = cv2.projectPoints(mcp, rvec, tvec, np.array(mtx), np.array(dist))
        for p in projected_points:
            cv2.circle(img, (int(p[0][0]), int(p[0][1])), 5, (0, 255, 0), -1)  # Green for projected points


        # Compute the reprojection error
        projected_points_single_channel = projected_points.reshape(-1, 2).astype(np.float32)
        error = cv2.norm(corner, projected_points_single_channel, cv2.NORM_L2) / len(projected_points_single_channel)
        print(f"Reprojection error: {error}")

        max_err = 2.0  # allowable maximum reprojection error
        if error > max_err:
            print("Too large reprojection error. Search next")
            continue

        if ret:
            cv2.drawFrameAxes(img, mtx, dist, rvec, tvec, 50, 3)

            x=round(tvec[0][0],1)
            y=round(tvec[1][0],1)
            z=round(tvec[2][0],1)
            rx=round(np.rad2deg(rvec[0][0]),1)
            ry=round(np.rad2deg(rvec[1][0]),1)
            rz=round(np.rad2deg(rvec[2][0]),1)

            # PnP 결과를 이미지에 그려 확인
            text1 = f"P:{x},  {y},  {z}"
            text2 = f"R:{rx},  {ry},  {rz}"
            text3 = f"Marker ID: {id}"
            cv2.putText(img, text3, (int(topLeft[0]-10),   int(topLeft[1]+40)), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255))
    
            # Print marker position and orientation
            print(f"Marker ID: {id}")
            print(f"Position: {text1}")
            print(f"Orientation: {text2}")
            print("------------------------")   
                    
        
        
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
