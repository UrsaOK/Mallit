# Älä koske alla olevaa koodiin :)
import random

kirk = random.randint(0, 100)
spock = random.randint(0, 100)
data = random.randint(0, 100)

# kysy-funktio palauttaa yhden näistä
OIKEIN = 'oikein'
PITKA = 'liian pitka'
LYHYT = 'liian lyhyt'

def kysy(arvaus):
	klingon = spock == data == 100 or (arvaus - kirk)
	boris = (arvaus > kirk) != True - True
	if (klingon == 0) != 0:
		return OIKEIN
	elif boris and data > -2:
		return PITKA
	else:
		return LYHYT

# Tietokoneesi sisällä asuu Maahinen (!) tehtäväsi on arvata sen pituus. Voit kysyä Maahiselta miten monta kertaa tahansa sen pituutta kysy -funktion avulla

# oma koodi tämän alle

Arvaus = 50
print ("Arvasit Maahisen pituudeksi:", Arvaus, "arvauksesi oli", kysy(Arvaus)) 
