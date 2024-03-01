class Spaceship:
    def __init__(self, x, y, sprite, speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed = speed
        self.hitbox = None
        self.Weapon = None

    def move(self, x, y):
        pass

    def shoot(self):
        pass
