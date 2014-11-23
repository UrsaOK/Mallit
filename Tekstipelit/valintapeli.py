PORKKANAT = 0
ISOT_PORKKANAT = 1
inventory = []

def valinta(dikti):
	aakkoset = "abcdefghijklmn"
	reaktiot = {}
	kuvaus = ""
	for i, teksti in enumerate(dikti):
		kuvaus += aakkoset[i]+") "+teksti+"\n"
		reaktiot[aakkoset[i]] = dikti[teksti]

	while True:
		kirjoitettu = input(kuvaus)
		for i in reaktiot:
			if kirjoitettu.strip().lower() == i:
				reaktiot[i]()
				return
		else:
			print("Tuo ei ole yksikään vaihtoehdoista")

porkkanatLattialla = True
def alkuhuone():
	print("Olet alasti huoneessa.")
	vaihtoehdot = {"Itke.": itke, "Mene ulos.": ulos}

	if porkkanatLattialla:
		print("Lattialla on röykkiö porkkanoita.")
		vaihtoehdot["Ota porkkanat!"] = get_carrots

	valinta(vaihtoehdot)

def itke():
	print("Yhyy...")
	alkuhuone()

def get_carrots():
	global porkkanatLattialla
	porkkanatLattialla = False
	inventory.append(PORKKANAT)

	print("Porkkanat katoavat mystisesti invetaarioosi.")
	alkuhuone()

def ulos():
	print("Eihän täällä edes ole ovea!")
	print("BZZZZZ...")
	talon_edessä()

def talon_edessä():
	print("Seisot talosi edessä. Siinä ei ole ovea. Kaukana näkyy pelto. Toisaalla kaupunki.")
	valinta({"Mene pellolle.":pelto, "Mene kaupunkiin": kaupunki, "Lopeta tämä typerä peli":list})

"""
Peltokoodia!
"""
kylvetty = False
lannoitettu = False
def pelto():
	vaihtoehdot = {"Palaa talosi eteen.": talon_edessä}
	if kylvetty:
		print("Pellolla kasvaa porkkanoita.")
		if lannoitettu:
			print("Porkkanoilla on suuret lehdet.")
			seuraus = saa_isot_porkkanat
		else:
			seuraus = porkkanat_takaisin
		vaihtoehdot["Vedä porkkanat maasta."] = seuraus

	else:
		print("Edessäsi on tyhjä pelto.")
		if PORKKANAT in inventory:
			vaihtoehdot["Kylvä peltoon porkkanasi"] = kylvä
		if lannoitettu:
			print("Se haisee pahalta.")

	if not lannoitettu:
		vaihtoehdot["Pasko pellolle."] = lannoita

	valinta(vaihtoehdot)

def kylvä():
	print("OK.")
	global kylvetty
	kylvetty = True
	inventory.remove(PORKKANAT)
	pelto()

def lannoita():
	global lannoitettu
	lannoitettu = True
	print("Ok.")
	pelto()

def saa_isot_porkkanat():
	print("Porkkanat ovat nyt paljon suurempia!")
	global kylvetty
	kylvetty = False
	inventory.append(ISOT_PORKKANAT)
	pelto()

def porkkanat_takaisin():
	print("Otit porkkanat takaisin pellosta.")
	global kylvetty
	kylvetty = False
	inventory.append(PORKKANAT)
	pelto()

"""
Kaupunkikoodia!
"""
def kaupunki():
	print("Kaupunkia ei ole vielä luotu, mutta sen paikalla on kauhea hirviö")
	print("""
 \ /
  o
_____
\\vvv/
 ^^^
""")
	valinta({"Mene takaisin talosi eteen": talon_edessä, "Taistele hirviön kanssa": taistelu})

def taistelu():
	print("STRIFE!!!")
	if PORKKANAT in inventory:
		print("Häviät hirviölle ja kuolet.")
		input()
	elif ISOT_PORKKANAT in inventory:
		print("Iso porkkana putoaa hirviön varpaille ja se putoaa puuttuvan kaupungin jättämään kuiluuun.")
		print("VOITIT!")
		input()
	else:
		print("Ilman porkkanaa et voi haastaa hirviötä. Sehän olisi aivan sopimatonta.")
		kaupunki()


alkuhuone()