from sfml_helpers import ThingList

def intersects(r1, r2):
    return not (r2.left > r1.right or r2.right < r1.left or
                r2.top > r1.bottom or r2.bottom < r1.top)

class CollisionSystem(ThingList):
    def find_collisions(self):
        """
        Äärimmäisen tehoton tapa löytää kaikki
        törmäykset.
        """
        self.remove_dead()

        for i, sprite1 in enumerate(self):
            for sprite2 in self[:i]:
                if intersects(sprite1.global_bounds, sprite2.global_bounds):
                    sprite1.collision(sprite2)
                    sprite2.collision(sprite1)

class Colliding:
    def collision(self, other):
        pass