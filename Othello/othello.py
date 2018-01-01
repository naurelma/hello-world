
"""
x 0 1 2 3 4 5 6 7
0 x x x x x x x x 
1 x x x x x x x x
2 x x x x x x x x
3 x x x W M x x x
4 x x x M W x x x
5 x x x x x x x x
6 x x x x x x x x
7 x x x x x x x x
"""

suunnat =  [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
class Lauta(dict):

	def __missing__(self, key):
		return 0
	
	def flip(self,pos):
		self[pos] *= -1

	def aseta(self,pos,väri, testi=False):
		if self[pos] != 0:
			return False
		kaikki = []
		for s in suunnat:
			käännettävät = []
			lisää = False

			for i in range(1,8):
				paikka = self[(s[0]*i+pos[0],pos[1]+s[1]*i)]
				if paikka == -1*väri:
					käännettävät.append((s[0]*i+pos[0],pos[1]+s[1]*i))
					continue
				elif paikka == 0:
					break
				elif paikka == väri:
					lisää = True
					break
			if lisää:
				kaikki.extend(käännettävät)

		if  len(kaikki) == 0:
			return False
		if not testi:
			self[pos] = väri
			for i in kaikki:
				self.flip(i)
		return True

	def  lailliset(self,väri):
		tulos = []
		for i in range(8):
			for j in range(8):
				if self.aseta((i,j),väri,True):
					tulos.append((i,j))
		return tulos

	def summa(self):
		tulos = 0
		for i in range(8):
			for j in range(8):
				tulos+= self[(i,j)]
		return tulos

	def flipAll(self):
		for i in range(8):
			for j in range(8):
				self[(i,j)] *= -1

def luo():
	lauta = Lauta()
	lauta[(3,3)] =  1
	lauta[(4,4)] =  1
	lauta[(3,4)] = -1
	lauta[(4,3)] = -1
	return lauta

def muuta(num):
	if num == 0:
		return "T"
	elif num == 1:
		return "W"
	elif num == -1:
		return "B"

def cmdTulosta(lauta):
	print("  0 1 2 3 4 5 6 7")
	for i in range(8):
		print(i,end = " ")
		for j in range(8):
			print(muuta(lauta[(j,i)]),end=" ")
		print()


def cmdSiirto():
	while True:
		try:
			x = int(input("Anna x [0,7]: "))
			y = int(input("Anna y [0,7]: "))
			return (x,y)
		except:
			pass


def pelaa(siirto1,siirto2,esitä,out):
	lauta =luo()
	vuoro = -1
	c = 0
	out("Alkaa")
	while True:
		if len(lauta.lailliset(vuoro)) == 0:
			out("Vuoro Vaihtui")
			vuoro *= -1
			c +=1
			if c>3:
				return lauta.summa()
		c = 0
		esitä(lauta)
		out("Vuoro(1 == W; -1 == B):{}".format(vuoro))
		if vuoro == -1:
			while not lauta.aseta(siirto1(),vuoro):
				out("Lisää lailliseen paikkaan")
		else:
			while not lauta.aseta(siirto2(),vuoro):
				out("Lisää lailliseen paikkaan")
		vuoro *= -1


if __name__ == "__main__":
	pelaa(cmdSiirto,cmdTulosta,print, t)