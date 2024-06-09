from sklearn.linear_model import LinearRegression
import numpy as np

# Create some data
X = np.array([[2], [5], [7], [8]])
Y = np.array([1, 2, 3, 3])

# Create a linear regression model
model = LinearRegression()
model.fit(X, Y)

# Print the model's coefficients
print(model.coef_, model.intercept_)