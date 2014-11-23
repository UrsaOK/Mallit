import sfml
import bisect


class Thing:
    alive = True

class Sprite(sfml.Sprite, Thing):
    """
    Sfmllän Sprite paitsi että sen voi laitella syvyyden mukaan
    """
    depth = 0

    def __lt__(self, other): 
        return self.depth < other.depth

    def update(self):
        pass

class ThingList(list):

    def remove_dead(self):
        copy = self[:]
        self.clear()
        for i in copy:
            if i.alive:
                self.append(i)

class Updater(ThingList):

    def update(self):
        self.remove_dead()

        for i in self:
            i.update()

class OrderedSprites(ThingList):
    """
    Spritejen piirtämiseen.
    Isoin depth piirretään viimeisenä.
    Toimii ainoastaan jos depth ei muutu.
    """
    def add(self, go): 
        bisect.insort(self, go)

    def draw(self, window):
        self.remove_dead()

        for i in self:
            window.draw(i)

class OrderedSpritesUpdater(OrderedSprites, Updater):
    pass
