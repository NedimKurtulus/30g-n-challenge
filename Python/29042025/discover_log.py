import json
import os
from datetime import datetime

DATA_FILE = "discoveries.json"

def load_discoveries():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_discoveries(discoveries):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(discoveries, file, indent=4, ensure_ascii=False)

def add_discovery(title, location, description):
    discoveries = load_discoveries()
    new_discovery = {
        "id": len(discoveries) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": title,
        "location": location,
        "description": description
    }
    discoveries.append(new_discovery)
    save_discoveries(discoveries)
    print("🆕 Yeni keşif kaydı eklendi.")

def list_discoveries():
    discoveries = load_discoveries()
    if not discoveries:
        print("❌ Keşif kaydı yok.")
        return
    for d in discoveries:
        print(f"[{d['id']}] {d['date']} | {d['title']} - {d['location']}")
