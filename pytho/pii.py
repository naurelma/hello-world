import matikka
import random
import math


def pii(rep = 1000, roll = 120):
    f = random.random
    total = 0
    count = 0
    #print (f())
    while count < rep:
        if matikka.syt(int(f()*roll),int(f()*roll))==1:
            total = total + 1
        count += 1
        #print(total,count,roll,rep)
    return math.sqrt(6/(total/rep))
