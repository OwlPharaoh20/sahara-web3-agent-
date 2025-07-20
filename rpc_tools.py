import os
import requests
from dotenv import load_dotenv

load_dotenv()
RPC_URL = os.getenv("BASE_RPC_URL")

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
            return f"💰 ETH Balance: {balance_eth:.4f} ETH"
        else:
            return "❌ Could not fetch balance."

    except Exception as e:
        return f"🚨 Error: {e}"
