from langchain.tools import tool
from rpc_tools import get_eth_balance, send_eth
import os

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

@tool
def CheckETHBalance(address: str = "") -> str:
    """
    Check the ETH balance of a wallet address.
    If no address is provided or a vague term like 'my wallet' is used,
    it defaults to the agent's configured wallet address.
    """
    if not address or "my" in address.lower():
        address = WALLET_ADDRESS
    return get_eth_balance(address)

@tool
def SendETH(input_text: str) -> str:
    """
    Send ETH from the agent's wallet.
    The input should be a sentence like: 'Send 0.1 ETH to 0xABC...'
    """
    try:
        import re

        # Extract ETH amount and recipient address
        amount_match = re.search(r"([\d.]+)\s*eth", input_text.lower())
        address_match = re.search(r"(0x[a-fA-F0-9]{40})", input_text)

        if not amount_match or not address_match:
            return "❌ Could not extract ETH amount or wallet address."

        amount = float(amount_match.group(1))
        recipient = address_match.group(1)

        return send_eth(recipient, amount)

    except Exception as e:
        return f"❌ Error while sending ETH: {e}"
