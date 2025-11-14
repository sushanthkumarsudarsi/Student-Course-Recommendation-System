🎓 Student Course Recommendation System
Machine Learning + Streamlit Web Application

This project is an end-to-end Machine Learning powered Student Course Recommendation System.
It predicts the best course for a student based on their skills, interests, and performance metrics.

Built using:

Python

Pandas, NumPy

Scikit-Learn (Random Forest Classifier)

Joblib

Streamlit

📌 🔍 Project Overview

Choosing the right career path is difficult for many students.
This system solves that problem by analyzing:

Math score

Coding score

Communication skill

Student interests

Age

and then predicting the most suitable course, such as:

Machine Learning

Data Science

Cloud Computing

Cybersecurity

Finance Analytics

Web Development

📁 Folder Structure
Student-Course-Recommendation-System/
│
├── data/
│   └── student_course_data.csv
│
├── models/
│   ├── model.joblib
│   ├── interest_encoder.joblib
│   └── course_encoder.joblib
│
├── src/
│   └── train_model.py
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

🧠 Machine Learning Model

The project uses:

Random Forest Classifier

Why Random Forest?

High accuracy

Works well with mixed categorical + numerical data

Handles non-linear patterns

Prevents overfitting

Training script:

src/train_model.py


Model outputs stored in:

models/

⚙️ Installation & Running Instructions
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/student-course-recommendation-system.git
cd student-course-recommendation-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the ML model
python src/train_model.py

4️⃣ Run the Streamlit web app
streamlit run app/app.py

📊 Dataset Description
Column	Meaning
Age	Student age
Math_Score	Mathematics score
Coding_Score	Programming ability
Communication	Communication skill
Interest	Student’s preferred domain
Course	Final recommended course

Dataset file:

data/student_course_data.csv

🌐 Web App Features (Streamlit)

✔ User-Friendly Input Form
✔ Real-Time Prediction
✔ Clean UI
✔ Dropdowns & Sliders
✔ Model automatically loads from joblib

Example output:

🎉 Recommended Course: Machine Learning

🚀 Future Improvements

Add more courses

Add Deep Learning / NLP model

Add dashboard analytics

Deploy online (Render / HuggingFace)

Add student login system

🧑‍💻 Author

Sushanth Kumar S


⭐ Support the Project

If you like this project, consider giving it a ⭐ star on GitHub.
