for i in x:
	pass

while ehto:
	pass

for i in x:
	if i == "a":
		break
else:
	# tähän tullaan jos x ei sisältänyt a:ta
	print("ei a:ta")

# saman voi kirjoittaa myös:
if a not in x:
	print("ei a:ta")

# tulostaa kaiken paitsi pienet kirjaimet
for i in "AArghKDJ!":
	if i.islower():
		continue
	print(i)

# ikuinen silmukka
while True:
	pass

# toinen ikuinen silmukka
a = [1]
for i in a:
	a.append(i)

"""
Tehtävä:
Kirjoita ohjelma, joka tulostaa fibonaccin lukujonoa kunnes sen pysäyttää
"""

a = 1
b = 1

while True:
	print(b)
	a, b = b, a + b
	#time.sleep(0.1)

"""
Tehtävä:
Kirjoita ohjelma, jonka kanssa voi pelata hirsipuuta.
"""

