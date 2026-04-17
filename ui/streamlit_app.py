import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("ScriptIQ")
st.caption("AI-powered story intelligence platform")

script = st.text_area("Paste your script here")

if st.button("Analyze"):
    response = requests.post(
        f"{API_URL}/analyze",
        json={"script": script}
    )

    result = response.json()

    st.subheader("Analysis Result")
    st.write(result["result"])