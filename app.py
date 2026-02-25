import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(page_title="Snap Delivery", layout="centered")

# Custom CSS to simulate a mobile app container and handle transitions
st.markdown("""
    <style>
    /* Hide Streamlit elements for a clean app look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile Wrapper */
    .mobile-container {
        width: 375px;
        height: 700px;
        margin: auto;
        border: 8px solid #333;
        border-radius: 40px;
        position: relative;
        overflow-y: auto;
        overflow-x: hidden;
        background: #fff;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
    }

    /* Background Image Style */
    .bg-onboarding {
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1554629947-334ff61d85dc?auto=format&fit=crop&q=80&w=375');
        background-size: cover;
        height: 100%;
        color: white;
        padding: 40px 25px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }

    .logo-text { font-size: 30px; font-weight: 800; color: white; position: absolute; top: 80px; left: 50%; transform: translateX(-50%); }
    
    .stButton>button {
        width: 100%;
        background-color: #006d77 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-weight: bold !important;
        border: none !important;
    }

    .login-form { padding: 60px 25px; color: #333; }
    </style>
    """, unsafe_allow_html=True)

# Session State to handle screen navigation
if 'screen' not in st.session_state:
    st.session_state.screen = 'onboarding'

# The "Phone" Wrapper
st.markdown('<div class="mobile-container">', unsafe_allow_html=True)

if st.session_state.screen == 'onboarding':
    # ONBOARDING UI
    st.markdown('''
        <div class="bg-onboarding">
            <div class="logo-text">Snap</div>
            <h1 style="font-size: 32px; line-height: 1.1;">Request for Delivery in few clicks</h1>
            <p style="margin-bottom: 20px; opacity: 0.9;">On-demand delivery whenever and wherever the need arises.</p>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("Get Started"):
        st.session_state.screen = 'login'
        st.rerun()

elif st.session_state.screen == 'login':
    # LOGIN UI
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    if st.button("← Back"):
        st.session_state.screen = 'onboarding'
        st.rerun()
        
    st.header("Welcome Back")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign In"):
        st.success("Logging you in...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
