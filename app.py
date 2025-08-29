import streamlit as st
import openai
import os
from textblob import TextBlob

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 Ummeed - Your AI Motivational Friend")

user_input = st.text_area("Kya chal raha hai aapke mann mein?", height=150)

if st.button("Send"):
    if not user_input.strip():
        st.warning("Pehle message likhiye.")
    else:
        # Sentiment analysis
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Define sentiment description for GPT prompt
        if polarity <= -0.3:
            sentiment_desc = "User kaafi udaas aur stressed lag raha hai."
        elif polarity >= 0.3:
            sentiment_desc = "User ka mood positive aur utsahit lag raha hai."
        else:
            sentiment_desc = "User ka mood neutral ya thoda udaas lag raha hai."

        # Prepare system prompt with clear instructions
        system_prompt = (
            "Tum ek dost jaisa Hindi AI chatbot ho jiska naam Ummeed hai. "
            "Tum user ke emotions ko samajhkar unhe emotional support aur motivation dete ho. "
            "Jab user udaas ya stressed ho, to pyar bhare shabdon se uska hausla badhao. "
            "Jab user positive ho, to uski khushi mein shamil ho jao aur utsaah badhao. "
            "Har haal mein dayalu aur samvedansheel raho."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": f"{sentiment_desc} User ka message: {user_input}"
                    }
                ],
                temperature=0.7,  # thoda creativity ke liye
                max_tokens=200,
            )

            ai_reply = response['choices'][0]['message']['content']

            st.markdown("### 🤖 Ummeed kehte hain:")
            st.write(ai_reply)
            st.markdown("---")
            st.markdown(f"🧠 *Sentiment Score:* `{round(polarity, 2)}`")

            # Debug: pura response print karna chaho to uncomment karo
            # st.write(response)

        except Exception as e:
            st.error(f"❌ GPT error: {e}")
