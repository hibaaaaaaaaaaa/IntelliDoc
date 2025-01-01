css='''<style>
/* Main container for content with scrollbar */
.conversation-container {
    width: 750px;
    height: 450px;
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 70px;
    left: 460px;
    z-index: 10000;

    display: flex;
    flex-direction: column; /* Enable vertical stacking */
    justify-content: space-between; /* Push input query to bottom */
}

/* Scrollable content inside the conversation container */
.conversation-content {
    flex-grow: 1;
    overflow-y: auto;
    margin-bottom: 80px; 
    margin-top:5px;
    max-height: 300px;/* Space between content and input query */
}

/* Custom scrollbar styling */
.conversation-container::-webkit-scrollbar {
    width: 10px;
}

.conversation-container::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

.conversation-container::-webkit-scrollbar-thumb {
    background-color: #C788CB;
    border-radius: 10px;
    border: 2px solid #f1f1f1;
}

/* Header container styling */
.header-conversation-container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background: linear-gradient(to bottom right, rgba(199, 136, 203, 0.3), rgba(169, 96, 238, 0.1));
    color: #393939;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 14px;
    font-family: 'Inter', sans-serif;
    margin-bottom: 14px;
}



.message-bubble {
    display: flex;

    font-family: 'Inter', sans-serif;
    align-items: flex-start;
    #font-size: 14px;
}

.avatar-bot {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
    background-color: rgba(175, 233, 255, 0.5);
}
.avatar-user {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
    background-color: rgba(199, 136, 203, 0.2);

}
.bot-message, .user-message {
    background-color: white;
    border-radius: 10px;
    padding: 8px 8px;
    max-width: 100%;
    color: #393939;
    display: flex;
    align-items: flex-start; /* Align the message at the top */
    margin-top: 2px;
}

.message-text, .message-text p, .message-text *{
    word-wrap: break-word;
    padding:8px;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    color: #393939 !important;
}




/* Input query container at the bottom */
.input-query-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height:11%;
    background-color: white;
    border-radius: 8px;
    padding: 5px;
    border: 0.9px solid #cfcfcf;
    position: relative;
}

/* Input field */
.ask-input {
    flex-grow: 1;
    padding: 8px;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
    background-color: transparent;
    color: #393939;
    width: 100%;  /* Ensure the input takes up all the available space */
    font-family: 'Inter', sans-serif;
}

/* Placeholder styling */
.ask-input::placeholder {
    color: rgba(57, 57, 57, 0.3);
    font-family: 'Inter', sans-serif;
    
}

.input-query-container:focus-within {
    border: 1.5px solid #ccb0cf; /* Thicker border on focus */
}
.send-button {
    background-color: rgba(199, 136, 203, 0.3); /* Set the background color */
    border: none;
    padding: 8px;
    border-radius: 13%; /* Make the button round */
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background-color 0.3s ease;
    margin-left: 10px; /* Adjust space between input and button */
    outline: none; 
    width: 38px !important;  /* Set the desired width */
    height: 38px !important; 
     
}
.send-button:focus {
    outline: none;
    box-shadow: none; /* Optional: Remove any box-shadow on focus */
}

/* Send button hover effect */
.send-button:hover {
    background-color: rgba(199, 136, 203, 0.9); /* Change color on hover */
}

.send-button img.send-icon {
    width: 40px; /* Set the width of the image */
    height: 40px; /* Set the height of the image */
    object-fit: contain; /* Ensures the image fits well within the button */
    display: block; /* Ensures there are no gaps around the image */
    pointer-events: none; /* Ensures the image doesn't interfere with button clicks */
    
}

</style>
'''
header_conversation='''
<div class="conversation-container">
    <!-- Header for the conversation -->
    <div class="header-conversation-container">
        {document_name} <!-- This will be dynamically injected -->
    </div>
    <!-- Scrollable conversation content -->
    <div class="conversation-content" id="chat_content">
        {conversation_history} <!-- Placeholder for conversation history -->
    </div>
    <!-- Input query container at the bottom -->
    
    
</div>
'''

bot_template='''
<div class="message-bubble bot-message">
    <img src="data:image/png;base64,{bot_avatar_img}" alt="Bot Avatar" class="avatar-bot">
    <div class="message-text">{bot_message}</div>
</div>
'''
user_template='''
<div class="message-bubble user-message">
    <img src="data:image/png;base64,{user_avatar_img}" alt="User Avatar" class="avatar-user">
    <div class="message-text">{user_message}</div>
</div>
'''

