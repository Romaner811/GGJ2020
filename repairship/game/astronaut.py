import os
import pygame
from pygame.rect import Rect

from repairship.core import pixelgameapp
from repairship.core.sizes import Size
from repairship.graphics.animation import Animation
from repairship.game.character import Character, PhysicalObject
from repairship.game.character_control import CharacterControl


ASSETS_PATH = r"assets"


class AstronautApp(pixelgameapp.PixelGameApp):
    def __init__(self, size, *args, **kwargs):
        super(AstronautApp, self).__init__(size, *args, **kwargs)

        sheet = pygame.image.load(os.path.join(ASSETS_PATH, "astronaut", "walking.png"))
        self.astronaut_animation = Animation(sheet, Size(7, 16), self.tick_interval)

        self.player_control = CharacterControl()
        # TODO: config.... json?
        from unittest import mock
        self.astronaut = Character(
            PhysicalObject(self.astronaut_animation.get_frame(0).get_rect()),
            mock.Mock(speed=Size(2, 1)),
            self.player_control
        )
        self.astronaut.hitbox.center = self.screen.get_rect().center

        self.init_player_control()

    def init_player_control(self):
        # keyboard events -> player_control
        # self.event_subscribe(...)
        pass

    def translate_rect(self, logic_rect):
        return pygame.rect.Rect(
            logic_rect.x,
            self.screen.get_height() - logic_rect.y - logic_rect.height,
            logic_rect.width,
            logic_rect.height
        )

    def on_frame(self, event):
        # draw the character in the correct position.
        player_image = self.astronaut_animation.get_frame_at(pygame.time.get_ticks())
        translated_rect = self.translate_rect(self.astronaut.hitbox)
        self.screen.blit(player_image, translated_rect)

        self.flush_screen()
