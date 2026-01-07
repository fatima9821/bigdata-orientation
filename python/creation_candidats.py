import random
import os

def creation_liste_candidats(nb=5000, chemin="../data/Candidats.txt"):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    filieres = ["MP", "PC"]
    with open(chemin, "w", encoding="utf-8") as f:
        for i in range(1, nb + 1):
            cin = f"CIN{i:05d}"
            nom = f"Nom{i}"
            prenom = f"Prenom{i}"
            filiere = random.choice(filieres)
            f.write(f"{cin} {nom} {prenom} {filiere}\n")

if __name__ == "__main__":
    creation_liste_candidats()
