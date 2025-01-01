import streamlit as st
import base64
import time

# Function to load and encode a PNG image to base64
def get_base64_png(png_path):
    with open(png_path, "rb") as png_file:
        return base64.b64encode(png_file.read()).decode('utf-8')

def get_base64_svg(svg_path):
    with open(svg_path, "r") as svg_file:
        return base64.b64encode(svg_file.read().encode('utf-8')).decode('utf-8')

def main_page():
# Set page configuration
    st.set_page_config(page_title="Full Screen Black Container with PNG", layout="wide")

# Encode the PNG and SVG images
    png_base64 = get_base64_png("background4.png")  # Replace with your PNG path
    phone_svg = get_base64_svg("phone.svg")
    web1_svg = get_base64_svg("web1.svg")
    white_svg = get_base64_svg("white.svg")

# Custom CSS to create a full-screen white container, add a PNG image, and hide the Streamlit header and footer
    st.markdown(f"""
    <style>
    /* Hide Streamlit header and footer */
    .reportview-container .main .block-container {{
        padding-top: 0rem;
        padding-bottom: 0rem;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Full-screen white container */
    .white-container {{
        background-color: white;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1; /* Lower z-index for white container */
    }}


    /* SVG image settings */
    .white-container .svg-container1 {{
        position: absolute;
        top: 10%;
        left: 45%;
    }}
    .white-container .svg-container1 img {{
        width: 650px;
        height: auto;
    }}
    .white-container .svg-container2 {{
        position: absolute;
        top: 15%;
        left: 40%;
    }}
    .white-container .svg-container2 img {{
        width: 250px;
        height: auto;
    }}
    .white-container .svg-container3 {{
        position: absolute;
        top: 18%;
        left: 59%;
    }}
    .white-container .svg-container3 img {{
        width: 440px;
        height: auto;
    }}
    .white-container .svg-container4 {{
        position: absolute;
        top: 46%;
        left: 59%;
    }}
    .white-container .svg-container4 img {{
        width: 440px;
        height: auto;
    }}
    </style>
    """, unsafe_allow_html=True)

# HTML structure for the white container with the PNG and SVG images, with the button before the headings
    st.markdown(f"""
    <div class="white-container">
        <img src="data:image/png;base64,{png_base64}" alt="Your PNG Image">
        <div class="svg-container1">
            <img src="data:image/svg+xml;base64,{web1_svg}" alt="Your SVG Image">
        </div>
        <div class="svg-container2">
            <img src="data:image/svg+xml;base64,{phone_svg}" alt="Your SVG Image">
        </div>
        <div class="svg-container3">
            <img src="data:image/svg+xml;base64,{white_svg}" alt="Your SVG Image">
        </div>
        <div class="svg-container4">
            <img src="data:image/svg+xml;base64,{white_svg}" alt="Your SVG Image">
        </div>
        <h1 style="position: absolute; top: 20%; left: 5%; color: #393939; font-family: 'Century Gothic'; font-size: 50px; margin: 0; font-weight: bold; white-space: pre-line;">IntelliDoc: <br>Your PDF Assistant</h1>
        <h2 style="position: absolute; top: 41%; left: 5%; color: #393939; font-family: 'Segoe Script'; font-size: 50px; margin: 0; font-weight: bold;">Powered by AI.</h2>
        <h3 style="position: absolute; top: 60%; left: 5%; color: #425466; font-family: 'Century Gothic'; font-size: 18px; margin: 0; font-weight: normal;">IntelliDoc is your personal document assistant that <br> allows you to upload any PDF file and get instant <br> answers to your queries based on its content.</h3>
        <h4 style="position: absolute; top: 64%; left: 81%; color: #393939; font-family: 'Century Gothic'; font-size: 14px; margin: 0; font-weight: normal; white-space: pre-line;">Built by <a href='https://github.com/hibaaaaaaaaaaa'>Hiba Sofyan</a></h4>
    </div>
    """, unsafe_allow_html=True)

# Use Streamlit's native button

# Position the button using Streamlit's style
    st.markdown(
    """
    <style>
    div.stButton > button {
        all: unset;
        width: 60px !important;
        height: 20px !important;
        font-family: 'Century Gothic' !important;
        font-size: 16px !important;
        background: transparent !important;
        border: none !important;
        position: fixed !important;
        top: 78% !important;
        left: 5% !important;
        color: #ffffff !important;
        cursor: pointer !important;
        z-index: 1 !important;
        padding: 10px 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: nowrap !important;
        user-select: none !important;
        -webkit-user-select: none !important;
        touch-action: manipulation !important;
    }

    div.st-emotion-cache-187vdiz.e1nzilvr4 p{
        font-family: 'Century Gothic' !important;
        font-size: 15px !important;
        font-weight:normal !important;
    }
    div.stButton > button::before,
    div.stButton > button::after {
        content: '' !important;
        position: absolute !important;
        bottom: 0 !important;
        right: 0 !important;
        z-index: -99999 !important;
        transition: all .4s !important;
    }

    div.stButton > button::before {
        transform: translate(0%, 0%) !important;
        width: 100% !important;
        height: 100% !important;
        background:  #11253E !important;
        border-radius: 10px !important;
    }

    div.stButton > button::after {
        transform: translate(10px, 10px) !important;
        width: 35px !important;
        height: 35px !important;
        background: #ffffff15 !important;
        backdrop-filter: blur(5px) !important;
        -webkit-backdrop-filter: blur(5px) !important;
        border-radius: 50px !important;
    }

    div.stButton > button:hover::before {
        transform: translate(5%, 20%) !important;
        width: 110% !important;
        height: 110% !important;
    }

    div.stButton > button:hover::after {
        border-radius: 10px !important;
        transform: translate(0, 0) !important;
        width: 100% !important;
        height: 100% !important;
    }

    div.stButton > button:active::after {
        transition: 0s !important;
        transform: translate(0, 5%) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    start_button_clicked = st.button("Start now")
    if start_button_clicked:
            print("clicked")
            time.sleep(1)
            st.session_state.page = 'second_page'
            st.rerun()