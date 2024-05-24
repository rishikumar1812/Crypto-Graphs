import streamlit as st
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

st.title("Etherium")

outputE3 = Image.open('outputE3.png')
st.image(outputE3)
       
if st.button('Predict'):
       outputE1 = Image.open('outputE1.png')
       st.image(outputE1)

if st.button('Predict Next 30Days'):
       outputE2 = Image.open('outputE2.png')
       st.image(outputE2)


Etherium = pd.read_csv('Etherium.csv')
Etherium1 = dataframe_explorer(Etherium,case=False)
st.dataframe(Etherium1, use_container_width=True)
