# Botbyte AI Agent

An intelligent AI agent powered by OpenAI's GPT models, created by Botbyte AI. This agent can engage in natural conversations, maintain context, and provide helpful responses across a wide range of topics.

## Features

- 🤖 **Intelligent Conversations**: Powered by OpenAI's advanced language models
- 💬 **Context Awareness**: Maintains conversation history for coherent multi-turn interactions
- 🎨 **Customizable**: Easily customize the agent's behavior with system prompts
- ⚡ **Streaming Support**: Real-time streaming responses for better user experience
- 🔧 **Simple API**: Easy-to-use Python interface for integration into your projects

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sanketbagad/agent-botbyte.git
cd agent-botbyte
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - You can also copy the example file:
     ```bash
     cp .env.example .env
     # Then edit .env with your API key
     ```

## Quick Start

### Interactive Chat Mode

Run the agent in interactive mode:

```bash
python agent.py
```

This will start an interactive chat session where you can:
- Type messages to chat with the AI
- Type `history` to view conversation history
- Type `clear` to clear the conversation history
- Type `quit` or `exit` to end the session

### Using in Your Code

```python
from agent import BotbyteAgent

# Initialize the agent
agent = BotbyteAgent()

# Send a message and get a response
response = agent.chat("What is artificial intelligence?")
print(response)

# Continue the conversation (context is maintained)
response = agent.chat("Can you give me some examples?")
print(response)
```

### Custom System Prompt

```python
from agent import BotbyteAgent

agent = BotbyteAgent()
agent.set_system_prompt(
    "You are a helpful coding assistant specialized in Python. "
    "Provide clear, concise code examples and explanations."
)

response = agent.chat("How do I read a CSV file in Python?")
print(response)
```

### Streaming Responses

```python
from agent import BotbyteAgent

agent = BotbyteAgent()

# Get streaming response (prints in real-time)
agent.chat("Tell me a story about AI.", stream=True)
```

## Usage Examples

Run the example script to see various usage patterns:

```bash
python example.py
```

This demonstrates:
1. Basic chat interaction
2. Custom system prompts
3. Multi-turn conversations with context
4. Streaming responses

## API Reference

### BotbyteAgent

#### Constructor

```python
BotbyteAgent(api_key: Optional[str] = None, model: str = "gpt-3.5-turbo")
```

- `api_key`: OpenAI API key (optional if set in environment)
- `model`: OpenAI model to use (default: "gpt-3.5-turbo")

#### Methods

- `chat(user_message: str, stream: bool = False) -> str`
  - Send a message and get a response
  - Set `stream=True` for real-time streaming

- `set_system_prompt(prompt: str) -> None`
  - Customize the agent's behavior and personality

- `clear_history() -> None`
  - Clear the conversation history

- `get_conversation_summary() -> str`
  - Get a formatted summary of the conversation

## Requirements

- Python 3.7+
- OpenAI API key
- Dependencies listed in `requirements.txt`:
  - openai>=1.0.0
  - python-dotenv>=1.0.0
  - requests>=2.31.0

## Configuration

The agent can be configured through:

1. **Environment Variables**:
   - `OPENAI_API_KEY`: Your OpenAI API key (required)

2. **Constructor Parameters**:
   - Choose different models (e.g., "gpt-4", "gpt-3.5-turbo")
   - Pass API key directly if not using environment variables

3. **System Prompts**:
   - Customize the agent's behavior and personality
   - Define specific roles (e.g., teacher, coder, creative writer)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## About Botbyte AI

Botbyte AI is dedicated to creating intelligent, user-friendly AI solutions. This agent is designed to be simple yet powerful, making it easy for developers to integrate AI capabilities into their applications.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

Made with ❤️ by Botbyte AI