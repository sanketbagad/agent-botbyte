"""
AI Agent by Botbyte AI
A simple yet powerful AI agent implementation that can interact with users,
process queries, and provide intelligent responses.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class BotbyteAgent:
    """
    Main AI Agent class that handles conversations and task execution.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize the Botbyte AI Agent.
        
        Args:
            api_key: OpenAI API key. If not provided, will look for OPENAI_API_KEY env var
            model: The OpenAI model to use (default: gpt-3.5-turbo)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        self.system_prompt = "You are Botbyte AI, a helpful and intelligent AI assistant created by Botbyte AI. You are knowledgeable, friendly, and always aim to provide accurate and useful information."
        
    def set_system_prompt(self, prompt: str) -> None:
        """
        Set or update the system prompt for the agent.
        
        Args:
            prompt: The new system prompt
        """
        self.system_prompt = prompt
        
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the conversation history.
        
        Args:
            role: The role (system, user, or assistant)
            content: The message content
        """
        self.conversation_history.append({"role": role, "content": content})
        
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []
        
    def chat(self, user_message: str, stream: bool = False) -> str:
        """
        Send a message to the AI agent and get a response.
        
        Args:
            user_message: The user's message
            stream: Whether to stream the response (default: False)
            
        Returns:
            The agent's response
        """
        # Add user message to history
        self.add_message("user", user_message)
        
        # Prepare messages for API call
        messages = [{"role": "system", "content": self.system_prompt}] + self.conversation_history
        
        try:
            if stream:
                response_text = ""
                stream_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    stream=True
                )
                
                for chunk in stream_response:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        response_text += content
                        print(content, end="", flush=True)
                
                print()  # New line after streaming
                assistant_message = response_text
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
                assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.add_message("assistant", assistant_message)
            
            return assistant_message
            
        except Exception as e:
            error_message = f"Error communicating with AI: {str(e)}"
            print(error_message)
            return error_message
    
    def get_conversation_summary(self) -> str:
        """
        Get a summary of the current conversation.
        
        Returns:
            A formatted string of the conversation history
        """
        if not self.conversation_history:
            return "No conversation history."
        
        summary = "Conversation History:\n" + "="*50 + "\n"
        for msg in self.conversation_history:
            role = msg["role"].upper()
            content = msg["content"]
            summary += f"{role}: {content}\n" + "-"*50 + "\n"
        
        return summary


def main():
    """
    Main function to demonstrate the AI agent usage.
    """
    print("=" * 60)
    print("Welcome to Botbyte AI Agent!")
    print("=" * 60)
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("Type 'clear' to clear conversation history.")
    print("Type 'history' to see conversation history.\n")
    
    try:
        agent = BotbyteAgent()
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using Botbyte AI Agent. Goodbye!")
                break
                
            if user_input.lower() == 'clear':
                agent.clear_history()
                print("\n[Conversation history cleared]")
                continue
                
            if user_input.lower() == 'history':
                print("\n" + agent.get_conversation_summary())
                continue
            
            print("\nBotbyte AI: ", end="")
            agent.chat(user_input, stream=True)
            
    except ValueError as e:
        print(f"\nError: {e}")
        print("\nPlease set your OPENAI_API_KEY environment variable.")
        print("You can create a .env file with: OPENAI_API_KEY=your_api_key_here")
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
