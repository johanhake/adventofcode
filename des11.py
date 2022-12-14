from collections import deque
from functools import reduce

def monkey_buisness(rep):
    with open("input/input-11.1.txt") as f:
        apeinstr = [instr.strip().split("\n") for instr in f.read().split("\n\n")]

        gjenstander = []
        gjenst_insp = [0 for _ in range(len(apeinstr))]
        operasjoner = []
        tester = []
        til_ape = []
        ns = {}
        for i, (apenr, startitems, operasjon, test, sant, falsk) in enumerate(apeinstr):
            gjenstander.append(deque([int(item) for item in startitems.replace("  Starting items: ","").split(", ")]))
            operasjoner.append(operasjon.replace("  Operation: new = ", ""))
            tester.append(int(test.replace("  Test: divisible by ", "")))
            til_ape.append([int(falsk.replace("   If false: throw to monkey ", "")),
                            int(sant.replace("   If true: throw to monkey ", ""))])
    
    mod = reduce(lambda a, b: a*b, tester)
    print(mod)
    # Gå igjennom operasjonene
    for i in range(1, rep+1):
        
        for j, (gster, opr, test, til) in enumerate(zip(gjenstander, operasjoner, tester, til_ape)):
            gjenst_insp[j] += len(gster)
            while gster:
                ns["old"] = gster.popleft()
                nyverdi = eval(opr, ns)
                if rep <= 20 :
                    nyverdi //= 3
                else:
                    nyverdi = nyverdi % mod
                gjenstander[til[(nyverdi // test)*test == nyverdi]].append(nyverdi)
                #gjenstander[til[nyverdi % test == 0]].append(nyverdi)
                
        if i % 100 == 0:
            gjenst_insp_debug = sorted(gjenst_insp)
            #print(gjenstander[0][0])
            print(i, gjenst_insp, gjenst_insp_debug[-1]*gjenst_insp_debug[-2])
            
    gjenst_insp = sorted(gjenst_insp)
    return gjenst_insp[-1]*gjenst_insp[-2]
    

print("Monkey buisness:", monkey_buisness(20))
print("Monkey buisness 2:", monkey_buisness(10000))