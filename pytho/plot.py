from matplotlib import pyplot as plt
import math

def t(x):
    return math.sin(x)

def test(mi,ma,f):
    x = [i/1000 for i in range(int(mi*1000),int(ma*1000))]
    y = []
    for i in x:
        y.append(f(i))
    

    plt.plot(x,y)
    plt.show()

test(0,10,t)
