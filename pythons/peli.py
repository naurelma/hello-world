import random

def total(x):
    total = 0
    for i in x:
        total += i
    return total

def _roll(x=6):
    return int(random.random()*x+1)

def peli(lkm=50, pituus=36):
    """yksi peli monopolin tuuppisellä laudalla"""
    visits = [0 for x in range(pituus)]

    current = 0
    for i in range(lkm):
        current += _roll() + _roll()
        if current >= pituus:
            current -= pituus
        visits[current] += 1

    return visits

def keskiarvo(kierrokset = 100, lkm = 50, pituus = 36):
    total = [0 for x in range(pituus)]
    for x in range(kierrokset):
        arr = peli(lkm,pituus)
        for i,v in enumerate(arr):
            total[i]+=v
    #print(total)
    for i,v in enumerate(total):
        total[i] = v/kierrokset

    return total
    

def tod(kierrokset=100,lkm=50,pituus=36):
    arr = keskiarvo(kierrokset,lkm,pituus)
    for i,v in enumerate(arr):
        arr[i] = v/lkm * 100

    return arr

def arvot(kier=100,lkm=50,pituus=36):
    arr = tod(kier,lkm,pituus)
    suurin = 0 #paikka
    suurin_arvo =0
    pienin = 0 #paikka
    pienin_arvo = 100    

    for i,v in enumerate(arr):
        if v<pienin_arvo:
            pienin_arvo = v
            pienin = i
        if v>suurin_arvo:
            suurin_arvo = v
            suurin = i
    print(arr)
    print()
    print("SP=", suurin, "arvo", suurin_arvo, "PP=",pienin,"arvo",pienin_arvo)








    
