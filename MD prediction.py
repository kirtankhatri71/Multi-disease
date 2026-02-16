import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load models
diabetes_data = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/Health project (multi disease)/diabetes_trained_model.sav","rb"))
heart_data = pickle.load(open("C:/Users/DELL/OneDrive/Desktop/Health project (multi disease)/heart_trained_model.sav","rb"))

# side bar navigates
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",

        ["Diabetes Prediction", "Heart Disease"],

        icons =["activity","heart"],
        default_index=0
    )


# Call the background function (use your actual image filename)
if (selected=="Diabetes Prediction"):
    
    # page title
    st.title("Diabetes Prediction using ml")
    st.write("Enter the patient details below to predict the likelihood of diabetes")

    Pregnancies= st.text_input("Number of pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Value")
    BMI = st.text_input("Bmi Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age Of the Person")

    # code for prediction
    diab_diagnosis = ""

    # creating a button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_data.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                                                  Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"
    st.success(diab_diagnosis)            


# Heart Disease 


if (selected =="Heart Disease" ):

    st.title("Heart Disease  Prediction using ml")
    st.write("Enter the patient details below to predict the likelihood of heart disease.")

    age= st.text_input("Age of the person")
    gender = st.selectbox("Gender", options=["Male", "Female"])

# Map the text to the numbers (1 for Male, 0 for Female)
    gender_mapping = {"Male": 1, "Female": 0}
    sex = gender_mapping[gender]
    cp = st.selectbox("chest pain type value",options= [0,1,2,3])
    trestbps = st.text_input("Resting blood pressure value")
    chol = st.text_input("Serum cholestoral in mg/dl")
    fbs = st.selectbox("fasting blood sugar",options = [0,1])
    restecg = st.selectbox("resting electrocardiographic results values",options = [0,1,2])
    thalach = st.text_input("maximum heart rate achieved")
    exang = st.selectbox("exercise induced angina",options = [0,1])
    oldpeak = st.text_input("ST depression induced by exercise relative to rest")
    slope = st.selectbox("the slope of the peak exercise ST segment",options=[0,1,2])
    ca= st.selectbox("number of major vessels (0-4) colored by flourosopy",options =[0,1,2,3,4])
    thal= st.selectbox("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",options = [0,1,2])



        # code for prediction
    heart_diagnosis = ""

    if st.button("Heart Disease Test Result"):
        try:
            # 2. CONVERT STRINGS TO NUMBERS EXPLICITLY
            # We wrap everything in float() to make the model happy
            input_data = [
                float(age), sex, cp, float(trestbps), float(chol), 
                float(fbs), restecg, float(thalach), float(exang), 
                float(oldpeak), float(slope), ca, thal
            ]

            # 3. Prediction
            # If you are using a scaler (as discussed before), 
            # remember to use heart_scaler.transform([input_data]) here!
            heart_prediction = heart_data.predict([input_data])

            if (heart_prediction[0] == 1):
                heart_diagnosis = "The person has heart disease"
                st.error(heart_diagnosis)
            else:
                heart_diagnosis = "The person does not have heart disease"
                st.success(heart_diagnosis)

        except ValueError:
            st.warning("Please enter valid numeric values in all text fields.")
       