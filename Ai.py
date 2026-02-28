#Coded by Rianto termux

import requests
import json
import time
import os

os.system('clear')
API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [
    {
        "role": "system",
        "content": "Kamu AI santai, jawaban singkat, gaul dikit, bahasa Indonesia."
    }
]

print("╔════════════════════════╗")
time.sleep(1)
print("║       🤖 ANTO AI       ║")
time.sleep(1)
print("║  Bacot santai Bareng ai║")
time.sleep(1)
print("║ Create by Rianto termux║")
time.sleep(1)
print("╚════════════════════════╝")
time.sleep(1)
print("🤖 AntoAi Chat (CTRL+C+ENTER untuk keluar)\n")

while True:
    user = input("\033[0;33mKamu: ")

    if user.lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }

    r = requests.post(URL, headers=headers, json=payload)
    data = r.json()

    if "choices" not in data:
        print("Error:", json.dumps(data, indent=2))
        continue

    reply = data["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print("\033[0;34mAI:", reply)