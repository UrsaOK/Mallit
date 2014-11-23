from turtle import *
from math import *

import time


class Pallo(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def draw(self):
		penup()
		goto(self.x, self.y)
		pendown()
		circle(30)

class Pomppiva(Pallo):
	def __init__(self, x, y, speedx=0, speedy=0):
		super(Pomppiva, self).__init__(x, y)
		self.speedx = speedx
		self.speedy = speedy

	def update(self):
		# pomppu
		if self.y < 0:
			self.y = 0
			self.speedy *= -1
		# painovoima
		self.speedy -= 0.1
		# eulerintegraatio
		self.x += self.speedx
		self.y += self.speedy

class Liikkuva(Pallo):
	def update(self):
		self.x += 1

hideturtle()
speed(0)
delay(0)

pallot = []
pallot.append(Pomppiva(0, 100))
pallot.append(Liikkuva(50, 170))
pallot.append(Pomppiva(150, 300))

while True:
	clear()
	for p in pallot:
		p.update()
		p.draw()
	time.sleep(1/30.0)