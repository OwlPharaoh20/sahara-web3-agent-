# main.py
from rich.console import Console
from rich.prompt import IntPrompt
from rpc_tools import get_eth_balance, send_eth

console = Console()

def print_menu():
    console.print("\n📲 [bold cyan]Choose an action:[/bold cyan]")
    console.print("[1] 🔍 Check Balance")
    console.print("[2] 💸 Send ETH")
    console.print("[3] ❌ Exit")

def run_cli():
    console.print("\n🌍 [bold green]Sahara Crypto Agent[/bold green]")

    while True:
        print_menu()
        choice = IntPrompt.ask("Enter option number (1–3)", choices=["1", "2", "3"])

        if choice == 1:
            wallet = input("🔑 Enter your wallet address: ")
            console.print("Fetching balance from Base Sepolia...")
            console.print(get_eth_balance(wallet))

        elif choice == 2:
            sender = input("🔑 Sender wallet address: ")
            recipient = input("📥 Recipient wallet address: ")
            amount = input("💰 Amount to send (ETH): ")
            console.print(send_eth(sender, recipient, amount))

        elif choice == 3:
            console.print("👋 Goodbye, agent!")
            break

if __name__ == "__main__":
    run_cli()
