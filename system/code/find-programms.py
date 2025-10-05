import os
import json

# Basisverzeichnisse automatisch setzen
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
PROGRAMMS_PATH = os.path.join(BASE_PATH, "programms")
JSON_PATH = os.path.join(BASE_PATH, "system", "code", "programms.json")

def programme_zu_json():
    programme = []

    # Prüfen, ob der Programme-Ordner existiert
    if not os.path.exists(PROGRAMMS_PATH):
        print(f"❌ Ordner '{PROGRAMMS_PATH}' wurde nicht gefunden.")
        return

    print("🔍 Suche nach Programmen in:", PROGRAMMS_PATH)
    print("--------------------------------------------------")

    # Alle Unterordner (Programme) durchgehen
    for unterordner in os.listdir(PROGRAMMS_PATH):
        unterordner_pfad = os.path.join(PROGRAMMS_PATH, unterordner)
        if not os.path.isdir(unterordner_pfad):
            continue

        icon_pfad = os.path.join(unterordner_pfad, "icon.png")
        index_pfad = os.path.join(unterordner_pfad, "index.html")

        # Suche nach .name-Datei
        name_datei = None
        for datei in os.listdir(unterordner_pfad):
            if datei.endswith(".name"):
                name_datei = datei
                break

        # Fehlende Dateien melden
        fehlermeldungen = []
        if not name_datei:
            fehlermeldungen.append("❌ .name fehlt")
        if not os.path.exists(icon_pfad):
            fehlermeldungen.append("⚠️ icon.png fehlt")
        if not os.path.exists(index_pfad):
            fehlermeldungen.append("⚠️ index.html fehlt")

        if fehlermeldungen:
            print(f"[{unterordner}] -> " + ", ".join(fehlermeldungen))
            # Programme ohne .name werden übersprungen
            if not name_datei:
                continue

        programmname = name_datei.replace(".name", "")

        programm_info = {
            "programmname": programmname,
            "icon": os.path.abspath(icon_pfad),
            "index": os.path.abspath(index_pfad)
        }

        programme.append(programm_info)
        print(f"✅ {programmname} erfolgreich hinzugefügt")

    # Ordner für JSON-Datei sicherstellen
    os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)

    # JSON leeren & neu schreiben
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(programme, f, ensure_ascii=False, indent=4)

    print("--------------------------------------------------")
    print(f"💾 {len(programme)} Programme gespeichert in: {JSON_PATH}")

if __name__ == "__main__":
    programme_zu_json()
