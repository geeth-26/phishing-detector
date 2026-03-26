import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# 🔥 Convert byte values to integers
for col in data.columns:
    data[col] = data[col].apply(lambda x: int(x.strip("b'")))

# Features and label
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save model
pickle.dump(model, open("model.pkl", "wb"))