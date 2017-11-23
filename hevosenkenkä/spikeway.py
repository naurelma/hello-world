import numpy as np
import cv2
import time
from vintravel import esine, push, merkki
import math
    

img = np.zeros((512,512,3), np.uint8)



def reset():
    global img
    img = np.zeros((512,1512,3), np.uint8)

def cvt(pos):
    return (pos[0],512-pos[1])


def ai(nopeus,arvo):
    con = 1000
    if arvo[1] > -90:
        return 0
    elif arvo[1] > -150:
        return con*100
    elif arvo[0]>50 and nopeus < 75:
        return -con/2-arvo[0]*0
    else:
        return 0
        

def pros(pl,coins):
    vect = []
    pituudet = []
    kulmat = []
    for i in coins:
        vect.append(pl.suunta(i))
    for i in vect:
        pituudet.append(math.hypot(i[0],i[1]))
    for p,s in zip(pituudet, vect):
        if p != 0:
            kulmat.append(merkki(s[1])*math.degrees(math.acos(s[0]/p)))
        else:
            kulmat.append(0)
    for i, v in enumerate(zip(pituudet,kulmat)):
        pl,coins[i] = push(pl,coins[i],ai(coins[i].nopeus(),v))


a = esine(100)
arr =[esine(10000) for i in range(20)]

a.pos = [150,100]
a.speed = [-1000,0]
for i in range(len(arr)):
    arr[i].pos = [(i
                   )*100,1]
lastTime = time.time()
#a.speed =[50,0]
while(True):
    kulu = time.time()-lastTime
    lastTime = time.time()
    reset()
    if a.pos[0] > 1500:
        a.pos = [0,a.pos[1]]
    elif a.pos[0] <0:
        a.pos = [1500,a.pos[1]]
    pros(a,arr)


    a.move(kulu)
    for i in range(len(arr)):
        arr[i].move(kulu)
                            
    cv2.circle(img,cvt(a.paikka()), 4, (0,0,255), -1)
    for i in range(len(arr)):
        cv2.circle(img,cvt(arr[i].paikka()), 4, (0,255,0), -1)

    cv2.imshow('window',img)
    #time.sleep(0.1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


    
