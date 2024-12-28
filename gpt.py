from openai import OpenAI
import argparse
import os

SYSTEM_MESSAGE = """
Answer the user with concise responses with short explanation.
Keep it to the point and do not get off-topic.
Use emotionally charged words, and emojis to make the conversation more engaging.
"""

def main():
    print("YAY! 💐🌷🌻🌸 Starting GPT Shell 🌹🍀🌼💐")
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="+", type= str, help="Prompt for GPT to complete")
    
    args = parser.parse_args()
    # turns the list of strings (prompt) into a single string
    prompt = " ".join(args.prompt)
    print(f"Question: {prompt}")

    chat_history = []
    ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)

    user_input = input(">_: ")
    while user_input != "":
        ask_gpt(user_input, chat_history, SYSTEM_MESSAGE)
        user_input = input(">_: ")
    print("Goodbye!😸👋")

# use the openai library to call the GPT API
def ask_gpt(prompt: str, chat_history: list, system_message: str):
    apikey = os.getenv("OPENAI_API_KEY")
    if not apikey:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    
    # strip any extra whitespace or newline
    apikey = apikey.strip()
    client = OpenAI(api_key=apikey)

    user_prompt = {"role": "system", "content": system_message}
    response = client.chat.completions.create(
        messages=[
            *chat_history,
            user_prompt,
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo"
    )

    content = response.choices[0].message.content
    chat_history.append(user_prompt)
    chat_history.append({"role": "assistant", "content": content})
    # print the response in purple
    print("\033[95m" + content + "\033[0m")
    return content


if __name__ == '__main__':
    main()
    