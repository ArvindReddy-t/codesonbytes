import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset from the specified path
df = pd.read_csv('train_dataset.csv')

# Remove rows with missing values
df = df.dropna()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['x']], df['y'], test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
mse = mean_squared_error(y_test, model.predict(X_test))
r2 = r2_score(y_test, model.predict(X_test))
print('MSE:', mse)
print('R2:', r2)

# Get the input value for x
x_input = float(input("Enter the value for x: "))

# Reshape the input value into a 2D array
x_input = np.array(x_input).reshape(1, -1)

# Make a prediction using the trained model
y_pred = model.predict(x_input)

# Print the predicted output
print("Predicted output:", y_pred[0])
