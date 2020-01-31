import pygame

from repairship.core.sizes import Direction
from repairship.game.pysicalobject import PhysicalObject


class Character(PhysicalObject):
    def __init__(self, pobj, config, controls):
        super(Character, self).__init__(pobj.hitbox, pobj.velocity)
        self.config = config
        self.controls = controls

    def update(self, time):
        self.velocity = self.controls.movement(self.config["speed"])
        super(Character, self).update(time)

    def collision(self, other):
        self.velocity.setself(Direction.STAY)
