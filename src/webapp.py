from chatbot import chatbot
import streamlit as st

chat = chatbot()


st.title("My new chatbot !")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])





if prompt := st.chat_input("This is an input"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        response  = st.write_stream(chat.response_generator(prompt))

    st.session_state.messages.append({"role": "assistant", "content": response})