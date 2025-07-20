import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from web3 import Web3

load_dotenv()
console = Console()

# For get_eth_balance (raw JSON-RPC)
RPC_URL = os.getenv("BASE_RPC_URL")

# For send_eth (web3.py)
w3 = Web3(Web3.HTTPProvider(os.getenv("BASE_SEPOLIA_RPC")))
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SENDER_ADDRESS = w3.eth.account.from_key(PRIVATE_KEY).address

def get_eth_balance(wallet_address: str) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"]
    }

    try:
        response = requests.post(RPC_URL, json=payload)
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

        # Build transaction
        nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
        tx = {
            "nonce": nonce,
            "to": to_address,
            "value": amount_wei,
            "gas": 21000,
            "maxFeePerGas": w3.to_wei(2, 'gwei'),
            "maxPriorityFeePerGas": w3.to_wei(1, 'gwei'),
            "chainId": 84532  # Base Sepolia Chain ID
        }

        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return f"✅ Sent {amount_eth} ETH to {to_address}\n🔗 Tx Hash: {w3.to_hex(tx_hash)}"

    except Exception as e:
        return f"❌ Failed to send ETH: {e}"
