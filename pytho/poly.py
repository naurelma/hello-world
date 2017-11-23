class polynomi:
    funktio = dir()

    def __init__(self):
        self.funktio = {0:0}

    def define(self, arg):
        self.funktio = arg

    def arvo(self,x):
        total = 0
        for k,v in self.funktio.items():
            total +=v*(x**k)
        return total

    def show(self):
        for k,v in reversed(sorted(self.funktio.items())):
            print("+",v,"*x^",k,sep = "",end = " ")
        print()
        
    def copy(self):
        r={}
        for k,v in self.funktio.items():
            r[k]=v
        return r
    
    def __add__(self, other):
        for k,v in other.funktio.items():
            if k in self.funktio:
                self.funktio[k]+=v
            else:
                self.funktio[k]=v

    def __sub__(self,other):
        for k,v in other.funktio.items():
            if k in self.funktio:
                self.funktio[k]-=v
            else:
                self.funktio[k]=-v
    def derivaatta(self):
        der = polynomi()
        funk = {}
        for k,v in self.funktio.items():
            funk[k-1]=v*k
        der.define(funk)
        return der
        



    
