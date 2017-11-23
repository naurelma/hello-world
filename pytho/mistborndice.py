from random import random
from math import ceil
def roll(num = 2):
	heitto = []
	for i in range(num):
		heitto.append(ceil(6*random()))
	lkm = [0,0,0,0,0,0]
	for i in range(6):
		lkm[i]=heitto.count(i+1)
	nudge = lkm.pop()
	curr = 0
	for i in range(5):
		if lkm[i] >1:
			curr = i+1
	return (curr,nudge)

def laske(arr):
	suurin = max(arr)
	if suurin<6:
            suurin = 5
	lista = []
	for i in range(suurin+1):
		lista.append(arr.count(i))
	return lista

def laske2(arr, die = 10):
        tulos = {}
        for i in range(die+1):
                for j in range(6):
                        tulos[(j,i)]=0
        for i in arr:
                tulos[i] += 1
        return tulos

def test2(num=2,rep=1000):
	a = []
	for i in range(rep):
		a.append(roll(num))		
	return a


def test(num=2,rep=1000):
	a = []
	b = []
	for i in range(rep):
		x,y = roll(num)
		a.append(x)
		b.append(y)
	return (a,b)

def quick(rep=1000):
    tulos = []
    for i in range(2,11):
        a,b = test(i,rep)
        tulos.append(laske(a))
    return tulos

def tulosta(arr,die):
        for j in range(die+1):
                for i in range(6):
                        print(arr[i,j],end =", ")
                print()
        for i in range(13-die):
                print(0)

                
def quick2(die=2,rep=1000):
        tulosta(laske2(test2(die,rep),die),die)
    
def qtulos(rep = 1000):
    a = quick(rep)
    for i in a:
        for j in i:
            print(j,end=", ")
        print()

def count(arr):
        lkm = [0,0,0,0,0,0]
        for i in range(6):
                lkm[i]=arr.count(i+1)
        nudge = lkm.pop()
        curr = 0
        for i in range(5):
                if lkm[i]>1:
                        curr=i+1
        return (curr,nudge)



def dec(d = 0):
	dice[d] -= 1
	if dice[d] == 0:
		dice[d]=6
		if(d+1==len(dice)):
                        #dice[0]=7
			return True
		else:
			return dec(d+1)
	else:
		return False

        
