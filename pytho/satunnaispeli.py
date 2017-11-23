import random

def risteys(lkm):
    return(int(random.random()*lkm))

    
def vuoro(kenttä):
    kerrat = 0
    while type(kenttä)!=int and kerrat <100:
        kenttä = kenttä[risteys(len(kenttä))]
        kerrat += 1
    return kenttä

ken = [[[1,2,3],[4,5,6],[7,8,9]], [10,11,12,[13,14,[15,16]]]]
