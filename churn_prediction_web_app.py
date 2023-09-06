# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:41:07 2023

@author: dell1
"""

import numpy as np
import streamlit as st
import tensorflow as tf
import pickle

def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

loaded_model = tf.keras.models.load_model('Model/ann.hdf5')
loaded_model_scaled = pickle.load(open('Model/trained_model_scaled.sav','rb'))


def churn_predict(input_data):
    input_data_flat = flat(input_data)
    input_data_array = np.array([input_data_flat])
    input_data_scaled = loaded_model_scaled.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    
    print(prediction)
    
    if prediction[0] >0.5:
        return 'The customer is churn'
    else:
        return 'The customer is not churn'
    

def main():
    
    st.title('Churn Prediction')
    st.header('Enter the following parameter:')
    
    CreditScore = st.number_input('Enter the credit score of the customer')
    Gender = st.selectbox('Select the gender of the customer', ('Male', 'female'))
    if Gender == 'Male':
        Gender = 0
    else:
        Gender = 1
    Age = st.number_input('Enter the age of the customer')
    Balance = st.number_input('Enter the balance of the customer')
    IsActiveMember = st.selectbox('Is the customer is active member', ('0', '1'))
    if IsActiveMember == '0':
        IsActiveMember = 0
    else:
        IsActiveMember = 1
    Geography = st.selectbox('Geography of the customer', ('France', 'Germany','Spain'))
    if Geography == 'France':
        Geography = [1,0,0]
    elif Geography == 'Germany':
        Geography = [0,1,0]
    else:
        Geography = [0,0,1]
    NumOfProducts = st.selectbox('Select the number of products', ('1', '2','3','4'))
    if NumOfProducts == '1':
        NumOfProducts = [1,0,0,0]
    elif NumOfProducts == '2':
        NumOfProducts = [0,1,0,0]
    elif NumOfProducts == '3':
        NumOfProducts = [0,0,1,0]
    else:
        NumOfProducts = [0,0,0,1]
    
    
    pred = ' '
    
    if st.button('Predit Churn'):
        pred = churn_predict([CreditScore,Gender,Age,Balance,IsActiveMember,Geography,NumOfProducts])
    st.success(pred)

if __name__ =='__main__':
    main()

    