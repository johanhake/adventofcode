import numpy as np
with open("input/input-1.1.txt") as f:
    
    sum = 0
    calories = []
    for tall in f.readlines():
        if tall != "\n":
            sum += int(tall)
        else:
            calories.append(sum)
            sum = 0

calories = np.array(calories)
print("Elf nr:", calories.argmax()+1, "kalorier:", calories.max())
print("Topp tre Elfs nr:", calories.argsort()[-3:]+1, "kalorier:", np.sort(calories)[-3:].sum())

