import csv
import json

def csv_to_config_json(csv_datei, ausgabe_json_datei):
    quadranten = ["Techniques", "Platforms", "Tools", "Languages & Frameworks"]
    ringe = ["Adopt", "Trial", "Assess", "Hold"]
    eintraege = []
    
    with open(csv_datei, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
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
        reader = csv.DictReader(f)
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
    csv_to_config_json("input.csv", "config.json")
    csv_to_markdown("input.csv", "tech_radar.md")