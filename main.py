from rich.console import Console
from rich.prompt import Prompt
from wallet import get_eth_balance

console = Console()

def run():
    console.print("\n🌍 [bold cyan]Sahara Crypto Agent[/bold cyan]")
    address = Prompt.ask("🔑 Enter your wallet address")

    console.print("\n[bold green]Fetching balance from Base Goerli...[/bold green]")
    balance = get_eth_balance(address)
    console.print(f"💰 [bold yellow]ETH Balance:[/bold yellow] {balance} ETH")

if __name__ == "__main__":
    run()
