class Bullet:
    def __init__(self, x, y, sprite, speed, damage):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed = speed
        self.damage = damage
        self.hitbox = None

    def move(self, x, y):
        pass
