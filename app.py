import streamlit as st
from textblob import TextBlob
import openai
import os

# API Key setup (best to use environment variable or st.secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")  # OR paste your key here (for testing only)

st.title("🧠  Ummeed - Your AI Motivational Friend")

user_input = st.text_area("What's on your mind?", height=150)

if st.button("Send"):
    if user_input:
        # Sentiment Analysis
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Response using OpenAI GPT
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Tum ek dost jaisa mental health AI chatbot ho jiska naam Ummeed hai. "
                            "Tumhara goal hai user ke emotions ko samajhna aur unhe empathy ke saath support karna. "
                            "Jab user udaas ho, toh unka sahara bano. Jab woh positive feel kare, unka utsah badhao."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            ai_reply = response["choices"][0]["message"]["content"]

            # Show reply and sentiment
            st.markdown(f"**🤖 Ummeed:** {ai_reply}")
            st.markdown(f"🧠 **Sentiment Score:** `{round(polarity, 2)}`")

        except Exception as e:
            st.error(f"Something went wrong while generating a response: {e}")
    else:
        st.warning("Please type a message to begin the conversation.")
