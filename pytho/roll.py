import random
def roll(mod = 0, rep = 20):
    total = mod
    for i in range(rep):
        if random.random()>0.5:
            total += 1
        else:
            total -= 1
    if total == 0:
        if random.random()>0.5:
            total += 1
        else:
            total -= 1
    return int(total)

def avg(x):
    a = 0
    for i in x:
        a+=i
    return a/len(x)
