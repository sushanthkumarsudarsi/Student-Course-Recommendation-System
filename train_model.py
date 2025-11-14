# train_model.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Ensure we are in the script folder (defensive)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1) Load dataset
df = pd.read_csv("student_course_data.csv")

# 2) Prepare label encoders: one for Interest (optional) and one for target Course
interest_le = LabelEncoder()
course_le = LabelEncoder()

df["Interest_enc"] = interest_le.fit_transform(df["Interest"])
df["Course_enc"] = course_le.fit_transform(df["Course"])

# 3) Features and target
X = df[["Age", "Math_Score", "Coding_Score", "Communication", "Interest_enc"]]
y = df["Course_enc"]

# 4) Train (simple)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5) Save artifacts using joblib (binary)
joblib.dump(model, "model.joblib")
joblib.dump(interest_le, "interest_encoder.joblib")
joblib.dump(course_le, "course_encoder.joblib")

print("Training complete. Saved: model.joblib, interest_encoder.joblib, course_encoder.joblib")
