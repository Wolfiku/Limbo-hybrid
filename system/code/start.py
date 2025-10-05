import subprocess
import os
import webbrowser
import time
import threading

# Basisverzeichnis (Limbo-hybrid)
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
SYSTEM_PATH = os.path.join(BASE_PATH, "system", "code")
INDEX_PATH = os.path.join(BASE_PATH, "index.html")

def starte_find_programms():
    """Findet und speichert Programme"""
    print("🔍 Starte 'find-programms.py' ...")
    subprocess.run(["python", os.path.join(SYSTEM_PATH, "find-programms.py")], check=True)
    print("✅ Programme aktualisiert!\n")

def starte_server():
    """Startet lokalen Server im Hintergrund"""
    print("🌐 Starte lokalen Server auf Port 8000 ...")
    os.chdir(BASE_PATH)
    subprocess.run(["python", "-m", "http.server", "8000"])

def starte_browser():
    """Öffnet index.html im Browser (localhost)"""
    time.sleep(2)  # kurze Verzögerung, damit Server startet
    url = "http://localhost:8000/index.html"
    print("🚀 Öffne Browser:", url)
    webbrowser.open(url, new=1, autoraise=True)

if __name__ == "__main__":
    # Schritt 1: Programme aktualisieren
    starte_find_programms()

    # Schritt 2: Server starten (im eigenen Thread)
    server_thread = threading.Thread(target=starte_server, daemon=True)
    server_thread.start()

    # Schritt 3: Browser öffnen
    starte_browser()

    print("\n💡 Drücke STRG + C zum Beenden des Servers.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Server beendet.")
