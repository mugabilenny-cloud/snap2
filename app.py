import streamlit as st

# Set page to be narrow and clean
st.set_page_config(page_title="Snap Delivery", layout="centered")

# Enhanced CSS for perfect alignment
st.markdown("""
    <style>
    /* Remove Streamlit's default header and padding */
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0rem; max-width: 400px;}
    
    /* The Mobile Frame */
    .phone-wrapper {
        width: 375px;
        height: 750px;
        margin: 20px auto;
        border: 10px solid #1e1e1e;
        border-radius: 45px;
        overflow: hidden;
        position: relative;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        background-color: #fff;
        display: flex;
        flex-direction: column;
    }

    /* Background Area */
    .bg-image {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1554629947-334ff61d85dc?auto=format&fit=crop&q=80&w=375');
        background-size: cover;
        background-position: center;
        z-index: 1;
    }

    /* Content Overlay */
    .content-overlay {
        position: relative;
        z-index: 2;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 60px 30px;
        color: white;
        text-align: left;
    }

    .logo-area {
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        margin-top: 20px;
    }

    .text-area h1 {
        font-size: 32px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
        color: white !important;
    }

    /* Streamlit Button Styling */
    div.stButton > button {
        width: 100%;
        background-color: #006d77 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 20px !important;
        font-weight: bold !important;
        border: none !important;
        text-transform: none;
    }
    
    .login-container {
        padding: 40px 25px;
        z-index: 3;
        background: white;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# Wrap everything in the phone frame
st.markdown('<div class="phone-wrapper">', unsafe_allow_html=True)

if st.session_state.page == 'onboarding':
    # This div holds the background and the text
    st.markdown('''
        <div class="bg-image"></div>
        <div class="content-overlay">
            <div class="logo-area">Snap</div>
            <div class="text-area">
                <h1>Request for Delivery in few clicks</h1>
                <p>On-demand delivery whenever and wherever the need arises.</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Place button at the bottom
    with st.container():
        st.markdown('<div style="padding: 0 30px 40px 30px; position: absolute; bottom: 0; width: 100%; z-index: 10;">', unsafe_allow_html=True)
        if st.button("Get Started"):
            st.session_state.page = 'login'
            st.rerun()
        st.markdown('<p style="text-align:center; color:white; font-size:12px; margin-top:10px;">Have an account already? <b>SIGN IN</b></p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'login':
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    if st.button("← Back"):
        st.session_state.page = 'onboarding'
        st.rerun()
    st.header("Welcome Back")
    st.text_input("Email")
    st.text_input("Password", type="password")
    st.button("Sign In")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
