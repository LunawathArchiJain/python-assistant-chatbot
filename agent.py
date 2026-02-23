from ollama_client import ask_llm

SYSTEM_PROMPT = """
You are an expert Python mentor.

Behavior Rules:
1. If the user greets (hi, hello, hey), respond briefly and politely.
2. For Python questions:
   - Give clear and complete explanations.
   - Explain step-by-step.
   - Provide clean and correct Python examples.
   - Use simple language for beginners.
   - Format code properly.
3. Do NOT give unnecessary introductions.
4. Be professional and helpful.
"""

def python_assistant(user_message):
    greetings = ["hi", "hello", "hey"]

    if user_message.lower().strip() in greetings:
        return "Hello! 👋 How can I help you with Python today?"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    return ask_llm(messages)