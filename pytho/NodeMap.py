import math
class NodeMap:
    class Node:
        coords = None
        naapurit={}
        #type = ""

        def __init__(s,coords):
            s.coords = coords
            s.naapurit = dict()

        def addNaapuri(s, coord):
            matka = math.hypot(s.coords[0]-coord[0],s.coords[1]-coord[1])
            if matka<50:
                s.naapurit[coord]= matka
            
        def poistaNaapuri(s,coord):
            del s.naapurit[coord]
            
#"""End Node"""
        
    nodes = {}

    def addNode(s,coords):
        s.nodes[coords]= NodeMap.Node(coords)

    def addNaapuri(s,alku,loppu):
        s.nodes[alku].addNaapuri(loppu)
        s.nodes[loppu].addNaapuri(alku)
        
    def show(s):
        for coord,node in s.nodes.items():
            print(coord,":",node.naapurit)




                
