import pandas as pd
import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model and dataset
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Streamlit app title
st.title("Laptop Price Predictor")

# User input fields
company = st.selectbox('Brand', df['Company'].unique())
type_name = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the Laptop (in kg)')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS', ['No', 'Yes'])
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.0)
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
                                                '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df['Gpu brand'].unique())
os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # Convert touchscreen and ips to binary values
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    # Extract screen resolution and compute pixels per inch (PPI)
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create the input query with correct feature names
    query_dict = {
        'Company': company,
        'TypeName': type_name,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }

    query = pd.DataFrame([query_dict])

    # Predict the price using the pre-trained model
    try:
        predicted_price = np.exp(pipe.predict(query)[0])
        st.title(f"The predicted price of this configuration is ₹{int(predicted_price)}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")