from repairship.core.sizes import Size, Direction


class PhysicalObject:
    def __init__(self, hitbox, velocity=None):
        if velocity is None:
            velocity = Direction.STAY.get()

        self.hitbox = hitbox
        self.velocity = velocity

    def update(self, time):
        self.hitbox.x += self.velocity.x * time
        self.hitbox.y += self.velocity.y * time

    def collision(self, other):
        pass
