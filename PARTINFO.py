import streamlit as st

# Set the title of the app
st.set_page_config(page_title="My Streamlit App")

# Add a title
st.title("Welcome to my Streamlit App!")

# Add some text
st.write("This is a basic Streamlit app.")

# Add a button
if st.button("Click me!"):
    st.write("You clicked the button!")