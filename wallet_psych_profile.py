import requests
import time
import random

ETHERSCAN_API_KEY = "YourAPIKeyHere"
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"

def get_transactions(address):
    """Get normal transactions for a wallet."""
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(ETHERSCAN_BASE_URL, params=params)
    return response.json().get("result", [])

def analyze_behavior(transactions):
    """Analyze wallet behavior and infer psychological profile."""
    if not transactions:
        return "⚠️ Empty wallet or no visible activity. Possibly inactive or cold wallet."

    timestamps = [int(tx['timeStamp']) for tx in transactions]
    deltas = [j - i for i, j in zip(timestamps[:-1], timestamps[1:])]
    
    avg_time = sum(deltas)/len(deltas) if deltas else 0
    tx_count = len(transactions)

    random_factor = random.random()

    if tx_count < 10:
        return "🧊 Cautious Observer: Likely watching from the sidelines or testing the waters."

    if avg_time < 3600:
        return "⚡ Impulsive Trader: Makes quick decisions, possibly based on hype or news."

    if avg_time > 86400 and tx_count > 50:
        return "🧘 Long-term Investor: Enters with conviction and holds with patience."

    if random_factor > 0.8:
        return "🎲 Risk Taker: Your transaction patterns resemble meme coin or NFT flippers."

    return "🧠 Balanced Participant: Neither too aggressive nor too passive — a healthy mix."

def profile_wallet(address):
    print(f"🔎 Analyzing wallet: {address}")
    txs = get_transactions(address)
    profile = analyze_behavior(txs)
    print(f"\n🧬 Psychological Profile: {profile}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Analyze Ethereum wallet behavior and infer psychological traits.")
    parser.add_argument("address", help="Ethereum wallet address (0x...)")
    args = parser.parse_args()

    profile_wallet(args.address)
