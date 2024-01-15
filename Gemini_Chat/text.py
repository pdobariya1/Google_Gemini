import streamlit as st
import google.generativeai as genai

from dotenv import dotenv_values

# Load environment variable
config = dotenv_values("D:/Project1/Gemini_chat_app/.env")
SECRET_KEY = config["GOOGLE_API_KEY"]

genai.configure(api_key=SECRET_KEY)


# Load Gemini pro model
model = genai.GenerativeModel("gemini-pro")

# Create a function and get response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Initialize streamlit app
st.set_page_config("Q&A Demo")
st.header("Gemini Application")

input = st.text_input("Input : ", key="input")
submit = st.button("Ask the question")

# Submit click event
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is :")
    st.write(response)