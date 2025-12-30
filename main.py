import os
from openai import OpenAI

def main():
    # Initialize the OpenAI client
    # The API key is expected to be in the OPENAI_API_KEY environment variable
    client = OpenAI()

    print("AI Chatbot: Hello! I'm your AI assistant. Type 'quit' or 'exit' to end the conversation.")
    
    messages = [
        {"role": "system", "content": "You are a helpful and friendly AI assistant."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("AI Chatbot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            
            bot_message = response.choices[0].message.content
            print(f"AI Chatbot: {bot_message}")
            messages.append({"role": "assistant", "content": bot_message})
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
