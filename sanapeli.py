#!/usr/bin/env python

import sys

class Sana(object):
	def __init__(self, teksti, indeksi, linkit):
		self.teksti = teksti
		self.indeksi = indeksi
		self.linkit = linkit
		self.piilossa = True

	def arvaa(self, arvaus):
		if arvaus == self.teksti:
			self.piilossa = False

	def __repr__(self):
		return "%s: #%s, %d links"%(self.teksti, self.indeksi, len(self.linkit))

def tulostaTilanne(sana, taso, ei=[]):
	if sana in ei:
		return
	ei.append(sana)
	sisennys = taso * " "
	if sana.piilossa:
		print "%s%s (%d)"%(sisennys, len(sana.teksti)*'*', len(sana.teksti))
	else:
		#ekaks teksti:
		print sisennys + sana.teksti + ":"
		for x in sana.linkit:
			tulostaTilanne(x, taso + 2, ei)

class Sanapeli:
	def __init__(self, sanat):
		self.sanat = sanat
		self.loydetyt = []
		self._prosessoi()
		self.sanat[0].piilossa = False
		self.loydetyt.append(self.sanat[0])

	def _prosessoi(self):
		d = {}
		for sana in self.sanat:
			d[sana.indeksi] = sana
		for sana in self.sanat:
			linkit = []
			for i in sana.linkit:
				linkit.append(d[i])
			sana.linkit = linkit

	def tulosta_tilanne(self):
		print("Tilanne:")
		print("Tunnetut sanat: ")
		tulostaTilanne(self.loydetyt[0], 0, [])
		#for x in self.loydetyt:
		#	print("- " + x.teksti)

	def arvaa(self, arvaus):
		piilossa = []
		for x in self.loydetyt:
			for y in x.linkit:
				if y.piilossa == True and not y in piilossa:
					piilossa.append(y)
		if len(piilossa) == 0:
			print("Voitit!! kirjoita exit poistuaksesi.")
			return
		for x in piilossa:
			x.arvaa(arvaus)
			if not x.piilossa:
				self.loydetyt.append(x)
				print "Loytyi! jee!"
				return
		print "Ei!!"

	def __repl__(self):
		return "sanapeli"


#rivi olis:
#esim1:
#1,2,majava
#ylla sanan indeksi on 1, silla on linkki sanaan 2, sana on majava
#esim2:
#1,2,3,4,majava
#...
def lue_peli(tiedostonimi):
	tiedosto = file(tiedostonimi, 'r')
	sanat = []
	for rivi in tiedosto.readlines():
		r = rivi.strip()
		kentat = r.split(',')
		ind = kentat[0]
		linkit = kentat[1:-1] #voi olla tyhja
		teksti = kentat[-1]
		sanat.append(Sana(teksti, ind, linkit))
	tiedosto.close()
	return sanat

def main(args):
	peli = Sanapeli(lue_peli(args[1]))
	while True:
		peli.tulosta_tilanne()
		arvaus = sys.stdin.readline().strip()
		if arvaus == "exit":
			break
		peli.arvaa(arvaus)

if __name__=='__main__':
	main(sys.argv)
