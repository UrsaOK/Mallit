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
	
def spiral():
	for i in range(110):
		left(5)
		forward(i/5)