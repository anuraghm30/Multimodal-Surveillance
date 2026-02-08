import streamlit as st

st.title("Multimodal Surveillance Dashboard")

st.subheader("Live Threat Status")
st.metric("Current Threat", "HIGH", "-2 since yesterday")

st.subheader("Event Log")
st.write("Timestamp | Threat | Source")
