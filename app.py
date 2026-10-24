
import streamlit as st
from agent import customer_service_agent

st.set_page_config(
    page_title="AI Customer Service Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Service Agent")
st.write(
    "Welcome! I can help you track orders, "
    "check refunds, and answer customer questions."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! How can I help you today? "
                "Try asking: Track order 1001."
            )
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    response = customer_service_agent(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)

st.sidebar.header("Try these questions")
st.sidebar.write("• Track order 1001")
st.sidebar.write("• Check refund for order 1003")
st.sidebar.write("• What is your return policy?")
st.sidebar.write("• Can I cancel my order?")
