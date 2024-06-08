from sklearn.linear_model import LinearRegression
import numpy as np

# Create some data
X = np.array([[-2], [-1], [0], [2]])
Y = np.array([4, 3, 1, 0])

# Create a linear regression model
model = LinearRegression()
model.fit(X, Y)

# Print the model's coefficients
print(model.coef_, model.intercept_)