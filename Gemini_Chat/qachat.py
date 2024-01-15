import streamlit as st
import google.generativeai as genai

from dotenv import dotenv_values

# Load environment varible
config = dotenv_values("D:/Project1/Gemini_chat_app/.env")
SECRET_KEY = config["GOOGLE_API_KEY"]

genai.configure(api_key=SECRET_KEY)


# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Save chat history
chat = model.start_chat(history=[])

# Create a function to get response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize streamlit app
st.set_page_config("Q&A Bot")
st.header("Gemini Q&A Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input : ", key="input")
submit = st.button("Ask the Question")


# Submit click event
if submit and input:
    response = get_gemini_response(input)
    
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is :")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The chat history is :")

for role, text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")