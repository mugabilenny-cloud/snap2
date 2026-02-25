import streamlit as st

st.set_page_config(page_title="Snap Delivery", layout="centered")

# CSS to fix the overflow and alignment issues
st.markdown("""
    <style>
    /* 1. Force Streamlit to let us use the full width/height of the block */
    .main .block-container {
        padding: 0;
        max-width: 100%;
        display: flex;
        justify-content: center;
    }
    header, footer, #MainMenu {visibility: hidden;}

    /* 2. The Phone Container - Fixed dimensions and hidden overflow */
    .phone-view {
        width: 375px;
        height: 700px;
        border: 12px solid #1a1a1a;
        border-radius: 45px;
        position: relative;
        overflow: hidden; /* This stops the image/text spill seen in Capture 4 */
        background-color: #000;
        box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        margin: 20px auto;
        display: flex;
        flex-direction: column;
    }

    /* 3. Background with proper scaling */
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

    /* 4. Content Container - Uses Flexbox to space items perfectly */
    .content-container {
        position: relative;
        z-index: 2;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Pushes top and bottom content apart */
        padding: 50px 30px;
        color: white;
        text-align: left;
    }

    .brand-logo {
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        margin-top: 10px;
    }

    .bottom-section h1 {
        font-size: 34px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
        color: white !important;
    }

    .bottom-section p {
        font-size: 16px;
        margin-bottom: 25px;
        opacity: 0.9;
    }

    /* 5. Custom Button Styling for Streamlit */
    div.stButton > button {
        width: 100%;
        background-color: #006d77 !important;
        color: white !important;
        border: none !important;
        padding: 18px !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# App Logic
if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'

# The Mobile Frame
st.markdown('<div class="phone-view">', unsafe_allow_html=True)

if st.session_state.page == 'onboarding':
    # Background and Content Layout
    st.markdown('''
        <div class="bg-image"></div>
        <div class="content-container">
            <div class="brand-logo">Snap</div>
            <div class="bottom-section">
                <h1>Request for Delivery in few clicks</h1>
                <p>On-demand delivery whenever and wherever the need arises.</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Button placed within the bottom section padding
    with st.container():
        st.markdown('<div style="padding: 0 30px 40px 30px; position: absolute; bottom: 0; width: 100%; z-index: 10;">', unsafe_allow_html=True)
        if st.button("Get Started"):
            st.session_state.page = 'login'
            st.rerun()
        st.markdown('<p style="text-align:center; color:white; font-size:13px; margin-top:15px; cursor:pointer;">Have an account already? <u>SIGN IN</u></p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'login':
    # Simple Login Screen to test navigation
    st.markdown('<div style="background:white; height:100%; padding: 40px 30px; z-index: 5; position: relative;">', unsafe_allow_html=True)
    if st.button("← Back"):
        st.session_state.page = 'onboarding'
        st.rerun()
    st.markdown('<h2 style="color:#006d77; margin-top:20px;">Welcome Back</h2>', unsafe_allow_html=True)
    st.text_input("Email")
    st.text_input("Password", type="password")
    st.button("Sign In")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
