"""
64 
64
64

"""
import numpy as np




class Taso():

	def __init__(self,numNode, prevNum):
		self.numNode = numNode
		self.prevNum = prevNum
		self.arvot = np.floor(5-10*np.random.random((numNode)))
		self.weights = np.floor(5-10*np.random.random((numNode,prevNum)))
		self.bias = np.floor(5-10*np.random.random((numNode)))

	def siirrä(self,prev):
		self.arvot = np.dot(prev.arvot,self.weights) + self.bias

	def aseta(self,idx,arvo):
		self.arvot[idx] = arvo

	def __str__(self):
		tulos = ["START",
		"{};{}".format(str(self.numNode),str(self.prevNum)),
		#str(self.arvot).replace("[","]").replace("]",""),
		"WEIGHT",
		str(self.weights).replace("[","]").replace("]",""),
		"BIAS",
		str(self.bias).replace("[","]").replace("]",""),
		"END"]
		return "\n".join(tulos)


class Network():

	def __init__(self, numA,numVälit,numL):
		self.numA = str(numA)
		self.numVälit = numVälit
		self.numL = str(numL)
		self.alku = Taso(numA,0)
		self.hidden = []
		viime = numA
		for i in numVälit:
			self.hidden.append(Taso(i,viime))
			viime = i
		self.loppu = Taso(numL,viime)

	def __str__(self):
		tulos = ["Network:",
		"{};{};{}".format(self.numA,str(self.numVälit),self.numL),
		str(self.alku),
		str(self.loppu)]
		for i in self.hidden:
			tulos.append(str(i))
		tulos.append("Network")
		return "\n".join(tulos)

	def dump(self,nimi):
		np.set_printoptions(threshold=float('inf'))
		with open(nimi,"w",encoding= "utf8") as f:
			f.write(str(self))
		np.set_printoptions(threshold=float(11))

	def vieEteen(self):
		viime = self.alku
		for i in range(len(self.hidden)):
			self.hidden[i].siirrä(viime)
			viime = self.hidden[i]
		self.loppu.siirrä(viime)

	def tulos(self):
		self.vieEteen()
		print(self.loppu.arvot.reshape((8,8)))

	def suurin(self):
		a = list(self.loppu.arvot)
		s = max(a)
		idx = a.index(s)
		self.loppu.arvot[idx] = float("-inf")
		return idx, s

	def asetaArvot(self,arr):
		if len(arr) != len(self.alku.arvot):
			raise ValueError("Ei sovi ")
		if type(arr) == type([]):
			self.alku.arvot = np.array(arr)
		else:
			self.alku.arvot = arr

def strToList(arr):
	tulos = []
	for i in arr.split(" "):
		if i == "":
			continue
		tulos.append(float(i))
	return tulos

def luo(nyk):

	arv = nyk[1].split(";")
	nyk  = nyk[2:-1]

	w = 0
	b = 0
	for i,v in enumerate(nyk):
		if v == "WEIGHT":
			w = i
		if v == "BIAS":
			b = i
			break
	arvot = nyk[:w][0]
	painot = nyk[w+1:b]
	bias = nyk[b+1:][0]
	t = strToList

	tulos = Taso(int(arv[0]),int(arv[1]))
	if len(arvot)>0:
		tulos.arvot = np.array(strToList(arvot))
	if len(painot)>0:
		tulos.weights = np.array([t(i) for i in painot])

	if len(bias)>0:
		tulos.bias = np.array(strToList(bias))
	return tulos


def rakennaTiedostosta(nimi):
	with open(nimi,encoding="utf8") as f:
		f.readline()
		arvot = f.readline().split(";")
		tulos = Network(int(arvot[0]),int(arvot[1]),int(arvot[2]))
		tasot = []
		nyk = []
		for line in f:
			line = line[:-1]
			nyk.append(line)
			if line == "END":
				tasot.append(luo(nyk))
				nyk = []
		tulos.alku = tasot[0]
		tulos.loppu = tasot[1]
		tulos.hidden = tasot[2:]
		return tulos 

def listaa(verkko):
	tulos = []
	selite = []
	for i in verkko.hidden:
		tulos.extend(i.weights.flat)
		selite.append(i.weights.shape)
		tulos.extend(i.bias.flat)
		selite.append(i.bias.shape)
	tulos.extend(verkko.loppu.weights.flat)
	selite.append(verkko.loppu.weights.shape)
	tulos.extend(verkko.loppu.bias.flat)
	selite.append(verkko.loppu.bias.shape)

	return tulos, selite


def rakennaListasta(lista, selite):
	pass
