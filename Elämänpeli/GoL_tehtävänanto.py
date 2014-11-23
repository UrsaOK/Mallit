
def montako_naapuria(x, y, lauta):
	"""
	Paluttaa montako naapuria ruudulla (x, y) on
	"""
	pass

def uusi_tila(vanha_tila, naapurien_maara):
	"""
	Antaa ruudun, jonka tila on vanha_tila
	ja jonka naapurien maara on naapurien_maara
	seuraavan tilan
	"""
	pass

def seuraava_asema(lauta):
	"""
	Laskee seuraavan framen laudan edellisestä
	"""
	return uusi_lauta

import random

WIDTH = 20
HEIGHT = 20

lauta = [[0 for _ in range(WIDTH+2)] for _ in range(HEIGHT+2)]

for x in range(1, WIDTH+1):
	for y in range(1, HEIGHT+1):
		lauta[x][y] = random.randint(0, 1)

for _ in range(10):
	for i in lauta:
		print(i)
	print()
	lauta = seuraava_asema(lauta)