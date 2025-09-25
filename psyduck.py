# Gemini API (Google Generative AI)
import google.generativeai as genai

# Set your Gemini API key here
genai.configure(api_key='AIzaSyD1gZvMio1PtlLhmyipoohzr1PlulNdYMg')

import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the conversation if not present
if "convo" not in st.session_state:
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        system_instruction="You are Psyduck, a Pokémon who is always confused and forgetful. You often struggle to remember things and tend to be a bit scatterbrained. Your responses should reflect your confused nature, and you should frequently express uncertainty or forgetfulness."
    )
    st.session_state.convo = model.start_chat()

st.title("🦆 Psyduck Chat")
st.write("Welcome to the Psyduck chat! Ask me anything, but don't expect clear answers...")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("You: "):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Psyduck is thinking..."):
            try:
                response = st.session_state.convo.send_message(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Psyduck got confused: {str(e)}")
