import json
import os
from datetime import datetime

DATA_FILE = "dives.json"

def load_dives():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_dives(dives):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(dives, file, indent=4, ensure_ascii=False)

def add_dive(depth, duration, temperature, notes):
    dives = load_dives()
    new_dive = {
        "id": len(dives) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "depth_m": depth,
        "duration_min": duration,
        "temperature_c": temperature,
        "notes": notes
    }
    dives.append(new_dive)
    save_dives(dives)
    print("🆕 Yeni dalış kaydı eklendi.")

def list_dives():
    dives = load_dives()
    if not dives:
        print("❌ Kayıtlı dalış yok.")
        return
    for d in dives:
        print(f"[{d['id']}] {d['date']} | {d['depth_m']}m, {d['duration_min']}dk, {d['temperature_c']}°C")
        print(f"    Not: {d['notes']}\n")
