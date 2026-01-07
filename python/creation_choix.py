import random
import os

def creation_choix(nb=5000, chemin="../data/Choix.txt"):
    filieres = ["MP", "PC"]
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        for i in range(1, nb + 1):
            cin = f"CIN{i:05d}"
            # On permet des doublons ou on évite, selon ton choix
            choix = random.choices(filieres, k=3)
            f.write(f"{cin} {choix[0]} {choix[1]} {choix[2]}\n")

if __name__ == "__main__":
    creation_choix()
