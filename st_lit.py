import streamlit as st
name = st.text_area("Enter your name: ")
st.write("Your name is:", name)