myy = 1.9
#G = g*m*m/r**2
from time import sleep
from math import sqrt, sin, cos, hypot

def summa(arr):
    vert = []
    vaak = []
    for i in arr:
        vaak.append(i[0])
        vert.append(i[1])
    vert = sum(vert)
    vaak = sum(vaak)
    return [vaak,vert]

def merkki(num):
    if num == 0:
        return 0
    else:
        return num/abs(num)

def push(a,b,mul):
    """a,b ovat esineitä, mul on väliltä [-1,1] """

    if a.pos == b.pos:
        return a,b
    # f = k/r
    väli = a.suunta(b)
    d = sqrt(väli[0]**2+väli[1]**2)
    if d == 0:
        return a,b
    yksi = [väli[0]/d,väli[1]/d]#a->b
    f = 100/(d**2)
    a.forces.append([-f*yksi[0]*mul,-f*yksi[1]*mul])
    b.forces.append([f*yksi[0]*mul,f*yksi[1]*mul])
    return a,b
    
    
class esine:
    def __init__(self,mass):
        self.mass = mass
        self.forces = []
        self.speed = [0.0,0.0]
        self.pos = [0.0,0.0] #[x,y]
    
    def _grav(self):
        self.forces.append((0,-10*self.mass))
    
    def _kitka(self,f, aika):           
        if f[1] >0:
            return f
        kitka = [myy*f[1]*merkki(self.speed[0]),myy*f[1]*merkki(f[0])] #vaihto ehdo kumpaankin [-,0,+]
        if kitka[0] == 0:
            kitka = kitka[1]
        else:
            kitka = kitka[0]
        f[0] += kitka
        if merkki(self.speed[0]) != merkki(self.speed[0] + f[0]*aika):
            self.speed[0] = 0
            f[0] = 0
        
        return f

    def suunta(self,other):
        a = self.paikka()
        b = other.paikka()
        return [b[0]-a[0],b[1]-a[1]]

    def nopeus(self):
        return hypot(self.speed[0],self.speed[1])
    
    def _osu(self,f):#negatiivinen jos ei voi osua näillä arvoilla
        try:
            y = self.pos[1]
            v = self.speed[1]
            m = self.mass
            if v>=0 and f>=0:
                return -1
            elif f == 0 and v != 0:
                return -y/v
            elif f != 0 and v == 0:
                return sqrt(-2*y*m/f)
            elif v**2-(2*f*y)/m < 0:
                return -1
            else:
                temp = sqrt(v**2-(2*f*y)/m)
                a = (-v+temp)/(f/m)
                b = (-v-temp)/(f/m)
                return max(a,b)
        except: 
            print("-"*10)
            print(y,v,f)
            print("-"*10)
            0/0#kaatuisi muutenkin tässä vaiheessa, haluan vain enemmän infoa
    
    def _sfMv(self,sftime,f):
        self.speed[0] += (f[0]*sftime)/self.mass
        self.speed[1] += (f[1]*sftime)/self.mass
        self.pos[0] += self.speed[0]*sftime
        self.pos[1] += self.speed[1]*sftime
        if self.pos[1] <0:
            self.pos[1] = 0
        
    def move(self,time):
        self._grav()
        f = summa(self.forces)
        #print(f)
        self.forces = []
        osumaAika = self._osu(f[1])
        #print(osumaAika)
        #print(round(self.pos[0],2),round(self.pos[1],2),"   ",round(f[0],2),round(f[1],2)," ",round(self.speed[0],2),round(self.speed[1],2),"   ",round(osumaAika,2))
        if osumaAika > time or osumaAika < 0: # ei osu maahan tässä stepissä tai liikkuu ylös
            self._sfMv(time,f)
        elif osumaAika < time:
            self._sfMv(osumaAika,f) # pos = (x,0)
            
            self.speed[1] = 0 # pysähtyy maahan osumisesta
            f = self._kitka(f,time-osumaAika)
            self._sfMv(time-osumaAika,f)
    def paikka(self):
        return int(self.pos[0]),int(self.pos[1])
    

            
            
        
def main():
    """addForce() applyForce() move() resetForce()"""
    a = esine(1)
    b = esine(1)
    a.pos = [1,1]
    push(a,b,1)
    for i in range(100):
        a.move(0.1)
if __name__ == "__main__":
    main()
