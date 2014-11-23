import sfml as sf

GRAVITY = 0.4

class Moduuli:
	MAXFALL = 16
	def __init__(self,x,y):
		self.alus = sf.Texture.from_file("alus_ei_tuli.png")
		self.alus_palaa = sf.Texture.from_file("alus_tuli.png")
		self.sprite = sf.Sprite(self.alus)
		self.sprite.origin = (32,32)
		self.sprite.position = (x,y)
		self.vy = 0
	def update(self):
		if self.vy < self.MAXFALL:
			self.vy += GRAVITY
		self.sprite.move((0,self.vy))
		if self.sprite.position.y > 200:
			self.sprite.position = 320, 64

window = sf.RenderWindow(sf.VideoMode(640,480), "Luna Landing")

window.framerate_limit = 60

mod = Moduuli(320,64)

while window.is_open:

    for event in window.events:

        if type(event) is sf.CloseEvent:
                window.close()

        mod.update()
       	window.clear()
       	window.draw(mod.sprite)
        window.display()