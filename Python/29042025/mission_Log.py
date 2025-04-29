import json
import os
from datetime import datetime

DATA_FILE = "missions.json"

def load_missions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_missions(missions):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(missions, file, indent=4, ensure_ascii=False)

def add_mission(location, notes):
    missions = load_missions()
    new_mission = {
        "id": len(missions) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "location": location,
        "status": "Başladı",
        "notes": notes
    }
    missions.append(new_mission)
    save_missions(missions)
    print(f"🆕 Görev eklendi: {location}")

def list_missions():
    missions = load_missions()
    if not missions:
        print("❌ Henüz görev yok.")
        return
    for m in missions:
        print(f"[{m['id']}] {m['date']} | {m['location']} - {m['status']}")
        print(f"    Not: {m['notes']}\n")

def complete_mission(mission_id):
    missions = load_missions()
    for m in missions:
        if m["id"] == mission_id:
            m["status"] = "Tamamlandı"
            save_missions(missions)
            print(f"✅ Görev tamamlandı: {m['location']}")
            return
    print("❌ Görev bulunamadı.")
