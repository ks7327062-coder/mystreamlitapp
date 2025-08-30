import streamlit as st

# Website Title
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="centered")

st.title("🌐 Welcome to My Streamlit Website")
st.subheader("Built with Python + Streamlit")
st.write("This is a simple interactive website created using Streamlit.")

# Input Section
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋 Welcome to my website!")

# Button Example
if st.button("Click Me"):
    st.info("You clicked the button!")

# Slider Example
age = st.slider("Select your age:", 1, 100, 18)
st.write(f"Your age is: {age}")

# File Upload Example
file = st.file_uploader("Upload a file", type=["txt", "csv", "png", "jpg"])
if file is not None:
    st.success(f"File {file.name} uploaded successfully!")

# Show a chart Example
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(data)
