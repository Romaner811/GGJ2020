from repairship.core.sizes import Size, Direction


class PhysicalObject:
    def __init__(self, hitbox, velocity=None):
        if velocity is None:
            velocity = Direction.STAY.get()

        self.hitbox = hitbox
        self.velocity = velocity
        self._last_time = 0

    def update(self, time):
        diff = (time - self._last_time) / 1000.0
        self.hitbox.move_ip(self.velocity.x * diff, self.velocity.y * diff)
        self._last_time = time

        print("diff", diff)
        print("vel", self.velocity.get_pair())
        print("hb", self.hitbox)

    def collision(self, other):
        pass
