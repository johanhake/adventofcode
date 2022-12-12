import numpy as np


retning = {
 "U": np.array([0,1]),
 "D": np.array([0,-1]),
 "R": np.array([1,0]),
 "L": np.array([-1,0])
 }

with open("input/input-9.1.txt") as f:
    
    # Debug
    innhold = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    # Leser fil
    innhold = f.read().strip()
    head_moves = [(move.split(" ")[0], int(move.split(" ")[1])) for move in innhold.split("\n")]
    heads = [np.array([0,0])]
    tails = [np.array([0,0])]
    
    for d, antall in head_moves:
        for _ in range(antall):
            heads.append(heads[-1]+retning[d])
            diff = heads[-1]-tails[-1]
            
            # Flytter bare hvis maks differanse er 2
            if np.absolute(diff).max()>1:
                # Flytter halen fortegnet til differansen.
               tails.append(np.sign(diff)+tails[-1])
    
    # Rensker ut dubletter
    tails = set(tuple(t) for t in tails)
    
    # Litt flere knuter
    knots = [[np.array([0,0])] for _ in range(10)]
    for d, antall in head_moves:
        for _ in range(antall):
            # Flytter første knuten
            knots[0].append(knots[0][-1]+retning[d])
            
            # Flytter de andre knutene
            for k in range(1, 10):
                diff = knots[k-1][-1]-knots[k][-1]
            
                # Flytter bare hvis maks differanse er 2
                if np.absolute(diff).max()>1:
                    # Flytter halen fortegnet til differansen.
                   knots[k].append(np.sign(diff)+knots[k][-1])

    # Rensker ut dubletter
    tails2 = set(tuple(t) for t in knots[-1])    
    print("Antall unike posisjoner for halen:", len(tails))
    print("Antall unike posisjoner for halen 2:", len(tails2))
    
