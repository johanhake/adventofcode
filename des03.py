# Bruker ASCII koden til hver bokstav
skift_lower = ord("a")-1
skift_upper =ord("A")-1-26

"Returnerer prioriteten til en bokstav. Bruker ASCII koden til bokstaven "
def prioritet(hva):
        return ord(hva)-skift_lower if hva.islower() else ord(hva)-skift_upper

with open("input-3.1.txt") as f:
    prioriteter = []
    grupp_prioriteter = []
    grupp_innhold = []
    # Samler opp alle prioriteterne
    for i, pakning in enumerate(f.readlines()):
        pakning = pakning[:-1] # Fjerner nylinje
        halvt_antall = len(pakning)//2
        
        # Splitter pakningen i to 
        utrymme1, utrymme2 = set(pakning[:halvt_antall]), set(pakning[halvt_antall:])
        
        # Tar vare på lik bokstav
        prioriteter.extend(utrymme1.intersection(utrymme2))
        
        # Legger inn pakningen i en grupp
        grupp_innhold.append(set(pakning))

        # Har vi en grupp på tre?
        if (i+1) % 3 == 0:
            # Samler opp innhold som er likt i en grupp
            grupp_prioriteter.extend(grupp_innhold[0].intersection(grupp_innhold[1].intersection(grupp_innhold[2])))
            grupp_innhold = []
    
    # Summerer opp tall ekvivalenten til de ulike prioritetene
    print("Sum prioriteter alle:", sum(prioritet(p) for p in prioriteter))
    print("Sum prioriteter grupper:", sum(prioritet(p) for p in grupp_prioriteter))