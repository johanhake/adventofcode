import re

# regexp mønster for flytt instruksjoner og crates
flytt_mønster = "^move (\d+) from (\d+) to (\d+)\n$"
crate_mønster = ("(\[\S\]|   ) "*9)[:-1]

with open("input/input-5.1.txt") as f:
    linjer = f.readlines()
    
    start_plassering = []
    for start_i, linje in enumerate(linjer):
        if (linje == "\n"):
            break
        # Fjerner nylinje
        start_plassering.append(linje[:-1])
    
    print(start_plassering[-2::-1])
    
    # Alle de ulike cratesene
    alle_crates = [[] for _ in range(9)]
    alle_crates2 = [[] for _ in range(9)]
     
    # Går igjennom de ulike linjene i omvendt rekkefølge
    for crates in start_plassering[-2::-1]:
        for i, crate in enumerate(re.findall(crate_mønster, crates)[0]):
            if crate != "   ":
                alle_crates[i].append(crate[1])
                alle_crates2[i].append(crate[1])
        print(re.findall(crate_mønster, crates)[0])
        
    instruksjoner = linjer[start_i+1:]
    
    # Går igjennom alle instruksjonene henter ut antall, fra og til
    for linje in instruksjoner:
        antall, fra, til = [int(t) for t in re.findall(flytt_mønster, linje)[0]]
        # Flytter crates etter CrateMover 9000
        flytt = []
        for i in range(antall):
            alle_crates[til-1].append(alle_crates[fra-1].pop())
            flytt.append(alle_crates2[fra-1].pop())

        # Flytter crates etter CrateMover 9001 (reverserer ordningen!)
        alle_crates2[til-1].extend(flytt[::-1])
        
    # Printer bokstavskombinasjonen til de øverste cratesene
    print("CrateMover 9000:", "".join(crate[-1] for crate in alle_crates))
    print("CrateMover 9001:", "".join(crate[-1] for crate in alle_crates2))