from collections import deque

class Mappe():
    def __init__(self, navn, forelder, root):
        self.navn = navn
        self.forelder = forelder
        self.root = root
        self.størrelse = 0
        self.mapper = {}
        
    def __str__(self):
        return f"{self.root}/{self.navn} - {self.størrelse}"

mapper = []

with open("input/input-7.1.txt") as f:
    kommandoer = deque(f.read().split("\n"))
    kommandoer.popleft()
    mappe = Mappe("root", None, "")
    
    tot_under_100000 = 0
    while kommandoer:
        kommando = kommandoer.popleft()
        
        while "$" not in kommando and kommandoer:
            split = kommando.split(" ")
            # Finner vi en mappe
            if split[0]=="dir":
                # Legg til en mappe til mapper
                mappe.mapper[split[1]] = Mappe(split[1], mappe, mappe.root + "/" + mappe.navn)
            else:
                # Adder filstørrelsene i mappen
                mappe.størrelse += int(split[0])
                
            kommando = kommandoer.popleft()
        
        # Hvis en ls
        if "$ ls" in kommando:
            #print(mappe.navn, mappe.størrelse)
            pass
        
        # Går opp en mappe
        if "$ cd .." in kommando:
            
            print(mappe)
            
            mapper.append((mappe.størrelse, mappe.navn))
            
            # Hvis mappestørrelsen er under 100 000 
            if mappe.størrelse <= 100000:
                tot_under_100000 += mappe.størrelse

            mappe.forelder.størrelse += mappe.størrelse
            mappe = mappe.forelder
            

        # Gå inn i en mappe
        elif "$ cd" in kommando:
            print(kommando)
            navn = kommando.split(" ")[-1]
            mappe = mappe.mapper[navn]
    
    # Går opp til root mappen
    while mappe.navn != "root":
        print(mappe)
        mapper.append((mappe.størrelse, mappe.navn))
        mappe.forelder.størrelse += mappe.størrelse
        mappe = mappe.forelder
    
    # Viser root mappen
    mapper.append((mappe.størrelse, mappe.navn))    
    print(mappe)
    
    # Sorterer alle mappene etter størrelser
    mapper.sort(reverse=True)
    
    # Finner nok plass
    brukt = mappe.størrelse
    forrige = brukt
    i = 0
    total = 70000000
    nokk = 30000000
    while (total - (brukt-mapper[i][0])) >= nokk:
        i+=1
        
    print("Tot under 100000:", tot_under_100000)
    print("Slett:", mapper[i-1][0])
    print(total - (brukt-mapper[i-1][0]))