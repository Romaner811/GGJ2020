from repairship.core.sizes import Size, Direction


class CharacterControl:
    def __init__(self):
        self.movement = Direction.STAY.get()
        self.interacting = False
