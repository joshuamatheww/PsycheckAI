import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="PsyCheck - AI", page_icon="🧠", layout="centered")

# Apply Custom CSS
custom_css = """
<style>
    /* General Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Center Content */
    .main-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      text-align: center;
      position: relative;
    }

    /* Custom Box */
    .container {
      max-width: 600px;
      background: white;
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0px 4px 20px rgba(92, 15, 163, 0.15);
      position: relative;
      animation: fadeIn 1s ease-in-out;
    }

    /* Title */
    h1 {
      font-family: 'Playfair Display', serif;
      font-size: 2.8rem;
      color: #5C0FA3;
      margin-bottom: 15px;
    }

    /* Description */
    p {
      font-size: 1.2rem;
      color: #4A0C85;
      margin-bottom: 25px;
    }

    /* Button */
    .btn {
      font-size: 1.2rem;
      background-color: #5C0FA3;
      color: white;
      border: none;
      padding: 14px 32px;
      border-radius: 30px;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
      transition: all 0.3s ease-in-out;
    }

    .btn:hover {
      background-color: #4A0C85;
      transform: scale(1.05);
    }

    /* Fade-in Animation */
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-15px); }
      to { opacity: 1; transform: translateY(0); }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title
st.markdown('<h1>PsyCheck - AI</h1>', unsafe_allow_html=True)
st.markdown('<p>Your companion for early mental health detection</p>', unsafe_allow_html=True)

# Button
st.markdown(
    '<a href="?page=form" class="btn">Get Started</a>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)  # Close container
st.markdown('</div>', unsafe_allow_html=True)  # Close main container
