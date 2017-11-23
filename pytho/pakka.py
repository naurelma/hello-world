from random import random

class deck:
    """
perus 52 korttia, kortit numeroita, kortin numero % 12 = maa
    """
    maat = 0
    korttia = 0
    pakka = []
    
    def __init__(self, maidenLKM = 4, korttiaPerMaa = 13):
        self.maat = maidenLKM
        self.korttia = korttiaPerMaa
        self.pakka = list(range(maidenLKM*korttiaPerMaa))
        self.suffleT()

    def show(self):
        for i in self.pakka:
            print("(",i%self.maat,",",i//self.maat,")",sep="",end="")
        print()
        
    
    def suffleT(self, toistot = 10):
        #pakka puoliksi (len()/4+int(rand()*len()/2)))) vuorotellen kummastakin puolikkaasta
        #(rand<0.5)
        puol = len(self.pakka)//2
        for å in range(toistot):
            tempA = self.pakka[:puol]
            tempB = self.pakka[puol:]
            if random()<0.5:
                tempA,tempB = tempB,tempA
            for i in range(0,len(self.pakka),2):
                self.pakka[i] = tempB.pop()
                self.pakka[i+1] = tempA.pop()
            self.pakka += tempB
            
