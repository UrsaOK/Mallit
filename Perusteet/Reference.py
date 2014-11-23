"""
Kaikkein tavallisin syntaksi.
"""

pass # ei tee mitään

# funktion kutsuminen:
funktio(argumentti1, argumentti2, argumentti3)

# funktion määritteleminen:
def funktionNimi(argumentin1Nimi, argumentin2Nimi, argumentin3Nimi):
	# koodia
	return arvoJokaTuleeFunktiokutsunTilalle

# dataan osoittaminen:
a = 5
# Nyt a osoittaa luomaasi viitoseen.
# tämäkin on sallittua:
a, b = 3, a

w = list(range(3))
a, b, c = w

# merkkijono
merkkijono = "tekstiä"

# output
print(merkkijono)

# input
input()

# ehtolause
if ehto:
	pass
elif ehto: # * [0, ∞[
	pass
else: # * [0, 1]
	pass

# vertailuoperaattorit
# kaikesta mitä tässä lukee tulee True
0 < 2
2 > 0
2 == 2
1 != 0
a in [a, b, c]

# silmukat (elset voi jättää pois)

"""
Aina ennen silmukan sisällön ajamista
while katsoo onko ehto tosi. Jos se ei 
ole tosi, siirrytään elseen.
"""
while ehto:
	break # lopettaa silmukan ja hyppää elsen yli
	continue # hyppää silmukan sisällä olevan koodin loppuun
else:
	pass

# Aluksi for tekee näin:
y = iter(x)
# Aina ennen silmukan sisällön ajamista for tekee:
i = next(y)
# Jos tulee virhe nimeltä
StopIteration
# siirrytään elseen

# for siis käy läpi kaikki x:n arvot
for i in x:
	break # lopettaa silmukan ja hyppää elsen yli
	continue # hyppää silmukan sisällä olevan koodin loppuun
else:
	pass

# forin kanssa käteviä funktioita: (Testaa!)
range(100)
range(1, 100)
range(1, -100, -1)
enumerate(x)

"""
Lista ja Tuple
lista ja tuple ovat samanlaiset,
mutta tupleta ei voi muokata;
pitää luoda uusi.

Kummassakin voi olla mitä tahansa sisällä.
"""
# luominen
lista = [1, [8], ["adf", 3]]
tuplee = (1, 2, 3)

# yhdenpituinen tuplee kirjoitetaan
(a,)

# slicing
# kaikesta mitä tässä lukee tulee True
lista[0] == 1
tuplee[0] == 1

tuplee[:2] == (1, 2)
tuplee[2:] == (3,)
tuplee[-1] == 3
tuplee[1:2] ==(2,)

# listan perään voi lisätä jotain
lista.append(4)

# testaa myös:
lista.pop()

"""
Importtaus
"""

import turtle
from turtle import *