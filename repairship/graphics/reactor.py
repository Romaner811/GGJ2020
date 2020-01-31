import os
import pygame
import itertools

from . import graphics_utils

_here = os.path.dirname(__file__)


def reactor_iter():
    _reactor_core_sheet = pygame.image.load(os.path.join(_here, "data", "reactor.png")).convert_alpha()
    return [graphics_utils.image_at(_reactor_core_sheet, r) for r in graphics_utils.slice_animation(26, 22, 7)]

if __name__ == "__main__":
    MULTIPLIER = 32
    SIZE = WIDTH, HEIGHT = 22 * MULTIPLIER, 26 * MULTIPLIER
    BACKGROUND_COLOR = pygame.Color('black')
    FPS = 10
    
    display = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    for frame in itertools.cycle(reactor_iter()):
        print("a")
        frame_scaled = pygame.transform.scale(frame, (22 * MULTIPLIER, 26 * MULTIPLIER))
        print("b")
        display.fill(BACKGROUND_COLOR)
        print("c")
        display.blit(frame_scaled, (0,0))
        print("d")
        pygame.display.flip()
        print("e")
        clock.tick(10)
        
