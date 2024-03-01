
class Asteroid:
    def __init__(self, x, y, sprite, speed, hp):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed = speed
        self.hp = hp
        self.hitbox = None



    def move(self, x, y):
        pass


class BigAsteroid(Asteroid):
    def __init__(self, x, y, sprite, speed, hp):
        super().__init__(x, y, sprite, speed, hp)
        self.split_probability = 0.7

    def split(self):
        pass



class SmallAsteroid(Asteroid):
    def __init__(self, x, y, sprite, speed, hp):
        super().__init__(x, y, sprite, speed, hp)
