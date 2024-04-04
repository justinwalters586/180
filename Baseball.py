# Import the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read the spreadsheet into a pandas DataFrame
data = pd.read_excel('C:/Users/WaltersJ07/Downloads/baseball.xlsx')

# Select the features (team values) and the target variable (playoffs)
features = data[['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']]
target = data['Playoffs']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
predictions = model.predict(X_test)

# Print the predictions
print(predictions)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy of the model
print(f"Accuracy: {accuracy}")
