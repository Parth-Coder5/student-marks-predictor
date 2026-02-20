import streamlit as st
import joblib
import numpy as np

model = joblib.load('students_marks_model.pkl')
features = joblib.load('model_features.pkl')

st.set_page_config(page_title='Students Marks Predictor',page_icon="📊")
st.title('📊 Students Marks Predictor')
st.write('Predict Student Final Marks (G3) using Machine Learning')

st.divider()

G1 = st.number_input("First_Period Grade (G1)",min_value=0,max_value=20,value=10)
G2 = st.number_input('Second_Period Grade (G2)',min_value=0,max_value=20,value=10)
studytime = st.slider("Weekly Study Time (1=low,4=high)", 1,4,2)
failures = st.slider('Number of Past Failures', 0,4,0)
absences = st.slider('Number of Absents', 0,100,5)

if st.button('Predict Final Marks',key='predict_btn'):
      input_data = np.array([[G1, G2, studytime, failures, absences]])
      prediction = model.predict(input_data)
      final_score = int(round(prediction[0]))
      st.success(f"🎯 Predicted Final Marks (G3): **{final_score} / 20**")
      percentage = (final_score/20) * 100
      st.info(f"📈 Percentage: {percentage:.1f}%")

      if final_score>=15:
            st.balloons()
            st.info('🔥 Excellent performance expected. keep it up!')
      elif final_score >=8 and final_score<15:
            st.warning('🙂 Average performance. More practice needed.')
      else:
            st.error('⚠️ Low performance risk. Increase study time!')

st.sidebar.header("ℹ️ About Project")
st.sidebar.write(
    """
    - ML Model: Decision Tree 
    - Dataset: Student Performance  
    - Built using: Python & Streamlit  
    """
)
st.markdown("---")
st.caption("Made with ❤️ by a Class 11 Student | ML Project")