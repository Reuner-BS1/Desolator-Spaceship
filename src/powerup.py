class Powerup:
    def __init__(self, x, y, sprite, speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed = speed
        self.hitbox = None

    def move(self, x, y):
        pass
