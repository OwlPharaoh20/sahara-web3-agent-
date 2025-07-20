from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

BASE_RPC_URL = os.getenv("BASE_RPC_URL")
web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

def get_eth_balance(address):
    try:
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.from_wei(balance_wei, 'ether')
        return round(balance_eth, 4)
    except Exception as e:
        return f"❌ Error: {str(e)}"
