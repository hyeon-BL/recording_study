import cv2  # OpenCV 라이브러리를 임포트
import numpy as np  # NumPy 라이브러리를 임포트
import os  # OS 모듈을 임포트하여 디렉토리 작업을 수행
from datetime import datetime  # datetime 모듈에서 현재 시간을 가져오기 위해 임포트

# 체스보드의 크기 설정 (행, 열)
chessboard_size = (6, 9)
# 체스보드의 각 사각형의 크기 (단위: mm)
square_size = 23.5

# 코너 서브픽셀 정확도를 위한 종료 기준 설정
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 실제 체스보드 크기에 기반한 객체 포인트 준비
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

# 모든 이미지에서 객체 포인트와 이미지 포인트를 저장할 배열 초기화
objpoints = []  # 실제 세계의 3D 포인트 좌표
imgpoints = []  # 이미지 평면의 2D 포인트 좌표

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists('captured'):
    os.makedirs('captured')
if not os.path.exists('parameters'):
    os.makedirs('parameters')

# 'captured' 디렉토리에서 기존 이미지를 로드
images = [f for f in os.listdir('captured') if f.endswith('.png')]
for fname in images:
    img = cv2.imread(os.path.join('captured', fname))  # 이미지를 읽어옴
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 이미지를 그레이스케일로 변환
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)  # 체스보드 코너 찾기
    if ret:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  # 코너 서브픽셀 정확도 향상
        objpoints.append(objp)  # 객체 포인트 추가
        imgpoints.append(corners2)  # 이미지 포인트 추가

# 캡처된 이미지를 사용하여 카메라 캘리브레이션 수행
if len(objpoints) > 0 and len(imgpoints) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    
    print(f"\nReprojection error:{ret}")
    # 현재 타임스탬프를 기반으로 고유한 파일 이름 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    camera_matrix_filename = f"parameters/camera_matrix_{timestamp}.txt"
    dist_coeffs_filename = f"parameters/dist_coeffs_{timestamp}.txt"

    # 캘리브레이션 결과 저장
    np.savetxt(camera_matrix_filename, mtx, fmt='%.4f')
    np.savetxt(dist_coeffs_filename, dist, fmt='%.4f')

    # 캘리브레이션 결과 화면에 출력
    print("\nCamera Matrix:")
    print(np.array_str(mtx, precision=4, suppress_small=True))
    print("\nDistortion Coefficients:")
    print(np.array_str(dist, precision=4, suppress_small=True))

    # 외부 파라미터를 동차 변환 행렬로 저장하고 화면에 출력
    for i, (rvec, tvec) in enumerate(zip(rvecs, tvecs)):
        R, _ = cv2.Rodrigues(rvec)  # 회전 벡터를 회전 행렬로 변환
        H = np.hstack((R, tvec))  # 회전 행렬과 변환 벡터를 결합
        H = np.vstack((H, [0, 0, 0, 1]))  # 동차 변환 행렬로 확장
        extrinsics_filename = f"parameters/extrinsics_{timestamp}_{i}.txt"
        np.savetxt(extrinsics_filename, H, fmt='%.4f')
        
        print(f"\nExtrinsics for image {i}:")
        print(np.array_str(H, precision=4, suppress_small=True))
    
    print(f"\nCalibration results saved as {camera_matrix_filename}, {dist_coeffs_filename}, and separate extrinsics files in 'parameters' directory.")
else:
    print("No valid chessboard images found for calibration.")