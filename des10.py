
with open("input/input-10.1.txt") as f:
    
    instr = f.read().strip().split("\n")
    instr = [int(inst.split(" ")[1]) if len(inst.split(" "))==2 else 0 for inst in instr][::-1]
    
    cycle = 1
    X = 1
    signal_styrke = 0
    output = ""
    while instr:
        inst = instr.pop()
        delay = 1 if inst == 0 else 2
        while delay:
            delay -= 1
            if (cycle - 20) % 40 == 0:
                signal_styrke += cycle*X
                #print(cycle, cycle*X)
            #print(X, cycle)
            
            # Er spriten innenfor cyclusen
            if X <= cycle % 40 < X+3:
                output += "#"
            else:
                output += "."

            if cycle % 40 == 0:
                output += "\n"
                
            cycle += 1
                
        X += inst
        
    print("Signalstyrke:", signal_styrke)
    # Har en bug som ikke viser helt riktig siste kolonne!
    print(output)
    
    