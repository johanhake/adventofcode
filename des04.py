with open("input-4.1.txt") as f:
    antall_full_overlapp = 0
    antall_overlapp = 0
    
    # Går igjennom alle seksjonene
    for i, seksjoner in enumerate(f.readlines()):
        # Henter ut de to intervallene
        s1, s2 = seksjoner[:-1].split(",")
        start1, slutt1 = [int(s) for s in s1.split("-")]
        start2, slutt2 = [int(s) for s in s2.split("-")]

        # Adderer mulig overlapp (True == 1)
        antall_full_overlapp += (start1 >= start2 and slutt1 <= slutt2) or \
                                (start1 <= start2 and slutt1 >= slutt2)
            
        # Adderer ikke (ikke overlapp) (True == 1)
        antall_overlapp += not (start1 > slutt2 or start2 > slutt1)
            
    print("Antall som har full overlapp:", antall_full_overlapp)
    print("Antall som har overlapp:", antall_overlapp)
