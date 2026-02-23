import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_llm(messages):
    payload = {
        "model": "llama3",
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["message"]["content"]