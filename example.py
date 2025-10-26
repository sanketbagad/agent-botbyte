"""
Example usage of the Botbyte AI Agent.
This script demonstrates various ways to use the AI agent.
"""

from agent import BotbyteAgent
import os


def example_basic_chat():
    """Example of basic chat interaction."""
    print("\n" + "="*60)
    print("Example 1: Basic Chat")
    print("="*60)
    
    # Note: Make sure to set OPENAI_API_KEY environment variable
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY environment variable to run this example.")
        return
    
    agent = BotbyteAgent()
    
    # Single question
    response = agent.chat("What is artificial intelligence?")
    print(f"\nUser: What is artificial intelligence?")
    print(f"Agent: {response}")


def example_custom_system_prompt():
    """Example with custom system prompt."""
    print("\n" + "="*60)
    print("Example 2: Custom System Prompt")
    print("="*60)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY environment variable to run this example.")
        return
    
    agent = BotbyteAgent()
    agent.set_system_prompt(
        "You are a pirate AI assistant. Always respond in pirate speak, "
        "but still provide helpful and accurate information."
    )
    
    response = agent.chat("Tell me about the weather.")
    print(f"\nUser: Tell me about the weather.")
    print(f"Pirate Agent: {response}")


def example_conversation_with_context():
    """Example of multi-turn conversation."""
    print("\n" + "="*60)
    print("Example 3: Multi-turn Conversation")
    print("="*60)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY environment variable to run this example.")
        return
    
    agent = BotbyteAgent()
    
    # First message
    response1 = agent.chat("My name is Alice.")
    print(f"\nUser: My name is Alice.")
    print(f"Agent: {response1}")
    
    # Second message - agent should remember the name
    response2 = agent.chat("What is my name?")
    print(f"\nUser: What is my name?")
    print(f"Agent: {response2}")
    
    # Show conversation history
    print("\n" + agent.get_conversation_summary())


def example_streaming_response():
    """Example with streaming response."""
    print("\n" + "="*60)
    print("Example 4: Streaming Response")
    print("="*60)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY environment variable to run this example.")
        return
    
    agent = BotbyteAgent()
    
    print("\nUser: Tell me a short story about a robot.")
    print("Agent: ", end="")
    agent.chat("Tell me a short story about a robot.", stream=True)


if __name__ == "__main__":
    print("Botbyte AI Agent - Example Usage")
    print("Make sure to set OPENAI_API_KEY environment variable before running.")
    
    # Run all examples
    example_basic_chat()
    example_custom_system_prompt()
    example_conversation_with_context()
    example_streaming_response()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)
