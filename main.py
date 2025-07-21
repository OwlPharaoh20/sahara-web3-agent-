from rpc_tools import get_eth_balance, send_eth
from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv
import os
from agent import handle_prompt

load_dotenv()
console = Console()

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

def main():
    console.print("\n🌍 [bold cyan]Sahara Crypto Agent[/bold cyan]")

    console.print("""
🤖 [bold]Available Features:[/bold]
• 🔍 Check Balance → e.g. "What is my ETH balance?" or "Check balance of 0xAbc..."
• 💸 Send ETH       → e.g. "Send 0.2 ETH to 0x123..."
• 📈 Spot Buy       → e.g. "Buy 0.5 ETH at $4200"
• 📉 Spot Sell      → e.g. "Sell 1.2 ETH at $3900"
• ❌ Exit           → type "exit" or "quit"
""")

    while True:
        user_prompt = Prompt.ask("\n💬 What would you like to do?")

        if user_prompt.lower() in ["exit", "quit"]:
            console.print("👋 Exiting... Bye!")
            break

        response = handle_prompt(user_prompt)
        console.print(response)


if __name__ == "__main__":
    main()
