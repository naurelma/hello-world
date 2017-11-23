import NodeMap

a = NodeMap.NodeMap()


def init():
    jatkuu = True
    while jatkuu:
        x = input("X:")
        y = input("Y:")
        x = int(x)
        y = int(y)
        a.addNode((x,y))
        if input("J:")!= "y":
            jatkuu = False
            yhdistä()


def test():
    lista = [(0, 0), (0, 1), (0, 2),
                     (1, 1), (1, 2), (1, 3),
                     (2, 1), (2, 2), (2, 3), 
             (3, 0),         (3, 2), (3, 5),
                                     (4, 5), (4, 6)]
    for i in lista:
        a.addNode(i)
    yhdistä()


    
def yhdistä():
    prev = (-100,-100)
    d = sorted(a.nodes.keys())
    for i in d:
        if prev[0] == i[0]:
            a.addNaapuri(prev,i)
        for j in range(i[0]-1,-1,-1):
            if (j,i[1]) in d:
                a.addNaapuri((j,i[1]),i)
                break
        prev = i
            
