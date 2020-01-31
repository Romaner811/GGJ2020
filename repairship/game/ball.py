import os
import pygame
from repairship.core import gameapp


ASSETS_PATH = r".\assets"


class BouncingBallApp(gameapp.GameApp):
    def __init__(self, size, speed, bg):
        super(BouncingBallApp, self).__init__(size)
        self._ball_animation_filepath = os.path.join(ASSETS_PATH, "tmp", "ball.png")
        self.speed = speed
        self.bg = bg
        self.ball = pygame.image.load(self._ball_animation_filepath)
        self.ballrect = self.ball.get_rect()

    def on_frame(self, event):
        self.ballrect = self.ballrect.move(self.speed.get_pair())
        if self.ballrect.left < 0 or self.ballrect.right > self.size.width:
            self.speed.x = -self.speed.x
        if self.ballrect.top < 0 or self.ballrect.bottom > self.size.height:
            self.speed.y = -self.speed.y
        self.screen.fill(self.bg)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()
