import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

MNEMONIC = os.getenv("MNEMONIC")
JETTON_MASTER = os.getenv("JETTON_MASTER")
JETTON_WALLET = os.getenv("JETTON_WALLET")

TONCENTER_API = "https://toncenter.com/api/v2"
API_KEY = os.getenv("TONCENTER_API_KEY")  # необязательно, но лучше

HEADERS = {"X-API-Key": API_KEY} if API_KEY else {}

def get_wallet_address(mnemonic):
    # Здесь должен быть вызов Ton SDK для получения адреса (опустим, если вручную)
    return JETTON_WALLET

def send_jetton(to_address, amount):
    print(f"⚡ Отправка {amount} GGWIN → {to_address}... (симуляция)")
    # Здесь будет реальная отправка через Smart Contract или API (если понадобится)
    # Сейчас просто для примера:
    return True

# Загрузка получателей
with open("recipients.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    address, amount = line.strip().split()
    success = send_jetton(address, amount)
    if success:
        print(f"✅ Успешно отправлено: {amount} GGWIN → {address}")
    else:
        print(f"❌ Ошибка при отправке на {address}")
