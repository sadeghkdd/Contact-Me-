import streamlit as st
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    body {
        background-color: #fffacd; 
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #fffacd; 
    }
    .box {
        width: 700px;  
        height: 50px; 
        border-radius: 15px;  
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);  
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;  
        color: white; 
        margin-top: 20px; 
        transition: transform 0.3s;  
    }
    .box:hover {
        transform: scale(1.05); 
    }
    .telegram-link {
        background-color: #0088cc; 
    }
    .github-link {
        background-color: #333;  
    }
    .gmail-link {
        background-color: #d93025; 
    }
    .link {
        text-decoration: none;
        font-family: 'Playfair Display', serif; 
        transition: color 0.3s, transform 0.3s, text-shadow 0.3s; 
        position: relative;
        display: flex;
        align-items: center;
    }
    .link img {
        margin-right: 10px; 
    }
    .link:hover {
        color: white; 
        transform: scale(1.1); 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); 
    }
    .intro {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="intro">
        <h2>Contact Me 🌟</h2>
        <p>
            Welcome! Here you can find different ways to get in touch with me via WhatsApp, Telegram, GitHub, and Gmail. 
            I'm always ready to answer your questions and meet your needs. Use the links below to connect with me.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="box whatsapp-link"> 
        <a href="https://wa.me/989306264213" class="link">
            <img src="https://cdn-icons-png.flaticon.com/512/124/124034.png" width="24" height="24"> WhatsApp Link
        </a> 
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="box telegram-link"> 
        <a href="https://t.me/Sadegh_kd" class="link">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" width="24" height="24"> Telegram Link
        </a> 
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="box github-link"> 
        <a href="https://github.com/sadeghkdd" class="link">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="24" height="24"> GitHub Link
        </a> 
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="box gmail-link"> 
        <a href="mailto:sadegh584@gmail.com" class="link">
            <img src="https://cdn-icons-png.flaticon.com/512/281/281769.png" width="24" height="24"> Gmail Link
        </a> 
    </div>
    """, 
    unsafe_allow_html=True
)
