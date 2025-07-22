# dex_tools.py

import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware.poa import geth_poa_middleware




load_dotenv()

# RPC and Web3 setup
RPC_URL = os.getenv("BASE_SEPOLIA_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)




# Uniswap V3 Router and Quoter addresses
ROUTER_ADDRESS = Web3.to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564")
QUOTER_ADDRESS = Web3.to_checksum_address("0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6")

# ABIs
UNISWAP_ROUTER_ABI = [
    {
        "inputs": [
            {"internalType": "bytes", "name": "path", "type": "bytes"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMinimum", "type": "uint256"}
        ],
        "name": "exactInput",
        "outputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function"
    }
]

UNISWAP_QUOTER_ABI = [
    {
        "name": "quoteExactInputSingle",
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {"name": "tokenIn", "type": "address"},
            {"name": "tokenOut", "type": "address"},
            {"name": "fee", "type": "uint24"},
            {"name": "amountIn", "type": "uint256"},
            {"name": "sqrtPriceLimitX96", "type": "uint160"}
        ],
        "outputs": [
            {"name": "amountOut", "type": "uint256"}
        ]
    }
]

# Example tokens on Base Sepolia (update as needed)
TOKENS = {
    "WETH": Web3.to_checksum_address("0x4200000000000000000000000000000000000006"),
    "USDC": Web3.to_checksum_address("0xDFA46478F9e5EA86d57387849598dbFB2e964b02")  # Replace with Sepolia-compatible USDC
}

def get_token_quote(token_in: str, token_out: str, amount_eth: float, fee: int = 3000) -> str:
    try:
        amount_in_wei = w3.to_wei(amount_eth, "ether")
        quoter = w3.eth.contract(address=QUOTER_ADDRESS, abi=UNISWAP_QUOTER_ABI)
        output = quoter.functions.quoteExactInputSingle(
            TOKENS[token_in],
            TOKENS[token_out],
            fee,
            amount_in_wei,
            0
        ).call()
        output_token = Web3.from_wei(output, 'ether')
        return f"📈 {amount_eth} {token_in} ≈ {output_token:.4f} {token_out}"
    except Exception as e:
        return f"❌ Failed to fetch quote: {e}"

def spot_buy(token_out: str, eth_amount: float) -> str:
    # Placeholder logic, we’ll integrate full tx flow after testing quotes
    return f"🚧 Buying {token_out} with {eth_amount} ETH — feature in progress..."

def spot_sell(token_in: str, amount: float) -> str:
    # Placeholder logic, we’ll integrate full tx flow after ERC20 allowance setup
    return f"🚧 Selling {amount} {token_in} — feature in progress..."
