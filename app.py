from flask import Flask, request
import time
from datetime import datetime

app = Flask(__name__)

def get_menu():
    now = datetime.now()
    return f"""
♡ NEXA-BOT ♡
♡⃟⃝ ♡ ☙ NEXA-BOT ☙ ♡
☙ ⃞̸͢𑁃̚ ♡ ⃞̸͢𑁃̚ ☙
│ ⛈️ *مـعـلـومـات الـبـوت*
│ ├❦ ➻ *الاسـم:* NEXA-BOT
│ ├❦ ➻ *الـمـطـور:* FIBREX x META AI = DEV
│ ├❦ ➻ *الـتـاريـخ:* {now.strftime('%Y-%m-%d')}
│ ├❦ ➻ *الـوقـت:* {now.strftime('%H:%M:%S')}
│ ├❦ ➻ *الـحـالـة:* 🟢 شـغـال
│ └❦ ➻ *الاصـدار:* V1.0.0
│ ⛈️ *الاوامـر*
│ ├❦ ➻ *.اوامر* - قائمة الاوامر
│ ├❦ ➻ *.منشن* - منشن للكل
│ └❦ ➻ *.بوت* - معلومات البوت
│ ⛈️ *FIBREX x META AI = DEV*
♡⃟⃝ ♡ ☙ ❦ ☙ ♡ ♡⃟⃝
"""

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    text = data.get('message','')
    # هنا كيخدم غير فالجروبات
    if text.startswith(".اوامر"):
        time.sleep(2) # باش ما تتبندش + دير رياكشن ⏳
        return {"text": get_menu()}
    return {"status":"ok"}

@app.route('/', methods=['GET'])
def home():
    return "NEXA-BOT is Running! ♡"

app.run(host='0.0.0.0', port=8080)
