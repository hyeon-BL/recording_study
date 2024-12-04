import pandas as pd

# Data extracted from the image
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'OxyCon': [37.99, 47.34, 44.38, 28.17, 27.07, 37.85, 44.72, 36.42, 31.21, 54.85, 39.84, 30.83],
    'Age': [41, 42, 37, 46, 48, 44, 43, 46, 37, 38, 43, 43],
    'Heart Rate': [138, 153, 151, 133, 126, 145, 158, 143, 138, 158, 143, 138]
}

# Create a DataFrame
df = pd.DataFrame(data)

def oxycon(age, heart_rate, w0=-59.50, w1=-0.15, w2=0.60):
    oxycon = (
        w0 +
        w1 * age +
        w2 * heart_rate
    )
    print(f"{round(w0, 4)} {round(w1, 4)} * {age} + {round(w2, 4)} * {heart_rate} = {oxycon.round(2)}")
    return oxycon.round(2)

# Calculate SSE
def calculate_sse(df):
    # Calculate squared differences
    for i in range(len(df)):
        df.loc[i, 'squared_error'] = (df.loc[i, 'OxyCon'] - df.loc[i, 'prediction_OxyCon'])**2
        print(f"({df.loc[i, 'OxyCon']} - {df.loc[i, 'prediction_OxyCon']})^2 = {df.loc[i, 'squared_error'].round(4)}")
    # Sum the squared differences
    sse = df['squared_error'].sum()/2
    
    return sse.round(4)

def calculate_derivatives(df):
    # Partial derivatives for each parameter
    d_intercept = -1 * (df['OxyCon'] - df['prediction_OxyCon']).sum()
    d_age = -1 * (df['OxyCon'] - df['prediction_OxyCon'] * df['Age']).sum()
    d_heart_rate = -1 * (df['OxyCon'] - df['prediction_OxyCon'] * df['Heart Rate']).sum()
    
    print(f"\nPartial derivatives:")
    print(f"d_intercept: {d_intercept:.4f}")
    print(f"d_age: {d_age:.4f}")
    print(f"d_heart_rate: {d_heart_rate:.4f}")
    
    return round(d_intercept, 4), round(d_age, 4), round(d_heart_rate, 4)

# Current weights
w0 = -59.50  # intercept
w1 = -0.15   # age coefficient
w2 = 0.60    # heart rate coefficient
learning_rate = 0.000002

# Apply the model to the DataFrame
df['prediction_OxyCon'] = df.apply(
    lambda row: oxycon(
        row['Age'], row['Heart Rate']
    ),
    axis=1,
)
print(df[['Age', 'Heart Rate', 'prediction_OxyCon']])

# Apply calculation
sse = calculate_sse(df)

print(f"Sum of Squared Errors (SSE): {sse:.4f}")

# Calculate initial predictions and SSE
df['prediction_OxyCon'] = df.apply(
    lambda row: oxycon(row['Age'], row['Heart Rate']),
    axis=1
)

# Calculate derivatives
d_w0, d_w1, d_w2 = calculate_derivatives(df)

# Update weights
new_w0 = w0 - learning_rate * d_w0
new_w1 = w1 - learning_rate * d_w1
new_w2 = w2 - learning_rate * d_w2

print(f"\nUpdated weights:")
print(f"w0 (intercept): {w0:.4f} -> {new_w0:.4f}")
print(f"w1 (age): {w1:.4f} -> {new_w1:.4f}")
print(f"w2 (heart rate): {w2:.4f} -> {new_w2:.4f}")


df['prediction_OxyCon'] = df.apply(
    lambda row: oxycon(row['Age'], row['Heart Rate'], new_w0, new_w1, new_w2),
    axis=1
)
print(df[['Age', 'Heart Rate', 'prediction_OxyCon']])
new_sse = calculate_sse(df)

print(f"\nUpdated SSE: {new_sse:.4f}")