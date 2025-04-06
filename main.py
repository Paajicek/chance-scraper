
import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.chance.cz/kurzy/zapas/tenis-nakashima-brandon-tiafoe-frances/6960773/co-se-sazi?timeFilter=form.period.today"
TEXT_TO_FIND = "počet es v zápasu"
CHECK_INTERVAL = 5  # vteřin
CHAT_ID = "1842186722"
BOT_TOKEN = "7785381597:AAFPf-jjYqSO_Db9w7avMXa3lq3PP3GbNb0"

def check_website():
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        if TEXT_TO_FIND.lower() in soup.text.lower():
            return True
    except Exception as e:
        print(f"Chyba při načítání stránky: {e}")
    return False

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Chyba při posílání zprávy: {e}")

already_sent = False

while True:
    print("🔄 Kontroluji stránku...")
    if check_website():
        print("✅ Text nalezen!")
        if not already_sent:
            send_telegram_message("🔔 Text 'počet es v zápasu' byl nalezen na stránce!")
            already_sent = True
    else:
        print("❌ Text nenalezen.")
        already_sent = False
    time.sleep(CHECK_INTERVAL)
