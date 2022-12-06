with open("input/input-6.1.txt") as f:
    melding = f.read()
    # Test
    #melding = "nppdvjthqldpwncqszvftbrmjlhg"
    start_pakke = 4
    while start_pakke < len(melding):
        unike = set(melding[start_pakke-4:start_pakke])
        if (len(unike)==4):
            break
        start_pakke += 1
    
    print("Pakke starter etter:", start_pakke)

    # Test
    #melding = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    start_beskjed = 14
    while start_beskjed < len(melding):
        unike = set(melding[start_beskjed-14:start_beskjed])
        if (len(unike)==14):
            break
        start_beskjed += 1
    print("Beskjed starter etter:", start_beskjed)
