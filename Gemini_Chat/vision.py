import streamlit as st
import google.generativeai as genai

from PIL import Image
from dotenv import dotenv_values

# Load environment variabla
config = dotenv_values("D:/Project1/Gemini_chat_app/.env")
SECRET_KEY = config["GOOGLE_API_KEY"]

genai.configure(api_key=SECRET_KEY)

# Load Gemini-pro-vision model
model = genai.GenerativeModel("gemini-pro-vision")

# Create a function and get response
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


# Initialize streamlit app
st.set_page_config("Q&A Demo with Image")
st.header("Gemini Application")

input = st.text_input("Input : ", key="input")

uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about an Image")

# Submit click event
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is :")
    st.write(response)