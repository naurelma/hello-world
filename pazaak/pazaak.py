from random import random
deck = [[],[]]
handDeck = [[1,2,3,4],[1,2,3,4]]
jatkaa = [True,True]
vuoro  = 0
def deal(player):
	global deck
	global jatkaa
	deck[player].append(int(random()*10))
	if sum(deck[player]) >20:
		print(player,"lost")
		jatkaa[player] = False
		
if __name__ == "__main__":
	player = 0
	while jatkaa[0] or jatkaa[1]:
		if not jatkaa[player]:
			continue
		deal(player)
		print(deck)
		print("summa = {} ja summa = {}".format(sum(deck[0]),sum(deck[1])))
		print(handDeck)
		a = input("{} anna hand decin kortin paikka tai anna 's' jos haluat lopettaa tämän setin tai anna 'p' for pass: ".format(player))
		try:
			b = int(a)
			deck[player].append(handDeck[player].pop(a))
		except:
			if a == "s":
				jatkaa[player] = False
		if player == 0:
			player = 1
		else:
			player = 0
		
