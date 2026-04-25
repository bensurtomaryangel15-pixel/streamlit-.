import streamlit as st

st.title("📞 Contacts")

name = st.text_input("Name")
email = st.text_input("E-mail")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully!")
    else:
        st.error("Please fill all fields")

st.markdown("### 🌐 Social Link")
st.write("--Facebook: https//www.facebook.com/angel.bensurto.75")