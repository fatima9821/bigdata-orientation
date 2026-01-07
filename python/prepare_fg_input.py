def charger_notes(chemin="../data/Notes.txt"):
    d = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            cin = parts[0]
            notes = list(map(int, parts[1:]))
            d[cin] = notes
    return d

def fusionner(chemin_cand="../data/Candidats.txt",
              chemin_notes="../data/Notes.txt",
              sortie="../data/CandNotes.txt"):
    notes = charger_notes(chemin_notes)
    with open(chemin_cand, "r", encoding="utf-8") as fc, \
         open(sortie, "w", encoding="utf-8") as out:
        for line in fc:
            parts = line.strip().split()
            cin = parts[0]
            if cin in notes:
                out.write(line.strip() + " " +
                          " ".join(map(str, notes[cin])) + "\n")

if __name__ == "__main__":
    fusionner()
