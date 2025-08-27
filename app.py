import streamlit as st
from textblob import TextBlob

st.title("🧠  Ummeed - Your AI Motivational Friend")

user_input = st.text_area("What's on your mind?", height=150)

if st.button("Send"):
    if user_input:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity < -0.3:
            st.write("I'm sorry you're feeling this way. You're not alone. 💙")
        elif polarity > 0.3:
            st.write("You sound positive today! Keep shining 🌟")
        else:
            st.write("Thanks for sharing. I'm here to listen.")

        st.write("Sentiment Score:", round(polarity, 2))
    else:
        st.warning("Please type a message to begin the conversation.")
