import streamlit as st

# Set page configuration
st.set_page_config(page_title="PsyCheck - AI", page_icon="🧠", layout="centered")

# Title and Introduction
st.title("PsyCheck - AI")
st.subheader("Your companion for early mental health detection")

# Button to navigate to the form
if st.button("Get Started"):
    st.session_state["page"] = "form"

# Display the form if the user clicks "Get Started"
if "page" in st.session_state and st.session_state["page"] == "form":
    st.title("Enter Your Details")

    name = st.text_input("Name", "")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    location = st.text_input("Location", "")

    if st.button("Submit"):
        st.success("Thank you for providing your information!")
        st.markdown("[Access Questionnaire](https://35ea-34-70-77-185.ngrok-free.app/)")

