import streamlit as st
import openai
import os
from textblob import TextBlob

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 Ummeed - Your AI Motivational Friend")

user_input = st.text_area("Kya chal raha hai aapke mann mein?", height=150)

if st.button("Send"):
    if user_input:
        # Sentiment
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        try:
            # GPT reply
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "Tum ek Hindi AI chatbot ho jiska naam Ummeed hai. Tum user ko emotionally support karte ho. "
                        "Unke jazbaat ko samajhne ki koshish karo, aur unka sahara bano ek ache dost ki tarah."
                    )},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response["choices"][0]["message"]["content"]

            # Output
            st.markdown("### 🤖 Ummeed says:")
            st.write(reply)

            st.markdown("---")
            st.markdown(f"🧠 *Sentiment Score:* `{round(polarity, 2)}`")

        except Exception as e:
            st.error(f"❌ GPT error: {e}")
    else:
        st.warning("Pehle message likhiye.")
