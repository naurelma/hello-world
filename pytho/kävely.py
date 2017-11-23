from random import random
dim = 2
endPos = []

def kävely(step=10):
    pos = [0 for i in range(dim)]
    
    for i in range(step):
        askel = int(dim*random())
        if (random() <0.5):
            pos[askel] += 1
        else:
            pos[askel] -= 1
    global endPos
    endPos.append(pos)
    
def lenkki(rep = 100,step = 50):
    for i in range(rep):
        kävely(step)
        
def setDim(d = 2):
    global endPos
    global dim
    dim = d
    endPos = []

def avg():
    global endPos
    lkm = {}
    yht = 0
    for i in endPos:
        yht +=1
        a = tuple(i)
        if a not in lkm:
            lkm[a] = 1
        else:
            lkm[a] += 1

    lkm2 = {}
    for i in range(-16,16):
        for j in range(-16,16):
            if (i,j) not in lkm:
                lkm[(i,j)] = 0
    for i in sorted(lkm):
        lkm2[i] = lkm[i]
    return lkm2

def printtaa(a):
    tyhjä = [[0 for i in range(35)] for i in range(35)]
    for k,v in a.items():
        tyhjä[k[0]+16][k[1]+16]=v
    for i in tyhjä:
       print(i)
    return tyhjä
