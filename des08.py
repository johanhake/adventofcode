import numpy as np

def utsikts_verdi_rad(høyde_utslag):
    if høyde_utslag.any():
        return np.argmax(høyde_utslag)+1
    # Hvis treet er høyere enn ALL i raden returneres lengden på raden
    return len(høyde_utslag)

with open("input/input-8.1.txt") as f:
    
    rader = f.read().strip().split("\n")
    #rader = ["30373","25512","65332","33549","35390"]
    høyder = []
    for rad in rader:
        høyder.append([int(tre) for tre in rad])

    # Lager en array med alle høydene
    høyder = np.array(høyder, dtype=int)
    
    # Lager en array for synlige treer
    synlig = np.zeros(høyder.shape, dtype=bool)
    
    # Lager en array for utsiktsscore
    utsikt_verdi = np.ones(høyder.shape, dtype=int)
    
    # Setter randen til synlig
    synlig[:,0] = 1
    synlig[:,-1] = 1
    synlig[0,:] = 1
    synlig[-1,:] = 1
    
    print(høyder)
    # Går igjennom radene fra toppen
    for rad in range(1,høyder.shape[0]-1):
        for kol in range(1,høyder.shape[1]-1):
            if (høyder[rad, kol] > høyder[:rad, kol]).all():
                #print(rad, kol, høyder[rad, kol] > høyder[:rad, kol], "topp")
                synlig[rad, kol] = 1
                
    # Går igjennom radene fra bunn
    for rad in range(høyder.shape[0]-2, 0, -1):
        for kol in range(1,høyder.shape[1]-1):
            if (høyder[rad, kol] > høyder[rad+1:, kol]).all():
                #print(rad, kol, høyder[rad, kol] > høyder[rad+1:, kol], "bunn")
                synlig[rad, kol] = 1
                
    for kol in range(1,høyder.shape[1]-1):
        for rad in range(1,høyder.shape[0]-1):
            if (høyder[rad, kol] > høyder[rad, :kol]).all():
                synlig[rad, kol] = 1

    for kol in range(høyder.shape[0]-2, 0, -1):
        for rad in range(1,høyder.shape[0]-1):
            if (høyder[rad, kol] > høyder[rad, kol+1:]).all():
                synlig[rad, kol] = 1

    # Sjekker utsikts verdiene
    for rad in range(1,høyder.shape[0]-1):
        for kol in range(1,høyder.shape[1]-1):
            # Kolonne bidrag
            utsikt_verdi[rad, kol] *= utsikts_verdi_rad(høyder[rad, kol]<=høyder[:rad, kol][::-1])
            utsikt_verdi[rad, kol] *= utsikts_verdi_rad(høyder[rad, kol]<=høyder[rad+1:, kol])
 
             # Rad bidrag
            utsikt_verdi[rad, kol] *= utsikts_verdi_rad(høyder[rad, kol]<=høyder[rad, :kol][::-1])
            utsikt_verdi[rad, kol] *= utsikts_verdi_rad(høyder[rad, kol]<=høyder[rad, kol+1:]) 

#print(f"{høyder} - {utsikt_verdi}")

print("Synlige trer:", synlig.sum())
print("Størst synlighetsverdi trer:", utsikt_verdi.max().max())
    
    