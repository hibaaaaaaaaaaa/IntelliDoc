import streamlit as st
import base64
from function import *
import time
from dotenv import load_dotenv
from html_template import css, header_conversation,bot_template,user_template
import html 
# Function to load and encode a PNG image to base64
def get_base64_png(png_path):
    with open(png_path, "rb") as png_file:
        return base64.b64encode(png_file.read()).decode('utf-8')

# Function to load and encode an SVG image to base64
def get_base64_svg(svg_path):
    with open(svg_path, "r") as svg_file:
        return base64.b64encode(svg_file.read().encode('utf-8')).decode('utf-8')

# Encode the PNG image
png_base64 = get_base64_png("background4.png")  # Replace with your PNG path
button_img = get_base64_png("icons8-en-haut-40.png") 
bot_avatar=get_base64_png("Design sans titre (15) (1).png")
user_avatar=get_base64_png("icons8-utilisateur-50 (3).png")


def handle_userinput(user_question):
    response=st.session_state.conversation2({'question':user_question})
    st.session_state.chat_history = response['chat_history']
    st.session_state.conversation = ""
    for i,message in enumerate( st.session_state.chat_history):
        if i % 2 ==0:
            user_message = user_template.replace("{user_avatar_img}", user_avatar).replace("{user_message}", message.content)
            # Append the user message to the conversation
            st.session_state.conversation += user_message
        else:
            bot_message = bot_template.replace("{bot_avatar_img}", bot_avatar).replace("{bot_message}", message.content)
            # Append the bot message to the conversation
            st.session_state.conversation += bot_message



def second_page():
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
            z-index: 9999;
        }}

        /* PNG image on top without margins */
        .white-container img {{
            width: 100%;
            height: auto;
            display: block;
            margin: 0;  /* Remove any default margin */
            padding: 0;  /* Remove any default padding */
        }}
        /* SVG image settings */
        .white-container .svg-container1 {{
            position: absolute;
            top: 10%;
            left: 45%;
        }}

        </style>
        """, unsafe_allow_html=True)

    # HTML structure for the black container with the PNG image
    st.markdown(f"""
        <div class="white-container">
            <img src="data:image/png;base64,{png_base64}" alt="Your PNG Image">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(
    """
    <style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(231, 232, 237, 0.45); /* Blue color with 80% opacity */
        color: #393939; /* Text color */
        font-family: 'Century Gothic'; /* Change to desired font */
        font-size:15px;
        
    }
    
    /* Change specific font styles in the sidebar */
    [data-testid="stSidebar"] {
         width: 402px !important;
    }
     /* Specific styling for 'Your documents' and 'Drop files here to upload' */
    [data-testid="stHeading"] h3 {
        color: #393939 !important; 
        font-family: 'Century Gothic' !important;
        font-weight: bold !important;
        font-size:40px !important;
        margin-top:-40px !important;
        
    }
    
    div.st-emotion-cache-1whx7iy.e1nzilvr4 p{
    color: #393939 !important; 
        font-family: 'Century Gothic' !important;
        font-weight: normal !important;
        font-size:18px !important;
        margin-top:-30px !important;
        
    }
    [data-testid="stFileUploaderDropzone"]{
        font-family: 'Century Gothic'; /* Change to desired font */
         font-size:15px;
         margin-top:-5px !important;
         height:140px;

    }
    [data-testid="baseButton-secondary"]{
    border-color:rgb(255,0,0);
    color:rgb(255,0,0);}
    
    li.st-emotion-cache-1l95nvm:nth-child(1) {
    margin-top: 50px;  /* Add top margin to the first file uploader item */
    color: #11253E;
}
 

    li.st-emotion-cache-1l95nvm:nth-child(n+2) {
    margin-top: 16px;  /* No extra margin for the second file uploader item */
    color: #11253E;
}

div.st-emotion-cache-187vdiz.e1nzilvr4{
        font-family: 'Century Gothic' !important;
        font-weight: normal !important;
        font-size:10px !important;
        color:rgb(255,255,255);
}
div.row-widget.stButton {
position:absolute;
width:110px !important;
top: 78% !important;
left: 70% !important;}

/* Default button styles */
div.row-widget.stButton > button.st-emotion-cache-1ny7cjd.ef3psqc13 {
  background: linear-gradient(to bottom right, #EF4765, #FF9A5A);
  border: 0;
  border-radius: 12px; /* Ensures rounded corners */
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  line-height: 2.5;
  outline: none; /* Ensures no outline */
  padding: 0 1rem;
  text-align: center;
  text-decoration: none;
  transition: box-shadow .2s ease-in-out;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
}

/* Focus state */
div.row-widget.stButton > button.st-emotion-cache-1ny7cjd.ef3psqc13:not([disabled]):focus {
  outline: none; /* Removes the default focus outline */
  border-radius: 12px; /* Keeps rounded corners */
  box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), 
              -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), 
              .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
}

/* Hover state */
div.row-widget.stButton > button.st-emotion-cache-1ny7cjd.ef3psqc13:not([disabled]):hover {
  outline: none; /* Ensures no outline during hover */
  border-radius: 12px; /* Keeps rounded corners */
  box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), 
              -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), 
              .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
}

div.st-emotion-cache-uzeiqp.e1nzilvr4 p{
        color: #11253E ; 
        font-family: 'Century Gothic' ;
        font-weight: normal ;
        font-size:16px ;
    
        
}


div.st-emotion-cache-j78z8c.e1se5lgy0{
left:28% !important;
height:100px;
top:99% !important;
position:absolute;}





    """,
    unsafe_allow_html=True
)
    
    input_css = """
<style>
/* Targeting the input container */
div[data-baseweb="base-input"] {
    
    background-color: transparent; /* Background color for input */
    
}

div[data-baseweb="input"] {
    align-items: center;
    justify-content: space-between;
    background-color: transparent; /* Background color for input */
    border: 1.2px solid #cfcfcf; /* Add border */
    border-radius: 8px; /* Rounded corners */
    padding: 10px; /* Inner padding */
    margin-bottom: 10px; /* Spacing below the input */
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1); /* Optional shadow */
    align-items: center;
    justify-content: space-between;
    width: 705px;
    height: 44px;
    display:flex;
    top: 455px; /* Align it to the top of the page */
    left: 480px;
    z-index: 12000;  
    position:fixed;
}


div[data-baseweb="input"] input {
    flex-grow: 1;
    border: none; /* Remove border */
    outline: none; /* Remove outline on focus */
    font-size: 14px; /* Font size */
    color: #393939; /* Text color */
    padding: 5px; /* Add padding inside */
    font-family: 'Inter', sans-serif; /* Optional font */
    font-size: 14px;
    background-color: transparent !important; /* Transparent background */
}

/* Placeholder styling */
div[data-baseweb="input"] input::placeholder {
    color: rgba(57, 57, 57, 0.5);
    background-color: transparent !important; /* Placeholder color */
}

/* Focus effect */
div[data-baseweb="input"]:focus-within {
    border: 1.5px solid #ccb0cf; /* Border color on focus */
    box-shadow: 0px 0px 4px rgba(199, 136, 203, 0.5); /* Optional glow */
}
</style>
"""


