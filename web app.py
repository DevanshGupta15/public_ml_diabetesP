#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:18:43 2022

@author: devansh
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model =pickle.load(open('/Users/devansh/Desktop/Delploying ml /trained_model2.sav','rb'))

def diabetes_prediction(input_data):
    
    input_data_to_array = np.asarray(input_data)
    input_data_reshaped = input_data_to_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')
      

  
def main():
    st.title("Diabetes Prediction Web App")
    Pregnancies = st.text_input("Number of pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin levels")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")
   
    diagnosis = " "  
   
    if st.button("Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)


      
if __name__ == "__main__":
    main()      
      
        
      
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       