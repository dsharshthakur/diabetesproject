import streamlit as st
import numpy as np
import pickle
import pandas as pd




st.title("Diabetes checker")
st.write("Fill the below form.")
with st.container(border = True):
    glucose = st.number_input("Glucose", value = 0)
    bp = st.number_input("Blood Pressure", value = 0,format = "%i")
    skin = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI", key = "bmi")
    pedigreefunction = st.number_input("DiabetesPedigreeFunction")
  
    gender_radio = st.radio("Gender", options= ["Male" , "Female"], horizontal = True , )
    if gender_radio == "Female":
        pregnancy = st.number_input("No. of pregnancies in past(if any)", value = 0)
    else:
        pregnancy = 0
    age = st.number_input("Age" , value = 18)
    col1 , col2, col3 = st.columns(3)
    with col2:
        submit_btn = st.button(label = "submit", key = "Submit_btn")

with open("model.pickle",  "rb")  as file:
    model = pickle.load(file)



if submit_btn== True:
    user_data = [pregnancy,glucose , bp , skin , insulin , bmi ,pedigreefunction, age]
    user_data_array = np.array(user_data).reshape(1,-1)
    print(user_data_array , user_data_array.shape)

    prediction = model.predict(user_data_array)[0]
    print(prediction)
    if prediction == 1:
        st.warning("Positive")


    else:
        st.success("Negative")




