import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st


import pickle

# Example object (could be a model, list, dict, etc.)
model = {"name": "Car Prediction Model", "version": 1.0}

# Save to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

import pickle

# Load from a file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

model=pk.load(open('model.pkl','rb'))
print(model)

cars_data = pd.read_csv(r"C:\Users\Manimaran P\Downloads\Cardetails.csv")

def get_brand_name(car_name):
    car_name=car_name.split(' ')[0]
    return car_name.strip()
cars_data['name']= cars_data['name'].apply(get_brand_name)

name=st.selectbox('Select Car Brand',cars_data['name'].unique())
year=st.slider('Car Manufactured Year' ,1994,2024)
km_driven=st.slider('No of kms Driven' ,1,200000)
fuel=st.selectbox('Fuel type' ,cars_data['fuel'].unique())
seller_type=st.selectbox('Seller type' ,cars_data['seller_type'].unique())
transmission=st.selectbox('Transmission type',cars_data['transmission'].unique())
owner=st.selectbox('seller type',cars_data['owner'].unique())
mileage=st.slider('Car Mileage' ,10,40)
engine=st.slider('Engine CC' ,700,5000)
max_power=st.slider('Max Power' ,0,200)
seats=st.slider('No of Seats' ,5,10)


if st.button('predict'):
    input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
   
    input_data_model['owner'] = cars_data['owner'].map({'First Owner': 1, 'Second Owner': 2,'Third Owner':3,'Fourth & Above Owner':4,'Test Drive Car':5 })
    input_data_model['fuel'] = cars_data['fuel'].map({'Diesel': 1, 'Petrol': 2, 'LPG':3, 'CNG':4 })
    input_data_model['seller_type'] = cars_data['seller_type'].map({'Individual': 1, 'Dealer': 2, 'Trustmark Dealer':3 })
    input_data_model['transmission'] = cars_data['transmission'].apply(lambda x: 1 if x == 'Manual' else 2)
    input_data_model['name'] = cars_data['name'].replace(
    ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata',
     'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 
     'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 
     'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
     25, 26, 27, 28, 29, 30, 31])

    car_price=model.predict(input_data_model)

    st.markdown(f'Car Price is predicted to be: {car_price[0]}')


