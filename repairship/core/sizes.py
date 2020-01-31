import enum


class Size:
    def __init__(self, width, height):
        self.x = width
        self.y = height

    @property
    def width(self):
        return self.x

    @property
    def height(self):
        return self.y

    # TODO: setters

    def get_pair(self):
        return self.x, self.y

    def __iter__(self):
        return iter(self.get_pair())

    def __add__(self, other):
        return Size(self.x + other.x, self.y + other.y)

    def multiply(self, other):
        return Size(self.x * other.x, self.y * other.y)

    def setself(self, other):
        self.x = other.x
        self.y = other.y

    def clone(self):
        return Size(*self.get_pair())


class PixelArtSize(Size):
    PIXEL_SIZE = 8

    def __init__(self, width, height, pixel_size=PIXEL_SIZE):
        super(PixelArtSize, self).__init__(
            int(width * pixel_size),
            int(height * pixel_size)
        )
        self.pixeled = Size(width, height)
        self.pixel_size = pixel_size

    @staticmethod
    def from_real_size(width, height, pixel_size=PIXEL_SIZE):
        return PixelArtSize(
            int(width / pixel_size),
            int(height / pixel_size),
            pixel_size
        )


class Direction(enum.Enum):
    STAY = Size(0, 0)

    LEFT = Size(-1, 0)
    RIGHT = Size(1, 0)
    UP = Size(0, 1)
    DOWN = Size(0, -1)

    LEFT_DOWN = Size(-1, -1)
    LEFT_UP = Size(-1, 1)
    RIGHT_DOWN = Size(1, -1)
    RIGHT_UP = Size(1, 1)

    def get(self):
        return self.value.clone()
