# 🎓 Student Marks Predictor (Machine Learning Project)

This project is an end-to-end **Machine Learning application** that predicts a student's **final marks (G3)** based on academic and behavioral features using supervised learning techniques.

---

## 📌 Project Overview
- Performed data cleaning and exploratory data analysis (EDA)
- Selected important features affecting student performance
- Trained multiple regression models
- Compared models using MAE and R² score
- Selected the **best-performing model**
- Saved the trained model and validated predictions manually
- Uploaded the complete project to GitHub

---

## 📊 Dataset
- Source: Student Performance Dataset
- File: `students.csv`
- Rows: 395
- Target Variable: **G3 (Final Grade)**

### Features Used:
- `G1` – First period grade  
- `G2` – Second period grade  
- `studytime` – Weekly study time  
- `failures` – Number of past failures  
- `absences` – Number of absences  

---

## 🧠 Machine Learning Models Used
The following models were trained and evaluated:

| Model | MAE | R² Score |
|------|-----|----------|
| Linear Regression | ~1.33 | ~0.78 |
| Decision Tree Regressor | ⭐ **~0.96** | ⭐ **~0.89** |
| Random Forest Regressor | ~1.05 | ~0.87 |
| Gradient Boosting | ~1.06 | ~0.85 |

✅ **Decision Tree Regressor** was selected as the final model due to lowest MAE and highest R² score.

---

## 🔍 Model Evaluation
- Predictions were compared with actual test values
- Predicted scores were rounded to integers for realistic interpretation
- Manual validation showed most predictions within **±1 to ±2 marks**

---

## 💾 Saved Files
- `students_marks_model.pkl` → Trained Decision Tree model
- `model_features.pkl` → Feature list used during training

---

## ▶️ How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Parth-Coder5/student-marks-predictor.git
