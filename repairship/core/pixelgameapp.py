import abc
import pygame

from repairship.core import gameapp, sizes


class PixelGameApp(gameapp.GameApp, abc.ABC):

    def __init__(self, size, fps=None):
        if not isinstance(size, sizes.PixelArtSize):
            size = sizes.PixelArtSize.from_real_size(*size.get_pair())
        super(PixelGameApp, self).__init__(size, fps)

        self.real_screen = self.screen
        self.pixelart_screen = pygame.Surface(size.pixeled.get_pair()).convert()

        self.screen = self.pixelart_screen

    def flush_screen(self):
        pygame.transform.scale(self.pixelart_screen, self.real_screen.get_size(), self.real_screen)
        super(PixelGameApp, self).flush_screen()
