# team_task_allocation_proj/mainApp/ml_models/tain_model.py
#-----------------------------------------------------------#

# The script for training the model

# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset (replace with your actual dataset)
data = pd.read_csv("employee_data.csv")

# Preprocessing
X = data[['skill_level', 'experience', 'rating', 'contributions']]
y = data['task_allocation']

""" 
print("The boy {} is going to {}".format("Daniel", 'School'))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
"""

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(model, "model.pkl")