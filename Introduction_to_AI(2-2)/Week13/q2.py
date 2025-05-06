import pandas as pd

# Data extracted from the image
data = {
    'ID': [1, 2, 3, 4],
    'SURFACE AREA': [784.0, 710.5, 563.5, 637.0],
    'HEIGHT': [3.5, 3.0, 7.0, 6.0],
    'ROOF AREA': [220.5, 210.5, 122.5, 147.0],
    'GLAZING AREA': [0.25, 0.10, 0.40, 0.60]
}

df = pd.DataFrame(data)

def calculate_heating_load(surface_area, height, roof_area, glazing_area):
  """Calculates the heating load based on the provided parameters.

  Args:
    surface_area: The surface area of the building.
    height: The height of the building.
    roof_area: The roof area of the building.
    glazing_area: The glazing area of the building.

  Returns:
    The calculated heating load.
  """
  heating_load = (
      -26.030
      + 0.0497 * surface_area
      + 4.942 * height
      - 0.090 * roof_area
      + 20.523 * glazing_area
  )
  print(f"-26.030 + 0.0497 * {surface_area} + 4.942 * {height} - 0.090 * {roof_area} + 20.523 * {glazing_area} = {heating_load}")
  return heating_load

# Apply the model to the DataFrame
df['HEATING LOAD'] = df.apply(
    lambda row: calculate_heating_load(
        row['SURFACE AREA'], row['HEIGHT'], row['ROOF AREA'], row['GLAZING AREA']
    ),
    axis=1,
)

# Print the DataFrame with the calculated heating load
print(df)

# Create a DataFrame