
class Size:
    def __init__(self, width, height):
        self.x = self.width = width
        self.y = self.height = height

    def get_pair(self):
        return self.x, self.y

    def __iter__(self):
        return iter(self.get_pair())


class PixelArtSize(Size):
    PIXEL_SIZE = 8  # tmp  (8)

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
