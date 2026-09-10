# Password Generator (Python)

Ein einfaches Kommandozeilen-Tool in Python, das sichere, zufällige Passwörter erzeugt.  
Es nutzt das `secrets`-Modul für kryptografisch starke Zufälligkeit.

## Features

- Konfigurierbare Länge
- Wahlweise Groß-/Kleinbuchstaben, Ziffern, Sonderzeichen
- Option, mehrdeutige Zeichen (0, O, 1, l, I) zu vermeiden
- Mehrere Passwörter auf einmal generieren

## Voraussetzungen

- Python 3.8 oder höher
- Keine zusätzlichen Pakete nötig (nur Standardbibliothek)

## Installation

1. Repository klonen:

   ```bash
   git clone https://github.com/DEIN_USER/password-generator.git
   cd password-generator
   ```

2. (Optional) Virtuelle Umgebung erstellen:

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

## Verwendung

Ein Passwort mit Standardlänge (16 Zeichen):

```bash
python password_generator.py
```

Länge anpassen:

```bash
python password_generator.py -l 20
```

Keine Sonderzeichen, keine mehrdeutigen Zeichen:

```bash
python password_generator.py -l 12 --no-punct --avoid-ambiguous
```

Mehrere Passwörter auf einmal:

```bash
python password_generator.py -n 5 -l 16
```

Alle Optionen anzeigen:

```bash
python password_generator.py --help
```

## Beispiel

```bash
$ python password_generator.py -l 12 --avoid-ambiguous
a7zK9mP3xR2b
```
## Lizenz

MIT
