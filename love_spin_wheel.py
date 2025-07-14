
import streamlit as st
import random
import time
st.set_page_config(page_title="lets spin the wheel love!!!!", page_icon="🐢", layout="centered")
st.markdown("<h1 style='text-align: center; color: pastel pink ;'>🎡 Spin the Love Wheel 💖</h1>", unsafe_allow_html=True)
tasks =[
    "give me virtual hug",
    "kiss me on cheekss😘",
    "grab my waist",
    "do you want head",
    "movie date tortoise🐢",
    "send shirtless hot pic",
    "lets talk on video call",
    "give me 5 names by which you will gonna call me❤️",
    "send me voice note in sexy voice😚",
    "give me a bold lip kisssss🥺"
]
if st.button("spin it and lick me😁"):
    spin_gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjA4OTZlMmZlZDIwMzVjYjMyZDJmYmQxNjFhZTJiOGFjNDA5MzE5MCZjdD1n/gH7Zfv7NJkHjxYrTNB/giphy.gif"
    st.image(spin_gif_url, caption="Spinning...", use_column_width=True)
    
    time.sleep(2.5)
    selected=random.choice(tasks)
    st.markdown(f"<h2 style='text-align: center; color: blue ;'>{selected}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; color: red ;'>surprise tasks are waiting for you and me tooo🥺</p>", unsafe_allow_html=True)