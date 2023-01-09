# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.ensemble import RandomForestClassifier
from pickle import dump
from pickle import load
import pickle








data=pd.read_csv("cleanchurn.csv",index_col=0)
array = data.values
X = array[:, 0:-1]
Y = array[:,-1]

loaded_model = load(open('final_model.sav', 'rb'))














# creating a function for Prediction

def ChurnCustomer_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] >= 0.5):
      return ' CHURN CUSTOMER'
    else:
      return 'NOT A CHURN CUSTOMER'
  
    
  
def main():
    
    
    # giving a title
    st.title('Churn Customer Prediction')
    
    
    # getting the input data from the user
    
    
    number1 = st.number_input('account_length')
    number2 = st.number_input('voice_mail_plan')
    number3 = st.number_input('voice_mail_messages')
    number4 = st.number_input('day_mins')
    number5 = st.number_input('evening_mins')
    number6 = st.number_input('night_mins')
    number7 = st.number_input('international_mins')
    number8 = st.number_input('customer_service_calls')
    number9 = st.number_input('international_plan')
    number10 = st.number_input('day_calls')
    number11 = st.number_input('day_charge')
    number12 = st.number_input('evening_calls')
    number13 = st.number_input('evening_charge')
    number14 = st.number_input('night_calls')
    number15 = st.number_input('night_charge')
    number16 = st.number_input('international_calls')
    number17 = st.number_input(' international_charge')
    number18 = st.number_input('total_charge ')
      
    
#     # code for Prediction
    churn = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        churn = ChurnCustomer_prediction([number1, number2, number3,number4,number5,number6,number7,number8,number9,number10,number11,number12,number13,number14,number15,number16,number17,number18])
        
        
    st.success(churn)
    
    
    
    
    
if __name__ == '__main__':
    main()
    


