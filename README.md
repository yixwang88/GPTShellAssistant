# GPT Shell Assistant
**GPT Shell Assistant** is a simple and interactive command-line tool that allows you to chat with OpenAI's GPT API model from your terminal. This tool supports ongoing conversations and keeps context while providing concise and engaging responses enhanced with emojis. 🌻✨

## 🌟 Features
- 🖋️ **Interactive Chat**: Communicate with GPT-3.5/4 directly in your terminal.
- 🧠 **Conversation Memory**: Maintains chat history for context-aware responses.
- 🌸 **Customizable System Message**: Tailor the behavior and tone of GPT by modifying the system message. I uses emojis and emotionally charged words to make responses more engaging.


## 🚀 Installation and Setup

### Prerequisites
1. Python 3.7 or above.
2. An OpenAI API key. [Sign up for OpenAI](https://platform.openai.com/) if you don't have one.


### Steps
1. **Install Dependencies:**
`pip install openai`
3. **Set Your OpenAI API Key:** (Add your OpenAI API key as an environment variable)

`>export OPENAI_API_KEY="sk-your-api-key"`
To make it permanent, add the above line to your shell configuration file (~/.zshrc or ~/.bashrc).
4. **Add an Alias** (For ease of use, add this alias to your shell configuration so you can use globally in your terminal)
`>alias chat="/opt/homebrew/bin/python3 /path/to/your/project/gpt.py"`


### Ready to use in your terminal
1. To start the chat: `chat "Ask your first question"`
2. Continue the conversation by entering responses.
3. Exit the chat by pressing Enter without typing anything:
`>_: (Press Enter)
Goodbye! 😸👋`

## 🛡️ Customization
1. System Message: Modify the SYSTEM_MESSAGE variable in gpt.py to change how GPT responds.
2. Switch between `gpt-3.5-turbo`, `gpt-4`, or any other available model based on your requirements.
