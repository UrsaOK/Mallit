from turtle import *
from math import *
import time

def spiral():
	for i in range(110):
		left(5)
		forward(i/5)

def plot(f):
	penup()
	for i in range(-30, 30):
		goto(i, f(i))
		pendown()

def line(x1, y1, x2, y2):
	penup()
	goto(x1, y1)
	pendown()
	goto(x2, y2)

def katko(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1

	factor = 1 / sqrt(dx**2 + dy**2) * 20
	dx *= factor
	dy *= factor

	x = x1
	y = y1

	penup()
	goto(x1, y1)

	while (x < x2) == (x1 < x2) and (y < y2) == (y1 < y2):
		pendown()
		goto(x, y)
		x += dx
		y += dy

		penup()
		goto(x, y)
		x += dx
		y += dy

	goto(x2, y2)

def project(x, y, z):
	z += 4
	return x / z * 500, y / z * 500

def rotate(x, y, angle):
	return x * sin(angle) - y * cos(angle), x * cos(angle) + y * sin(angle)

cube_data = [
	(-1, -1, -1, 1, -1, -1),
	(1, -1, -1, 1, -1, 1),
	(1, -1, 1, -1, -1, 1),
	(-1, -1, 1, -1, -1, -1),
	(-1, 1, -1, 1, 1, -1),
	(1, 1, -1, 1, 1, 1),
	(1, 1, 1, -1, 1, 1),
	(-1, 1, 1, -1, 1, -1),
	(-1, 1, 1, -1, -1, 1),
	(1, 1, 1, 1, -1, 1),
	(-1, 1, -1, -1, -1, -1),
	(1, 1, -1, 1, -1, -1),
]

def cube(FRAMES, startangle, da):

	for i in range(FRAMES):
		clear()
		angle = startangle + i / FRAMES * da
		for x1, y1, z1, x2, y2, z2 in cube_data:

			x1, z1 = rotate(x1, z1, angle)
			x2, z2 = rotate(x2, z2, angle)

			if z1 > 0.8 or z2 > 0.7:
				fun = katko
			else:
				fun = line

			fun(*project(x1, y1, z1) + project(x2, y2, z2))

		time.sleep(1/30)


def wobble(frames, angle):

	for i in range(frames):
	
		mul = (frames - i) / frames

		xtran = 0.5 + 0.25 * (1 - mul)

		wobbren(1, 1, xtran, angle)

	half = int(frames/2)
	for i in range(half):
	
		mul = (half - i) / half

		xtran = 0.5 + 0.25 * mul

		wobbren(1, 1, xtran, angle)

	for i in range(frames):
	
		mul = (frames - i) / frames

		xmul = 0.5 + 0.5 * mul
		yzmul = sqrt(1/xmul)
		xtran = 0.25 + 0.25 * mul

		wobbren(xmul, yzmul, xtran, angle)

	speed = 0

	for _ in range(200):
		speed += -i / 100
		i += speed
		speed *= 0.97

		mul = (frames - i) / frames

		xmul = 0.5 + 0.5 * mul
		yzmul = sqrt(1/xmul)
		xtran = 0.25 + 0.25 * mul

		wobbren(xmul, yzmul, xtran, angle)

def wobbren(xmul, yzmul, xtran, angle):
	clear()

	part1 = []
	for x1, y1, z1, x2, y2, z2 in cube_data:
		part1.append((x1 / 2 * xmul - xtran, y1 * yzmul, z1 * yzmul, x2 / 2 * xmul - xtran, y2 * yzmul, z2 * yzmul))

	part2 = []
	for x1, y1, z1, x2, y2, z2 in cube_data:
		part2.append((x1 / 2 * xmul + xtran, y1 * yzmul, z1 * yzmul, x2 / 2 * xmul + xtran, y2 * yzmul, z2 * yzmul))

	for x1, y1, z1, x2, y2, z2 in part1 + part2:

		x1, z1 = rotate(x1, z1, angle)
		x2, z2 = rotate(x2, z2, angle)

		line(*project(x1, y1, z1) + project(x2, y2, z2))

	time.sleep(1/30)


def compilation():
	cube(3, 0, 1)

	speed(0)
	hideturtle()
	cube(5, 1, 2.5)

	delay(1)
	cube(5, 3.5, 0.5)

	delay(0)
	cube(100, 4, pi)

	wobble(30, 4+pi)


class vec3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __mul__(self, other):
		return vec3(self.x * other, self.y * other, self.z * other)

	def __add__(self, other):
		return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

	def length(self):
		return sqrt(self.x**2 + self.y**2 + self.z**2)


class RigidBody:

	def __init__(self, pos, mass):
		self.invmass = 1 / mass

		self.position = pos

		self.speed = vec3(0, 0, 0)

		self.force = vec3(0, 0, 0)

	def act(self, dt):
		acceleration = self.force * self.invmass
		self.force = vec3(0, 0, 0)

		self.speed += acceleration * dt
		self.position += self.speed * dt

def make_soft_cube():
	a = RigidBody(vec3(-1, -1, -1.2), 1)
	b = RigidBody(vec3(1, -1, -1), 1)
	c = RigidBody(vec3(1, -1.3, 1), 1)
	d = RigidBody(vec3(-1, -1, 1), 1)
	e = RigidBody(vec3(-1, 1, -1), 1)
	f = RigidBody(vec3(1, 1, -1), 1)
	g = RigidBody(vec3(1, 1, 1), 1)
	h = RigidBody(vec3(-1, 1, 1), 1)

	connections = [
	(a, b), (b, c), (c, d), (d, a),
	(e, f), (f, g), (g, h), (h, e),
	(e, a), (f, b), (g, c), (h, d)]

	return [a, b, c, d, e, f, g, h], connections


def softbody(frames):
	nodes, connections = make_soft_cube()

	l = 2
	k = 1

	dt = 0.1

	while True:
		clear()

		for a, b in connections:
			pa = a.position
			pb = b.position

			# F = -kx
			d = pb - pa
			x = d * (l - d.length())
			a.force += x * -k
			b.force += x * k

			# "kitka"
			dv = b.speed - a.speed
			a.speed += dv * 0.1 * dt
			b.speed -= dv * 0.1 * dt

			# lattia
			if a.position.y < -1.5:
				b.position.y = -1.5
				if a.force.y < 0:
					a.force.y = 0
				if a.speed.y < 0:
					a.speed.y = 0

			if b.position.y < -1.5:
				b.position.y = -1.5
				if b.force.y < 0:
					b.force.y = 0
				if b.speed.y < 0:
					b.speed.y = 0

			line(*project(pa.x, pa.y, pa.z) + project(pb.x, pb.y, pb.z))

		for i in nodes:
			# gravitaatio
			i.force += vec3(0, -0.1, 0)

			i.act(dt)

		time.sleep(1/30)

speed(0)
delay(0)
hideturtle()

softbody(100)

done()