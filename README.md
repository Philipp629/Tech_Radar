# Tech-Radar-Generator

Dieses Repository enthält ein Python-Skript, um eine Tech-Radar-Konfiguration und Dokumentation aus einer CSV-Datei zu erstellen. Es generiert eine JSON-Datei, die mit dem [Zalando Tech Radar](https://github.com/zalando/tech-radar) kompatibel ist, sowie eine Markdown-Datei mit detaillierten Beschreibungen, um Technologieentscheidungen für Teams einfach zu visualisieren und zu dokumentieren.

## Funktionen
- Konvertiert eine CSV-Datei in:
  - Eine `config.json`-Datei für die Visualisierung im Zalando Tech Radar.
  - Eine `tech_radar.md`-Datei mit strukturierten Beschreibungen, die zu den Radar-Blips passen.
- Flexibler Eingabedateiname: Funktioniert mit jedem CSV-Dateinamen, der als Kommandozeilenargument angegeben wird.
- Unterstützt Quadranten (`Techniques`, `Platforms`, `Tools`, `Languages & Frameworks`) und Ringe (`Adopt`, `Trial`, `Assess`, `Hold`).

## Voraussetzungen
- **Python 3.x**: Stellen Sie sicher, dass Python auf Ihrem System installiert ist (`python --version` zum Überprüfen).
- Keine zusätzlichen Python-Pakete erforderlich, da nur die Standardbibliotheken (`csv`, `json`, `sys`) verwendet werden.

## Installation
1. Klonen Sie dieses Repository:
   ```bash
   git clone <repository-url>
   cd tech-radar-generator
