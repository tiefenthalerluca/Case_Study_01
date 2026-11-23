# Case Study 01 – Geräteverwaltung

Im Fach Algorithmen & Datenstrukturen am MCI Innsbruck entwickeln wir eine Geräteverwaltung mit Python. Für die Oberfläche ist Streamlit vorgesehen, für die Datenspeicherung TinyDB.

## Einrichtung auf dem Mac

Öffne den Ordner `Case_Study_01` in VS Code und wähle **Terminal → Neues Terminal**. Führe diese drei Zeilen der Reihe nach aus. Dafür brauchst du Python 3, zum Beispiel Python 3.12.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Die `.venv` bleibt auf deinem Rechner. Wenn du später ein neues Terminal öffnest, aktivierst du sie wieder mit `source .venv/bin/activate`.

## Installation testen

Mit `python hello_world.py` erscheint `Hello World` im Terminal. Mit dem folgenden Befehl öffnest du die Streamlit-Demo im Browser.

```bash
python -m streamlit hello
```

Mit `Ctrl+C` im Terminal beendest du die Demo.

## Einrichtung auf Windows

Öffne den Ordner `Case_Study_01` in VS Code und wähle **Terminal → Neues Terminal**. Führe diese drei Zeilen der Reihe nach aus. Dafür brauchst du Python 3, zum Beispiel Python 3.12.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Die `.venv` bleibt auf deinem Rechner. Wenn du später ein neues Terminal öffnest, aktivierst du sie wieder mit:

```powershell
.venv\Scripts\Activate.ps1
```

### Falls PowerShell die Aktivierung blockiert

Falls Windows meldet, dass die Ausführung von Skripten deaktiviert ist, führe folgenden Befehl aus:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Aktiviere anschließend die virtuelle Umgebung erneut:

```powershell
.venv\Scripts\Activate.ps1
```

Diese Einstellung gilt nur für das aktuelle PowerShell-Terminal.
