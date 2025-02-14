import streamlit as st
from streamlit_javascript import st_javascript

width = st_javascript("window.innerWidth")

if width:
    if width < 768:
        st.write("📱 نمایش در موبایل")
    else:
        st.write("💻 نمایش در دسکتاپ")

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
        width: 90%;  
        max-width: 700px;
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
    .whatsapp-link { background-color: #25D366; }
    .telegram-link { background-color: #0088cc; }
    .github-link { background-color: #333; }
    .gmail-link { background-color: #d93025; }
    .link {
        text-decoration: none;
        font-family: 'Playfair Display', serif; 
        transition: color 0.3s, transform 0.3s, text-shadow 0.3s; 
        position: relative;
        display: flex;
        align-items: center;
        color: white;
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
            You can find different ways to contact me via WhatsApp, Telegram, GitHub, and Gmail. 
            Click on the links below to connect with me.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

contacts = [
    ("https://wa.me/989306264213", "WhatsApp", "https://cdn-icons-png.flaticon.com/512/124/124034.png", "whatsapp-link"),
    ("https://t.me/Sadegh_kd", "Telegram", "https://cdn-icons-png.flaticon.com/512/2111/2111646.png", "telegram-link"),
    ("https://github.com/sadeghkdd", "GitHub", "https://cdn-icons-png.flaticon.com/512/733/733553.png", "github-link"),
    ("mailto:sadegh584@gmail.com", "Gmail", "https://cdn-icons-png.flaticon.com/512/281/281769.png", "gmail-link"),
]

for link, name, icon, css_class in contacts:
    st.markdown(
        f"""
        <div class="box {css_class}"> 
            <a href="{link}" class="link" target="_blank">
                <img src="{icon}" width="24" height="24"> {name}
            </a> 
        </div>
        """,
        unsafe_allow_html=True
    )
