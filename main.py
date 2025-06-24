import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from time_utils import time_category
with open (r'C:\Users\hp\Documents\machine learning\KNN\Ml project\smart_home_.pkl','rb') as obj1:
   dict1=pickle.load(obj1)
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("pngtree-concept-smart-home-and-wireless-control-technology-picture-image_15533056.jpg")

page_bg_img = f'''
<style>
.stApp {{
background-image: url("data:image/jpg;base64,{bg_img}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
image-rendering: auto;
background-colour: black;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: white;'>⚡Smart Home Energy Tracker</h1>",
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    /* Change font color for all inputs */
    input, select, textarea {
        color: White !important;
    }

    /* Change the dropdown text */
    .stSelectbox > div > div > div {
        color: Black !important;
    }

    /* Change the number input value */
    .stNumberInput input {
        color: Black !important;
    }

    /* Change date and time input value */
    .stDateInput input, .stTimeInput input {
        color: Black !important;
    }
            
   /* Change date and time input value */
    .stTimeInput input {
        color: Black !important;
    }

    /* Optional: Change label colors too */
    label {
    color: white !important;
   }
    </style>
""", unsafe_allow_html=True)

appliance=st.selectbox("Select Appliance Type",['Fridge', 'Oven', 'Dishwasher', 'Heater', 'Microwave','Air Conditioning', 'Computer', 'TV', 'Washing Machine', 'Lights'])
date=st.date_input('Enter date')
temp=st.number_input("Enter Outdoor Temperature in Celsius")
time=st.time_input("Enter time")
hour=time.hour
time=time_category(hour)
time=dict1["ordinal"].transform([[time]])[0][0]
season=st.selectbox('Select season',['Fall', 'Summer', 'Winter', 'Spring'])
size=st.number_input('Enter Number of people living')
week=date.weekday()
Day=date.day
year=date.year
month=date.month
data_onehot=[[appliance,season]]
encoded=dict1['onehot'].transform(data_onehot).flatten()
button=st.button("Predict")
numeric=[temp,size,time,year,month,Day,week]
data=np.concatenate([numeric,encoded]).reshape(1,-1)
if button:
   scaled=dict1["scaler"].transform(data)
   res=dict1["model"].predict(scaled)[0]
   st.markdown(
    f"<h3 style='color:White'>⚡ Estimated Energy Consumption is {res:.2f} KWh</h3>",
    unsafe_allow_html=True
   )
