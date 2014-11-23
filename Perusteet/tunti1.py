
# funktion kutsuminen:
funktio(argumentti1, argumentti2, argumentti3)

# funktion määritteleminen:
def funktionNimi(argumentin1Nimi, argumentin2Nimi, argumentin3Nimi):
	# koodia
	return arvoJokaTuleeFunktiokutsunTilalle

# merkkijono
"tekstiä"

# output
print("sana", "toinen")

# input
input()

"""
Tehtävä:
Tee ohjelma, joka ottaa rivin käyttäjältä ja tulostaa sen.
"""

# dataan osoittaminen:
a = 5
# Nyt a osoittaa luomaasi viitoseen.

"""
Tehtävä:
Tee ohjelma, joka ottaa rivin käyttäjältä ja tulostaa sen kahdesti.
"""
# ehtolause
if ehto:
	pass
elif ehto: # * (0 ... ∞)
	pass
else: # * (0 tai 1)
	pass

# vertailuoperaattorit
0 < 2
2 > 0
2 == 2
1 != 0
a in [a, b, c]

# järjestetyt kokoelmat
lista = [1, [8], ["adf", 3]]
tuplee = (1, 2, 3)

lista[0] == 1
tuplee[0] == 1

lista.append(4)
lista[3] == 4

a, b, c == tuplee

import random
random.choice(lista) in lista

"""
Tehtävä:
Kirjoita ohjelma, joka kysyy satunnaisen kysymyksen ja kommentoi
vastausta kysymyksestä riippuen.
"""

import random

def oletko(iii):
	if iii in ("joo", "kyllä"):
		print("ok")
	elif iii == "en":
		print("täh")
	else:
		print("idiootti")

def lempiväri(sdk):
	print("En välitä.")

kysymykset = [["oletko?", oletko], ["lempiväri?", lempiväri]]

kysymys = random.choice(kysymykset)

kysymys[1](input(kysymys[0]))

"""
Tehtävä:
Kirjoita funktio, joka laskee minkä tahansa fibonaccin luvun
1, 1, 2, 3, 5, 8, 13...
               ^
3 + 5 -------->|
"""

def fibonacci(x):
	if x <= 0:
		return 1
	return fibonacci(x-1) + fibonacci(x-2)