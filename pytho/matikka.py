import math

def is_prime(x):
    if x%2==0:
        return False
    for i in range(3,1+int(x//2),2):
        if x%i == 0:
            return False
    return True

def next_prime(x):
    i = x +1
    while not is_prime(i):
        i +=1
    return i

def prime_gen(alku, loppu):
    i = 0
    while i < loppu:
        alku = next_prime(alku)
        i += 1
        yield alku
        
def factor(x):
    if x%2==0:
        return [2,x//2]
    for i in range(3,1+int(x//2),2):
        if x%i==0:
            return [i,x//i]
    return [1,x]

def tulo(x):
    a = 1
    for i in x:
        a*=i
    return a
	
def prime_factor(x):
    tekijät = []
    tulos = 1
    luku = x
    while x%2==0:
        tekijät.append(2)
        x = x//2
        tulos *= 2
    for i in range(3,x+1,2):
        while x%i==0:
            tekijät.append(i)
            x = x//i
            tulos *= i
            if tulos == luku and tulo(tekijät)==luku:
                return tekijät
    return tekijät

def syt(x,y):

	if x<y:
		x,y = y,x
		
	if y == 0:
		return y
		
	elif x%y == 0:
		return y
	
	elif x%y != 0:
		return syt(y,x%y)

def pyj(x,y):
	return x*y//syt(x,y)
	
def hypot(x,y):
	return math.hypot(x,y)
	
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

class vector():
    x = 0.0
    y = 0.0
    z = 0.0

    def setvalues(s,a=0.0,b=0.0,c=0.0):
        s.x = a
        s.y = b
        s.z = c
    
    def dot(s,v):
        return s.x*v.x + s.y*v.y + s.z*v.z

    def length(s):
        return math.sqrt(s.dot(s))

    def add(s,v):
        s.x += v.x
        s.y += v.y
        s.z += v.z
    
    def väh(s,v):
        s.x -= v.x
        s.y -= v.y
        s.z -= v.z
    
    def skal(s,k):
        s.x *= k
        s.y *= k
        s.z *= k
    
    def cross(s,v):
        u = vector()
        a = s.y*v.z - s.z*v.y
        b = v.x*s.z - v.z*s.x
        c = s.x*v.y - v.x*s.y
        u.setvalues(a,b,c)
        return u

    def kulma(s,v):
        return math.acos(s.dot(v)/(s.length()*v.length()))
    
    def norm(s):
        s.skal(1/s.length())

    def copy(s):
        v = vector()
        v.setvalues(s.x,s.y,s.z)
        return v

    def values(s):
        return [s.x,s.y,s.z]
