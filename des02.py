"""
A Rock
B Paper
C Scissors
X Rock 1
Y Paper 2
Z Scissors 3
"""

poeng1 = {
    "A X\n" : 3+1,
    "A Y\n" : 6+2,
    "A Z\n" : 0+3,
    "B X\n" : 0+1,
    "B Y\n" : 3+2,
    "B Z\n" : 6+3,
    "C X\n" : 6+1,
    "C Y\n" : 0+2,
    "C Z\n" : 3+3,
    }

"""
A Rock 1
B Paper 2
C Scissors 3
X tap
Y uavgjort
Z vinst
"""

poeng2 = {
    "A X\n" : 0+3,
    "A Y\n" : 3+1,
    "A Z\n" : 6+2,
    "B X\n" : 0+1,
    "B Y\n" : 3+2,
    "B Z\n" : 6+3,
    "C X\n" : 0+2,
    "C Y\n" : 3+3,
    "C Z\n" : 6+1,
    }

with open("input/input-2.1.txt") as f:
    resultat = f.readlines()
    print("Poeng spill 1:", sum(poeng1[r] for r in resultat))
    print("Poeng spill 2:", sum(poeng2[r] for r in resultat))

