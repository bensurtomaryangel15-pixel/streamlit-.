import streamlit as st

st.title("📂 Project")

projects = {
    "attached in Github",
    "school web project"
}

for name, desc in projects():
    with st.expander(name):
        st.write("desc")