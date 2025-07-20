# main.py
from rpc_tools import get_eth_balance, send_eth
from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")


def main():
    console.print("\n🌍 [bold cyan]Sahara Crypto Agent[/bold cyan]")

    while True:
        console.print("\n📲 [bold]Choose an action:[/bold]")
        console.print("[1] 🔍 Check Balance")
        console.print("[2] 💸 Send ETH")
        console.print("[3] ❌ Exit")

        choice = Prompt.ask("Enter option number (1–3)", choices=["1", "2", "3"], default="1")

        if choice == "1":
            address = Prompt.ask("🔍 Enter wallet to check balance (Leave blank to use yours)", default=WALLET_ADDRESS)
            result = get_eth_balance(address)
            console.print(result)

        elif choice == "2":
            to = Prompt.ask("📥 Recipient wallet address")
            amount = Prompt.ask("💸 Amount of ETH to send")
            result = send_eth(to, amount)
            console.print(result)

        elif choice == "3":
            console.print("👋 Exiting... Bye!")
            break


if __name__ == "__main__":
    main()