# Sidebar code
    if "conversation" not in st.session_state:
        st.session_state.conversation = ""

    if "conversation2" not in st.session_state:
        st.session_state.conversation2 = None
    
        
    st.write(css, unsafe_allow_html=True)
    st.markdown(input_css, unsafe_allow_html=True)

   
    user_question=st.text_input(
        "",
        placeholder="Ask me about your document ...",
        key="query_input_unique_key"
    ) 
    header_placeholder = st.empty()
    if not user_question:
        header_placeholder.write(
        header_conversation.replace("{document_name}", "No document added")
                        .replace("{conversation_history}", st.session_state.conversation),
        unsafe_allow_html=True
    )

   
# Text input for the user query
    
    with st.sidebar:
        st.subheader("IntelliDoc")
        pdf_docs = st.file_uploader("Drop files & PDFs here to upload", accept_multiple_files=False)
        header_placeholder.write(
                    header_conversation.replace("{document_name}", "New document added: " + pdf_docs.name)
                                    .replace("{conversation_history}", st.session_state.conversation),
                    unsafe_allow_html=True
                )
        if st.button("Process"):
            if pdf_docs is not None:
                # Initial bot message and user acknowledgment
                bot_message = bot_template.replace("{bot_avatar_img}", bot_avatar).replace("{bot_message}", "Processing ...")
                st.session_state.conversation += bot_message 
                
                # Update the conversation header
                header_placeholder.write(
                    header_conversation.replace("{document_name}", "New document added: " + pdf_docs.name)
                                    .replace("{conversation_history}", st.session_state.conversation),
                    unsafe_allow_html=True
                )
                
                
                with st.spinner("Processing..."):
                    load_dotenv()
                    
                    # Extract text from PDF
                    text = get_text(pdf_docs)
                    documents = get_pdf_pages(pdf_docs)
                    
                    # Split text into chunks
                    chunks = get_chunks(text)
                    print("Chunks created successfully.")
                    
                    # Generate embeddings and create vector store
                    vectorstore = get_vectorstore2(chunks)
                    print("Vectorstore generated.")
                    
                    # Set up conversation chain
                    st.session_state.conversation2 = get_conversation(vectorstore)
                    print("Conversation chain initialized.")
                    
                    # Update conversation with bot response
                    bot_response = "Processing complete. Ready to answer your questions !"
                    bot_message = bot_template.replace("{bot_avatar_img}", bot_avatar).replace("{bot_message}", bot_response)
                    st.session_state.conversation += bot_message
                    
                    # Update header again
                    header_placeholder.write(
                        header_conversation.replace("{document_name}", "New document added: " + pdf_docs.name)
                                        .replace("{conversation_history}", st.session_state.conversation),
                        unsafe_allow_html=True
                    )
        if user_question:
            print(user_question)
            handle_userinput(user_question)
            header_placeholder.write(
            header_conversation.replace("{document_name}", "New document added: " + pdf_docs.name)
                                .replace("{conversation_history}", st.session_state.conversation),
                    unsafe_allow_html=True
                    )
    