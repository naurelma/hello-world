kenttä = []

def tul(kenttä):
    
    for i in kenttä:
        print(i)


def luo_kenttä_tyhjä():
    kenttä = None
    kenttä = [[0 for j in range(8)] for i in range(8)]
    return kenttä


def luo_kenttä():
    kenttä = None
    kenttä = [[0 for j in range(8)] for i in range(8)]
    
    for i,v in enumerate(kenttä[:]):
        for j in range(8):
            if((i+1)<len(kenttä)//2):
                if(i%2==j%2):
                    kenttä[i][j] = 8
            elif(i>len(kenttä)/2):
                if(i%2==j%2):
                    kenttä[i][j] = 3
		
    
    return kenttä

def vuoro(kenttä,kenen=8):
    a = input("siirrettävä:")
    l = input("kohde:")
    a = a.split(sep=",")
    l = l.split(sep=",")
    c = a+l
    for i,v in enumerate(c[:]):
        c[i]=int(v)
  
