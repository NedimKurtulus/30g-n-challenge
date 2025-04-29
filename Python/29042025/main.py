import mission_log
import dive_log
import discovery_log
import route_log

def menu():
    while True:
        print("\n--- Deniz Keşfi Uygulaması ---")
        print("1. Görev Günlüğü")
        print("2. Dalış Günlüğü")
        print("3. Keşif Günlüğü")
        print("4. Rota Günlüğü")
        print("5. Çıkış")
        choice = input("Seçim: ")

        if choice == "1":
            mission_menu()
        elif choice == "2":
            dive_menu()
        elif choice == "3":
            discovery_menu()
        elif choice == "4":
            route_menu()
        elif choice == "5":
            print("🌊 Güle güle kaptan!")
            break
        else:
            print("❌ Geçersiz seçim.")

# ---------------- Görev Günlüğü ----------------
def mission_menu():
    while True:
        print("\n--- Görev Günlüğü ---")
        print("1. Yeni görev ekle")
        print("2. Görevleri listele")
        print("3. Görevi tamamla")
        print("4. Geri dön")
        ch = input("Seçim: ")
        if ch == "1":
            loc = input("Konum: ")
            note = input("Not: ")
            mission_log.add_mission(loc, note)
        elif ch == "2":
            mission_log.list_missions()
        elif ch == "3":
            try:
                mid = int(input("Tamamlanacak görev ID: "))
                mission_log.complete_mission(mid)
            except ValueError:
                print("Geçerli bir sayı gir.")
        elif ch == "4":
            break
        else:
            print("❌ Geçersiz seçim.")

# ---------------- Dalış Günlüğü ----------------
def dive_menu():
    while True:
        print("\n--- Dalış Günlüğü ---")
        print("1. Yeni dalış kaydı")
        print("2. Dalışları listele")
        print("3. Geri dön")
        ch = input("Seçim: ")
        if ch == "1":
            try:
                depth = float(input("Derinlik (metre): "))
                duration = int(input("Süre (dakika): "))
                temp = float(input("Sıcaklık (°C): "))
                note = input("Not: ")
                dive_log.add_dive(depth, duration, temp, note)
            except ValueError:
                print("Geçerli sayı girin.")
        elif ch == "2":
            dive_log.list_dives()
        elif ch == "3":
            break
        else:
            print("❌ Geçersiz seçim.")

# ---------------- Keşif Günlüğü ----------------
def discovery_menu():
    while True:
        print("\n--- Keşif Günlüğü ---")
        print("1. Yeni keşif ekle")
        print("2. Keşifleri listele")
        print("3. Geri dön")
        ch = input("Seçim: ")
        if ch == "1":
            title = input("Başlık: ")
            location = input("Konum: ")
            desc = input("Açıklama: ")
            discovery_log.add_discovery(title, location, desc)
        elif ch == "2":
            discovery_log.list_discoveries()
        elif ch == "3":
            break
        else:
            print("❌ Geçersiz seçim.")

# ---------------- Rota Günlüğü ----------------
def route_menu():
    while True:
        print("\n--- Rota Günlüğü ---")
        print("1. Yeni rota ekle")
        print("2. Rotaları listele")
        print("3. Geri dön")
        ch = input("Seçim: ")
        if ch == "1":
            name = input("Rota adı: ")
            coords = []
            print("📌 Koordinatları gir (bitirmek için 'b' yaz):")
            while True:
                lat = input("  Enlem (lat): ")
                if lat.lower() == "b":
                    break
                lon = input("  Boylam (lon): ")
                try:
                    coords.append((float(lat), float(lon)))
                except ValueError:
                    print("Geçersiz koordinat, tekrar dene.")
            note = input("Not: ")
            route_log.add_route(name, coords, note)
        elif ch == "2":
            route_log.list_routes()
        elif ch == "3":
            break
        else:
            print("❌ Geçersiz seçim.")

# ---------------- Ana Başlatıcı ----------------
if __name__ == "__main__":
    menu()
