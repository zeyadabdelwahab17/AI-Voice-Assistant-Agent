import streamlit as st
from speech_input import recognize_speech
from speech_output import speak_text
from llm import get_llm_response
from database import save_conversation

st.set_page_config(page_title="Voice Assistant Agent", layout="centered")
st.title("🎤 Voice Assistant Agent")

if st.button("Start Listening"):
    st.info("🎙 Listening... Please speak.")

    query = recognize_speech()

    if query:
        st.success(f"✅ You said: {query}")

        response, status, response_time_ms = get_llm_response(query)

        st.markdown(f"**🤖 Response:** {response}")
        st.markdown(f"⏱️ *Status:* `{status}` – *Response time:* `{response_time_ms} ms`")

        speak_text(response)

        success = save_conversation(query, response, status, response_time_ms)
        if not success:
            st.warning("⚠️ Failed to log this conversation.")
    else:
        st.error("❌ Sorry, I couldn’t understand your speech.")
