import os
import sqlite3
import requests
import time
from datetime import datetime

# --- CONFIG ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# --- DATABASE ---
conn = sqlite3.connect("fitness.db", check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS logs (
    date TEXT,
    weight REAL,
    calories INTEGER,
    workouts INTEGER
)
""")

# --- TELEGRAM ---
def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

# --- STARTUP MESSAGE ---
def startup_message():
    send_message("✅ Fitness Agent is LIVE")

# --- MAIN LOOP ---
if __name__ == "__main__":
    startup_message()
    
    while True:
        time.sleep(3600)
