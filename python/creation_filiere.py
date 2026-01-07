import json
import os

def creation_filiere(chemin="../data/Filiere.json"):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    filiere = {
        "MP": ["E101", 200],
        "PC": ["E205", 150]
    }
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(filiere, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    creation_filiere()
