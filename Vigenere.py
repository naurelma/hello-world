aakkoset = [chr(i) for i in range(ord("A"),ord("Z")+1)]
aakkoset.extend(["Å","Ä","Ö"])

def swap(i,lista):
	return lista[i:] + lista[:i]

neliö = []
for i in range(len(aakkoset)):
	neliö.append(swap(i,aakkoset))

def vigenere(koodi,avain,lähtö, salaa = True):
	def avaa(d,char):
		return aakkoset[neliö[d].index(char)]

	def sulje(d,char):
		return neliö[d][aakkoset.index(char)]

	if salaa:
		f = sulje
	else:
		f = avaa

	le = len(avain)
	idx = aakkoset.index(lähtö.upper())
	key =  swap(idx,aakkoset)
	koodi = koodi.upper()
	avain = avain.upper()
	purettu = []
	valit = []
	code = []
	for i,v in enumerate(koodi):
		if v not in aakkoset:
			valit.append((i,v))
		else:
			code.append(v)

	for i , char in enumerate(code):
		a = avain[i%le]
		d = key.index(a)
		purettu.append(f(d,char))
	
	for i in valit:
		purettu.insert(i[0],i[1])
	
	return "".join(purettu)


viesti = "MIKÄ ON PARAS SALAKIRJOITUS MENETELMä"
sv = "TYZF BÖ WQDHF EHÄPRYDQBXÅHE TUÖLGTSÖN"
print(vigenere(sv,"LUT","E",False))
print(vigenere(viesti,"LUT","E"))
print(vigenere(vigenere(viesti,"LUT","E"),"LUT","E",False))