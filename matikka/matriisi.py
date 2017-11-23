def ide(dim):
    m=Matrix(dim,dim)
    for i in range(dim):
        m.set(i,i,1)
    return m
def dot(u,v):
    if len(u)==len(v):
        summa = 0
        for a,b in zip(u,v):
            summa += a*b
        return summa
    else:
        raise ValueError
def luo(row,col):
    m = Matrix(row,col)
    for i in range(row):
        for j in range(col):
            m.set(i,j,int(input("{},{}: ".format(i,j))))
    return m
def _div(arr,num):
    tul = []
    for i in arr:
        tul.append(i/num)
    return tul

def _sum(arr1,arr2):
    tul = []
    for i,j in zip(arr1,arr2):
        tul.append(i+j)
    return tul
def _mul(arr,num):
    tul = []
    for i in arr:
        tul.append(i*num)
    return tul

def rref(mat):
     


def det(mat,k=0):
    if mat.row != mat.col:
        raise ValueError("ei neliö")
    elif mat.row == 1:
        return mat.solut[0][0]
    summa = 0
    for i,v in enumerate(mat.solut):
        kerroin = ((-1)**(i)) * v[0]
        if kerroin == 0:
            continue
        temp = det(mat.remove(i,0),k+1)
        summa += kerroin * temp
    return summa

class Matrix:
    def __init__(self,row, col, val = 0):
        self.solut = [[val for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col
        self.dim = (row,col)

    def set(self,row,col,arvo):
        self.solut[row][col] = arvo
        
    def setAll(self,solut,row,col):
        self.solut = solut
        self.row = row
        self.col = col
        self.dim = row,col

    def getRow(self,index):
        r = []
        for i in range(self.col):
            r.append(self.solut[i][index])
        return r
    def getCol(self,index):
        return self.solut[index]

    def transpose(self):
        m = Matrix(self.col,self.row)
        for i in range(self.row):
            for j in range(self.col):
                m.set(j,i,self.solut[i][j])
        return m
    def remove(self,row,col):
        m = self.copy()
        m.solut.pop(row)
        for i in range(len(m.solut)):
            m.solut[i].pop(col)
        m.row -=1
        m.col -=1
        m.dim = m.row,m.col
        return m
    def tulosta(self):
        for i in self.solut:
            for j in i:
                print(j,end=" ")
            print()
    def __repr__(self):
        return "Matrix({},{})".format(self.row,self.col)

    def __str__(self):
        self.tulosta()
        return ""
    def __radd__(self,other):
        return self + other
    
    def __rmul__(self,other):
        if type(other)==type(1):
            self.__mul__(other)

    def __mul__(self,other):
        if type(other) == type(1):
            m = Matrix(1,1)
            m.setAll(self.solut,self.row,self.col)
            for i in range(self.row):
                for j in range(self.col):
                    m.solut[i][j] *= other
            return m
        elif type(self)==type(other):
            if self.col == other.row:
                m = Matrix(self.row,other.col)
                for i in range(m.row):
                    for j in range(m.col):
                        m.set(i,j,dot(self.getRow(i),other.getCol(j)))
                return m
            else:
                raise NotImplemented
        
    def __add__(self,other):
        if type(self) == type(other):
            if(self.dim == other.dim):
                m = Matrix(self.row,self.col)
                for i in range(self.row):
                    for j in range(self.col):
                        m.set(i,j,self.solut[i][j]+other.solut[i][j])
                return m
            else:
                raise NotImplemented
        elif type(other) == type(1):
            m = ide(self.row,self.col)
            return  self + m * other

    def copy(self):
        m = Matrix(self.row,self.col)
        for i in range(self.row):
            for j in range(self.col):
                m.set(i,j,self.solut[i][j])
        return m
