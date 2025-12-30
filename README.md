# AI Chatbot Project

A modern AI chatbot powered by OpenAI's GPT models, featuring both a Command Line Interface (CLI) and a beautiful Web UI built with Streamlit.

## Features
- **Web UI**: A clean, interactive web interface using Streamlit.
- **CLI Mode**: A simple command-line interface for quick interactions.
- **Streaming Responses**: Real-time message streaming in the Web UI.
- **Context Aware**: Maintains conversation history for coherent interactions.

## Prerequisites
- Python 3.x
- OpenAI API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akashmandala/ai-chatbot-project.git
   cd ai-chatbot-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API Key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

### Option 1: Web UI (Recommended)
Run the Streamlit application:
```bash
streamlit run app.py
```

### Option 2: CLI Mode
Run the terminal-based chatbot:
```bash
python main.py
```

## License
MIT License
