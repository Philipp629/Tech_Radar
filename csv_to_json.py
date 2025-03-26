import csv
import json
import sys

def csv_to_config_json(csv_datei, ausgabe_json_datei):
    quadranten = ["Techniken", "Plattformen", "Werkzeuge", "Sprachen & Frameworks"]
    ringe = ["Adoptieren", "Testen", "Bewerten", "Halten"]
    eintraege = []
    
    with open(csv_datei, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')  # Semikolon als Trennzeichen
        for zeile in reader:
            eintrag = {
                "label": zeile["name"],
                "quadrant": quadranten.index(zeile["quadrant"].strip()),
                "ring": ringe.index(zeile["ring"].strip()),
                "moved": 0 if zeile.get("isNew", "FALSE").upper() == "FALSE" else 1,
                "active": True
            }
            eintraege.append(eintrag)
    
    config = {"entries": eintraege, "quadrants": quadranten, "rings": ringe}
    with open(ausgabe_json_datei, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print(f"Erstellte Datei: {ausgabe_json_datei}")

def csv_to_markdown(csv_datei, ausgabe_md_datei):
    radar = {}
    blip_nummer = 1
    
    with open(csv_datei, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')  # Semikolon als Trennzeichen
        for zeile in reader:
            quadrant = zeile["quadrant"].strip()
            ring = zeile["ring"].strip()
            if quadrant not in radar:
                radar[quadrant] = {}
            if ring not in radar[quadrant]:
                radar[quadrant][ring] = []
            nummer = zeile.get("id", str(blip_nummer))
            blip_nummer += 1
            radar[quadrant][ring].append((nummer, zeile["name"], zeile["description"]))
    
    md_inhalt = "# Tech-Radar 2025\n\n"
    for quadrant, ringe in radar.items():
        md_inhalt += f"## {quadrant}\n\n"
        for ring, technologien in ringe.items():
            md_inhalt += f"### {ring}\n\n"
            for nummer, name, beschreibung in technologien:
                md_inhalt += f"{nummer}. **{name}**: {beschreibung}\n"
            md_inhalt += "\n"
    
    with open(ausgabe_md_datei, 'w', encoding='utf-8') as f:
        f.write(md_inhalt)
    print(f"Erstellte Datei: {ausgabe_md_datei}")

if __name__ == "__main__":
    if len(sys.argv) < 2:  # Prüft, ob ein Argument übergeben wurde
        print("Verwendung: python csv_to_json.py <csv-datei>")
        sys.exit(1)
    
    csv_datei = sys.argv[1]  # Der erste Parameter ist der CSV-Dateiname
    # Ausgabedateinamen basierend auf dem Eingabedateinamen generieren
    basis_name = csv_datei.rsplit('.', 1)[0]  # Entfernt die Endung (z. B. "input" aus "input.csv")
    json_datei = f"{basis_name}.json"
    md_datei = f"{basis_name}.md"
    
    csv_to_config_json(csv_datei, json_datei)
    csv_to_markdown(csv_datei, md_datei)