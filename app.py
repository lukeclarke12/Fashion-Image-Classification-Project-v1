#!/usr/local/bin/python3
from PIL import Image, ImageOps
import keras
import numpy as np
import streamlit as st
from img_classification import fashion_image_classification

st.title("Fashion Clothing Article Classification Model")
st.header("Fashion Clothing Article Classification Example")
st.text("Upload an image of a clothing article for fashion category classification")

uploaded_file = st.file_uploader("Choose a clothing article image ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded clothing image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = fashion_image_classification(image,
                                           'fashion_image_classification_v1.h5')
    if label == 0:
        st.write("Dress")

    elif label == 1:
        st.write("Jacket")

    elif label == 2:
        st.write("Jeans")

    elif label == 3:
        st.write("Skirt")

    elif label == 4:
        st.write("Blouse")

    elif label == 5:
        st.write("Shorts")

    else:
        st.write("Failed to classify")


