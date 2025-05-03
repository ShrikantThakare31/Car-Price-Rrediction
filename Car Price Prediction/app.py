import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st

# Load model
@st.cache_resource
def load_model():
    return pk.load(open('model.pkl', 'rb'))

model = load_model()

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv('Cardetails.csv')
    df['brand'] = df['name'].apply(lambda x: x.split(' ')[0].strip())
    return df

cars_data = load_data()

st.title('🚗 Car Price Prediction App')

# UI
name = st.selectbox('Car Brand', sorted(cars_data['brand'].unique()))
year = st.slider('Manufactured Year', 1994, 2024, 2015)
km_driven = st.slider('Kilometers Driven', 100, 200000, 30000, step=1000)
fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
owner = st.selectbox('Ownership', cars_data['owner'].unique())
mileage = st.slider('Mileage (kmpl)', 10, 40, 18)
engine = st.slider('Engine Capacity (CC)', 700, 5000, 1200)
max_power = st.slider('Max Power (bhp)', 30, 200, 85)
seats = st.slider('Number of Seats', 2, 10, 5)

# Mapping dictionaries
brand_map = {k: v for v, k in enumerate(sorted(cars_data['brand'].unique()), 1)}
fuel_map = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}
seller_map = {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3}
trans_map = {'Manual': 1, 'Automatic': 2}
owner_map = {
    'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3,
    'Fourth & Above Owner': 4, 'Test Drive Car': 5
}

if st.button("Predict Price"):
    try:
        input_data = pd.DataFrame([[
            brand_map.get(name, 0), year, km_driven,
            fuel_map.get(fuel, 0), seller_map.get(seller_type, 0),
            trans_map.get(transmission, 0), owner_map.get(owner, 0),
            mileage, engine, max_power, seats
        ]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type',
                     'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])

        prediction = model.predict(input_data)
        st.success(f"Estimated Car Price: ₹ {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
