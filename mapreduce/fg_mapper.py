#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    # CIN Nom Prenom Filiere + 8 notes = 12 éléments
    if len(parts) != 12:
        continue
    cin = parts[0]
    try:
        notes = list(map(int, parts[4:]))
    except ValueError:
        continue
    analyse, algebre, physique, chimie, info, sta, fr, ang = notes
    fg = (analyse*8 + algebre*6 + physique*8 + chimie*6 +
          info*6 + sta*4 + fr*3 + ang*3)
    print(f"{cin}\t{fg}")
