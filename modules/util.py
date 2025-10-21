import os, json, datetime, pytz
from flask import Flask
from threading import Thread
from config import KST

BASE_PATH = "/opt/render/project/data"
os.makedirs(BASE_PATH, exist_ok=True)
DATA_FILE = os.path.join(BASE_PATH, "data.json")
BACKUP_FILE = os.path.join(BASE_PATH, "data_backup.json")

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def ensure_user(data, uid):
    if "users" not in data:
        data["users"] = {}
    if uid not in data["users"]:
        data["users"][uid] = {}
    u = data["users"][uid]
    u.setdefault("attendance", [])
    u.setdefault("activity", {})
    u.setdefault("notified", {})
    u.setdefault("level", 1)
    u.setdefault("exp", 0)
    u.setdefault("rank_title", None)
    u.setdefault("badges", [])
    data["users"][uid] = u

def logical_date_str_from_now():
    now = datetime.datetime.now(KST)
    logical = now - datetime.timedelta(hours=6)
    return logical.strftime("%Y-%m-%d")

# Flask KeepAlive
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))

def keep_alive():
    Thread(target=run_flask, daemon=True).start()
