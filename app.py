import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Load the pickled model
model = pickle.load(open('logisticregression.pkl', 'rb'))
def predict(diameter):
  output= diameter

  if output>=13.5:
    prediction="hazardous"
  else:
    prediction="non hazardous"
  print(prediction)
  return prediction
def main():

    st.title("Asteroid prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Asteroid prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    dia = st.number_input('diameter', 2, 40)
    result=""
    if st.button("Predict"):
        result=predict(float(dia))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
