from time import time

class clicer:
    pps = 1
    points = 0
    items = [{"lkm":0,"pps":1,"cost":10,"tax":1.09},
             {"lkm":0,"pps":10,"cost":100,"tax":1.10},
             {"lkm":0,"pps":100,"cost":1000,"tax":1.06},
             {"lkm":0,"pps":1000,"cost":10000,"tax":2.00}]
    ti = 0
    def __init__(self):
       self.ti = time()

    def inv(self):
        delta = time()-self.ti
        self.ti = time()
        self.points += delta*self.pps
        print("***","pps=",self.pps,"points=",self.points,"***")
        for i in self.items:
            print(i)

    def _osta(self,nimi):
        delta = time()-self.ti
        self.ti = time()
        self.points += delta* self.pps
        if self.items[nimi]["cost"]<=self.points:
            self.points -= self.items[nimi]["cost"]
            self.items[nimi]["lkm"] += 1
            self.items[nimi]["cost"] *= self.items[nimi]["tax"]
            self.pps += self.items[nimi]["pps"]
            return True
        else:
            return False
    
    def osta(self,nimi,lkm=1):
        self.inv()
        counter = 0
        while(self._osta(nimi)and counter<lkm):
            counter +=1
        self.inv()
        return counter
