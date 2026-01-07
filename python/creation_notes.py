import random
import os

def creation_notes(nb=5000, chemin="../data/Notes.txt"):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        for i in range(1, nb + 1):
            cin = f"CIN{i:05d}"
            notes = [random.randint(0, 20) for _ in range(8)]
            f.write(cin + " " + " ".join(map(str, notes)) + "\n")

if __name__ == "__main__":
    creation_notes()
