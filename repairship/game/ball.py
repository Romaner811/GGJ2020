import os
import pygame

from repairship.core import pixelgameapp


ASSETS_PATH = r".\assets"


class BouncingBallApp(pixelgameapp.PixelGameApp):
    def __init__(self, size, speed, bg, *args, **kwargs):
        super(BouncingBallApp, self).__init__(size, *args, **kwargs)
        self._ball_animation_filepath = os.path.join(ASSETS_PATH, "ball", "ball.png")
        self.speed = speed
        self.bg = bg
        self.ball = pygame.image.load(self._ball_animation_filepath)

        self.ball_rect = self.ball.get_rect()
        self.boaundaries_rect = self.screen.get_rect()

    def on_frame(self, event):
        self.ball_rect = self.ball_rect.move(self.speed.get_pair())
        if self.ball_rect.left < 0 or self.ball_rect.right > self.boaundaries_rect.width:
            self.speed.x = -self.speed.x
        if self.ball_rect.top < 0 or self.ball_rect.bottom > self.boaundaries_rect.height:
            self.speed.y = -self.speed.y

        self.screen.fill(self.bg)
        self.screen.blit(self.ball, self.ball_rect)

        self.flush_screen()
