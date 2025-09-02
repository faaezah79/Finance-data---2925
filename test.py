import streamlit as st

# Title
st.title("My First Streamlit App")

# Subtitle
st.header("Welcome!")

# Text input
name = st.text_input("Enter your name:")

# Slider
age = st.slider("Select your age:", 1, 100, 18)

# Button
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")
