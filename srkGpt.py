import streamlit as st
import requests


# SRK-GPT App Title
st.set_page_config(page_title="SRKGPT - Ask about Shah Rukh Khan 🤖", page_icon="🎬")
st.title("🌟 SRKGPT — Ask Anything About Shah Rukh Khan")

# Chat input from user
user_question = st.text_input("Ask your question about SRK:")

# Your active n8n production webhook URL
N8N_WEBHOOK_URL = "https://lahirisamrat59.app.n8n.cloud/webhook/d4f9762c-1e2c-42aa-9385-ed899787bc68"

# When user hits Enter
if user_question:
    with st.spinner("Thinking like SRK... 🎥"):
        try:
            # Send question to n8n webhook
            response = requests.post(
                N8N_WEBHOOK_URL,
                json={"chatInput": user_question},
                timeout=20
            )

            if response.status_code == 200:
                json_data = response.json()
                print(json_data)
                answer = json_data["choices"][0]["message"]["content"]
                st.success("🎤 SRK says:")
                st.write(answer)
            else:
                st.error(f"❗ Error from SRKGPT: {response.status_code}")
                st.text(response.text)

        except Exception as e:
            st.error(f"⚠️ Could not connect to SRKGPT API: {e}")
