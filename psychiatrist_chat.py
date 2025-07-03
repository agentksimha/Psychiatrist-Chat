import streamlit as st
from together import Together
import os

# Set your API key
os.environ["TOGETHER_API_KEY"] = "888fb84e1b638788f3b6e59865697fa5e52ade7a091e1a1777aa883eb92ddbba"
client = Together()

# Initialize Streamlit page
st.set_page_config(page_title="Psychiatrist Chat", page_icon="🧠")
st.title("🧠 Psychiatrist Chat")
st.write("Talk to a helpful, friendly Harvard-certified psychiatrist.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful, friendly harvard certified psychiatrist."}
    ]

# User input
user_input = st.chat_input("What's on your mind?")
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get response from Together AI
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=st.session_state.chat_history
        )
        reply = response.choices[0].message.content.strip()
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display chat messages
for msg in st.session_state.chat_history[1:]:  # skip system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
