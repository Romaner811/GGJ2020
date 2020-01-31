import os
import pygame
import itertools

from . import graphics_utils

_here = os.path.dirname(__file__)

_walking_sheet = pygame.image.load(os.path.join(_here, "data", "astronaut-walk.png"))
_typing_sheet = pygame.image.load(os.path.join(_here, "data", "astronaut-walk.png"))

def spaceman_walking_iter():
    return [graphics_utils.image_at(_walking_sheet, r) for r in graphics_utils.slice_animation(7, 16, 4)]

def spaceman_typing_iter():
    return [graphics_utils.image_at(_typing_sheet, r) for r in graphics_utils.slice_animation(7, 16, 5)]

if __name__ == "__main__":
    MULTIPLIER = 32
    SIZE = WIDTH, HEIGHT = 32 * MULTIPLIER, 16 * MULTIPLIER
    BACKGROUND_COLOR = pygame.Color('black')
    FPS = 10
    
    display = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    for frame in itertools.cycle(spaceman_walking_iter()):
        print("a")
        frame_scaled = pygame.transform.scale(frame, (7 * MULTIPLIER, 16 * MULTIPLIER))
        print("b")
        display.fill(BACKGROUND_COLOR)
        print("c")
        display.blit(frame_scaled, (0,0))
        print("d")
        pygame.display.flip()
        print("e")
        clock.tick(10)
        
