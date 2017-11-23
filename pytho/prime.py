import math

def is_prime(x):
    if x%2==0:
        return False
    for i in range(3,1+int(x//2),2):
        if x%i == 0:
            return False
    return True


def next_prime(x):
    i = x +1
    while not is_prime(i):
        i +=1
    return i


def prime_gen(alku, loppu):
    i = 0
    while i < loppu:
        alku = next_prime(alku)
        i += 1
        yield alku
        
def factor(x):
    if x%2==0:
        return [2,x//2]
    for i in range(3,1+int(x//2),2):
        if x%i==0:
            return [i,x//i]
    return [1,x]

def tulo(x):
    a = 1
    for i in x:
        a*=i
    return a
	
def prime_factor(x):
    tekijät = []
    tulos = 1
    luku = x
    while x%2==0:
        tekijät.append(2)
        x = x//2
        tulos *= 2
    for i in range(3,x+1,2):
        while x%i==0:
            tekijät.append(i)
            x = x//i
            tulos *= i
            if tulos == luku and tulo(tekijät)==luku:
                return tekijät
    return tekijät






        
