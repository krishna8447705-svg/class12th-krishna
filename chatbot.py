# AI Chatbot for Instagram / Social Media
# Class 12 Student Project | Made with Python + ChatGPT (Free Tier)

import os
from openai import OpenAI

if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Create an API key and set it in your terminal."
    )
$env:OPENAI_API_KEY = "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"
client = OpenAI()

def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

print("🤖 AI Chatbot Started! Type 'exit' to stop")
print("Instagram/WhatsApp style replies deta hai...\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye! 👋")
        break
    if user_input.strip() == "":
        continue
    ai_response = chat_with_ai(user_input)
    print(f"Chatbot: {ai_response}\n")