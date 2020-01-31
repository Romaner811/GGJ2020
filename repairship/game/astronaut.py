import os
import pygame
from pygame.rect import Rect
from pygame.locals import *

from repairship.core.gameapp import EVENT_ID_SONG_END
from repairship.core import pixelgameapp
from repairship.core.sizes import Size
from repairship.graphics.animation import Animation
from repairship.game.character import Character, PhysicalObject
from repairship.game.character_control import CharacterControl
from repairship.units import UnitTranslator

ASSETS_PATH = r"assets"


class AstronautApp(pixelgameapp.PixelGameApp):
    def __init__(self, size, *args, **kwargs):
        super(AstronautApp, self).__init__(size, *args, **kwargs)

        sheet = pygame.image.load(os.path.join(ASSETS_PATH, "img", "astronaut", "walking.png"))
        astronaut_image_size = Size(7, 16)
        self.astronaut_animation = Animation(sheet, astronaut_image_size, 7)

        screen_center = self.screen.get_rect().center
        self.unit_translator = UnitTranslator(Size(*self.screen.get_size()), Size(*screen_center))

        self.error_sound = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "audio", "error.wav"))

        self.player_control = CharacterControl()
        astronaut_rect = Rect((0, 0), astronaut_image_size.get_pair())
        astronaut_rect.center = screen_center
        astronaut_rect = self.unit_translator.rect_to_world(astronaut_rect)
        self.astronaut = Character(
            PhysicalObject(astronaut_rect),
            {"speed": Size(20000, 0)},
            self.player_control
        )

        self.start_music()

        self.event_subscribe(KEYDOWN, self.on_key_down)
        self.event_subscribe(KEYUP, self.on_key_up)

        self.flipped = False

    def on_key_down(self, event):
        if event.key == K_w:
            self.player_control.movement.y += 1
        elif event.key == K_s:
            self.player_control.movement.y += -1
        elif event.key == K_d:
            self.player_control.movement.x += 1
            self.flipped = False
        elif event.key == K_a:
            self.player_control.movement.x += -1
            self.flipped = True
        elif event.key == K_e:
            self.player_control.interacting = True

    def on_key_up(self, event):
        if event.key == K_w:
            self.player_control.movement.y -= 1
        elif event.key == K_s:
            self.player_control.movement.y -= -1
        elif event.key == K_d:
            self.player_control.movement.x -= 1
        elif event.key == K_a:
            self.player_control.movement.x -= -1
        elif event.key == K_e:
            self.player_control.interacting = False

    def start_music(self):
        """
        Starts the music from the beginning.
        """
        pygame.mixer.music.set_endevent(EVENT_ID_SONG_END)
        pygame.mixer.music.load(os.path.join(ASSETS_PATH, "audio", "bt.ogg"))
        pygame.mixer.music.play()
        self.event_subscribe(EVENT_ID_SONG_END, self.continue_music)

    def continue_music(self, event):
        """
        Restarts the music from the loop point.
        """
        pygame.mixer.music.play(start=52.664)

    def on_frame(self, event):
        self.astronaut.update(pygame.time.get_ticks())

        player_image = self.astronaut_animation.get_frame(1) if self.player_control.movement.x == 0 else \
            self.astronaut_animation.get_frame_at(pygame.time.get_ticks())
        translated_rect = self.unit_translator.rect_to_screen(self.astronaut.hitbox)
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.flip(player_image, self.flipped, False), translated_rect)

        self.flush_screen()
