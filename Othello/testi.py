import network
import othello



net = network.Network(64,[64],64)

#a,b = network.listaa(net)
net.asetaArvot([0 for i in range(64)])
#net.tulos()

arvo1 = []
arvo2 = []
lailliset = [0,0]
def esitä(lauta):
	global arvo1
	global arvo2

	arvo1 = [lauta[(i//8,i%8)] for i in range(64)]
	lailliset[0] = 
	lauta.flipAll()
	arvo2 = [lauta[(i//8,i%8)] for i in range(64)]
	lauta.flipAll()

c1 = 0
def siirto1():
	global c1
	global c2
	c2 = 0
	c1+=1
	net.asetaArvot(arvo1)
	net.vieEteen()
	assert c1 < 65
	for i in range(c1):
		p = net.suurin()[0]
	if c1 == 64:
		print(net.loppu.arvot)
	return  (p//8,p%8)

c2 = 0
def siirto2():
	global c1
	global c2
	c1 = 0
	c2 +=1
	net.asetaArvot(arvo2)
	net.vieEteen()

	assert c2 < 65
	for i in range(c2):
		p = net.suurin()[0]
	if c2 == 64:
		print(net.loppu.arvot)
	return  (p//8,p%8)

c = 0
def out(s):
	return 
	global c
	c += 1
	if c % 10 == 1:
		print(s)
print(othello.pelaa(siirto1,siirto2,esitä,out))