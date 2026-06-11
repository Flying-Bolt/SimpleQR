> [!IMPORTANT]
> **Dieses Repository ist umgezogen und wird auf GitHub nicht mehr gepflegt.**
> Die aktuelle Version und die weitere Entwicklung gibt es nur noch auf Codeberg:
> **https://codeberg.org/Flying-Bolt/SimpleQR**

---

# SimpleQR – QR-Code Generator

Ein schlichter, portabler QR-Code-Generator mit grafischer Oberfläche (GUI), geschrieben in Python.

![Screenshot](screenshot.png)

## Features

- Text oder URL in einen QR-Code umwandeln
- Größe des QR-Codes frei einstellbar (Box-Größe 4–20)
- Echtzeit-Vorschau direkt im Fenster
- Export als **PNG** oder **JPEG**
- Keine Installation nötig – läuft als einzelnes Python-Skript
- App-Icon eingebettet (kein externer Asset-Ordner erforderlich)

## Voraussetzungen

- Python 3.8 oder neuer
- pip-Pakete:

```
pip install qrcode[pil] pillow
```

## Verwendung

```bash
python SimpleQR.py
```

1. Text oder URL in das Eingabefeld eintragen
2. Gewünschte QR-Größe mit dem Schieberegler einstellen
3. **„QR-Code erzeugen"** klicken → Vorschau erscheint
4. **„QR-Code speichern"** klicken → Speicherort wählen (PNG/JPEG)

## Projektstruktur

```
SimpleQR/
├── SimpleQR.py      # Hauptskript (Icon eingebettet, keine weiteren Dateien nötig)
├── screenshot.png   # Screenshot der Anwendung
└── README.md
```

## Abhängigkeiten

| Paket | Zweck |
|-------|-------|
| `qrcode[pil]` | QR-Code-Erzeugung |
| `Pillow` | Bildverarbeitung & GUI-Vorschau |
| `tkinter` | GUI-Framework (in Python enthalten) |

## Lizenz

MIT License – frei verwendbar, veränderbar und verteilbar.
