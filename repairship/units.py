from pygame.rect import Rect

from repairship.core.sizes import Size

DEFAULT_PIXEL_RATIO = 1000


class UnitTranslator:
    def __init__(self, screen_center, screen_size, pixel_ratio=None):
        if pixel_ratio is None:
            pixel_ratio = DEFAULT_PIXEL_RATIO

        self.pixel_ratio = pixel_ratio  # world units per pixel
        self.screen_size = screen_size
        self.screen_center = screen_center

    def vect_to_world(self, gvect):
        gvect = gvect.clone()
        gvect.x *= self.pixel_ratio
        gvect.y *= self.pixel_ratio
        return gvect

    def vect_to_screen(self, wvect):
        wvect = wvect.clone()
        wvect.x /= self.pixel_ratio
        wvect.y /= self.pixel_ratio
        return wvect

    def rect_to_world(self, rect):
        return Rect(
            rect.x * self.pixel_ratio,
            (self.screen_size.height - rect.y) * self.pixel_ratio,
            rect.width * self.pixel_ratio,
            rect.height * self.pixel_ratio,
        )

    def rect_to_screen(self, rect):
        return Rect(
            rect.x / self.pixel_ratio,
            self.screen_size.height - (rect.y / self.pixel_ratio),
            rect.width / self.pixel_ratio,
            rect.height / self.pixel_ratio,
        )
