import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import random

fig, ax = plt.subplots()
a = np.zeros(101)
a[len(a)//8]=500
a[-(len(a)//2)]=-500
a[-(len(a)//8)]=500
line, = ax.plot(a)

ax.set_ylim(-20, 20)


def area(y, h=1):
    """puolisuunnikas säännön perusteella laskettu pinta-ala"""
    result = 0.5*(y[0]+y[-1])
    result += sum(y[1:-1])
    return result*h


def update(data):
    line.set_ydata(data)
    return line,

def data_gen():
    global TOTAL
    while True :
        a = line.get_ydata()
        a = flow(a)
        #a[a < 0] = 0
        #a[a > 50] = 50
        #a[int(random()*len(a))] +=2
        yield a
        

def flow(arr):
    total = sum(arr)
    
    keskiarvo = np.zeros(len(arr))
    keskiarvo[0] = (arr[0]+arr[1])/2
    keskiarvo[-1] = (arr[-1]+arr[-2])/2
    for i, v in enumerate(zip(arr[:-2], arr[2:])):
        keskiarvo[i+1] += (sum(v)+arr[i+1]) / 3
    
    diff = (sum(keskiarvo) - total)/len(keskiarvo)
    keskiarvo += diff
    
    return keskiarvo
    



plt.grid(True)
ani = animation.FuncAnimation(fig, update, data_gen, interval=1)
plt.show()
