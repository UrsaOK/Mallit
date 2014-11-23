import sfml
from sfml_helpers import *
from collision import *

class Seinä(Sprite, Colliding):
    pass

class Sankari(Sprite, Colliding):
    yspeed = 0
    on_ground = False

    def update(self):
        self.lastpos = self.position

        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.A):
            self.move((-1, 0))
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.D):
            self.move((1, 0))
        if sfml.Keyboard.is_key_pressed(sfml.Keyboard.W) and self.on_ground:
            self.yspeed = -5

        if not self.on_ground:
            self.yspeed += 0.1

        self.move((0, self.yspeed))

        self.view.center = self.position

        self.on_ground = False

    def collision(self, other):
        if isinstance(other, Seinä):
            newpos = self.position
            # riittääkö se, että aionoastaan x tai y akselilla siirrytään
            # edelliseen sijaintiin?
            self.position = (self.lastpos.x, newpos.y)
            if self.collides_with(other):
                self.yspeed = 0
                self.on_ground = True
                self.position = (newpos.x, self.lastpos.y)
                if self.collides_with(other):
                    self.position = self.lastpos

    def collides_with(self, other):
        return intersects(self.global_bounds, other.global_bounds)

def testlevel(peli):
    peli.uusiSeina(70, 130)

    for i in range(10):
        peli.uusiSeina(i*250, 300)

    s = Sankari(sfml.Texture.from_file("tile.png"))
    s.position = i*150, 0
    s.view = game.window.view
    game.sprites.add(s)
    game.collider.append(s)

    s = Sprite(sfml.Texture.from_file("tile.png"))
    s.depth = -100
    s.position = (300, 50)
    game.sprites.add(s)


class Game:
    def __init__(self):
        self.window = sfml.RenderWindow(sfml.VideoMode(1280, 960), "test")
        self.clock = sfml.system.Clock()

        self.sprites = OrderedSpritesUpdater()
        self.collider = CollisionSystem()

    def run(self):
        self.clock.restart()

        while self.window.is_open:

            for event in self.window.events:
                if type(event) is sfml.CloseEvent:
                    self.window.close()

            self.sprites.update()
            self.collider.find_collisions()

            self.window.clear()
            self.sprites.draw(self.window)
            self.window.display()

            while self.clock.elapsed_time.seconds < 1 / 60:
                pass
            self.clock.restart()

    def uusiSeina(self, x, y):
        s = Seinä(sfml.Texture.from_file("tile.png"))
        s.position = (x, y)
        game.sprites.add(s)
        game.collider.append(s)
        return s

game = Game()
testlevel(game)
game.run()
