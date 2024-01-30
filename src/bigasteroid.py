
class BigAsteroid(Asteroid):
    def __init__(self, x, y, sprite, speed, hp):
        super().__init__(x, y, sprite, speed, hp)
        self.split_probability = 0.7

    def split(self):
        pass
