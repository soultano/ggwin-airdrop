import os
from dotenv import load_dotenv

load_dotenv()

MNEMONIC = os.getenv("MNEMONIC")
JETTON_MASTER = os.getenv("JETTON_MASTER")
JETTON_WALLET = os.getenv("JETTON_WALLET")

print("GGWIN Airdrop script loaded.")
print("Mnemonic:", "*" * len(MNEMONIC))
print("Jetton Master:", JETTON_MASTER)
print("Jetton Wallet:", JETTON_WALLET)

# Тут позже добавим логику отправки через TON SDK или Toncenter API
