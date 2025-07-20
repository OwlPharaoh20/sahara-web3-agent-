import os
from dotenv import load_dotenv
from web3 import Web3
from rich.console import Console
import requests

load_dotenv()
console = Console()

# Load ENV
BASE_SEPOLIA_RPC = os.getenv("BASE_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(BASE_SEPOLIA_RPC))

# Validate RPC connection
if not w3.is_connected():
    console.print("[red]❌ Error: Web3 is not connected. Check BASE_RPC_URL[/red]")
    exit()

# Derive sender address from private key
try:
    SENDER_ADDRESS = w3.eth.account.from_key(PRIVATE_KEY).address
except Exception as e:
    console.print(f"[red]❌ Invalid PRIVATE_KEY in .env: {e}[/red]")
    exit()

def get_eth_balance(wallet_address: str) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"]
    }
    try:
        response = requests.post(BASE_SEPOLIA_RPC, json=payload)
        result = response.json()
        if "result" in result:
            balance_wei = int(result["result"], 16)
            balance_eth = balance_wei / 1e18
            return f"\U0001F4B0 ETH Balance: {balance_eth:.4f} ETH"
        else:
            return "❌ Could not fetch balance."
    except Exception as e:
        return f"\U0001F6A8 Error: {e}"

def send_eth(to_address: str, amount_eth: float) -> str:
    try:
        # Convert ETH to Wei
        amount_wei = w3.to_wei(amount_eth, 'ether')
        # Fetch current nonce
        nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
        # Build transaction dict
        tx = {
            "nonce": nonce,
            "to": Web3.to_checksum_address(to_address),
            "value": amount_wei,
            "gas": 21000,
            "maxFeePerGas": w3.to_wei(2, 'gwei'),
            "maxPriorityFeePerGas": w3.to_wei(1, 'gwei'),
            "chainId": 84532  # Base Sepolia
        }
        # Sign the transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        # Send raw transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        return f"✅ Sent {amount_eth} ETH to {to_address}\n🔗 Tx Hash: {w3.to_hex(tx_hash)}"
    except Exception as e:
        return f"❌ Failed to send ETH: {e}"
