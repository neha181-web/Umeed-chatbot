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
        # Sentiment analysis
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Sentiment label for GPT prompt
        if polarity <= -0.3:
            sentiment_desc = "user kaafi udaas ya stressed lag raha hai"
        elif polarity >= 0.3:
            sentiment_desc = "user positive aur utsahit lag raha hai"
        else:
            sentiment_desc = "user ka mood neutral ya thoda sa udaas lag raha hai"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Tum ek dost jaisa Hindi AI chatbot ho jiska naam Ummeed hai. "
                            "Tum user ke jazbaat ko samajhne ki puri koshish karte ho aur unka emotional sahara bante ho. "
                            "Jab user udaas ya stressed ho, toh pyar bhare aur sahayak shabdon me unhe rahat dena. "
                            "Jab woh positive ho, toh unka hausla badhana. Har halat me unke saath dayalu aur samvedansheel raho."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Mera mood ye hai: {sentiment_desc}. Yeh raha mera message: {user_input}"
                    }
                ]
            )
            reply = response["choices"][0]["message"]["content"]

            st.markdown("### 🤖 Ummeed kehte hain:")
            st.write(reply)

            st.markdown("---")
            st.markdown(f"🧠 *Sentiment Score:* `{round(polarity, 2)}`")

        except Exception as e:
            st.error(f"❌ GPT error: {e}")
    else:
        st.warning("Pehle message likhiye.")
