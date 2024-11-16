import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBpBRtvT1h6X9LIWWsrrQE9d9HAvBWUZEk")
llm = genai.GenerativeModel('models/gemini-1.5-flash')
chatbot = llm.start_chat(history=[])

st.title(" 🤖 Welcome to the Chatbot")
# Initialize session state for chat history if not already present
if 'history' not in st.session_state:
    st.session_state.history = [("ai", "Hi there! I am a helpful AI assistant. How can I help you today?")]
# Display all previous chat messages stored in the history
for role, message in st.session_state.history:
    st.chat_message(role).write(message)

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    # Display the human's input and save to history
    st.chat_message("human").write(human_prompt)
    st.session_state.history.append(("human", human_prompt))
    # Display the ai's response and save to history
    response = chatbot.send_message(human_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state.history.append(("ai", response.text))
