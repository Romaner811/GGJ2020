import pygame

def image_at(sheet, rect_points):
    rect = pygame.Rect(*rect_points)
    image = pygame.Surface(rect.size).convert_alpha()
    image.blit(sheet, (0,0), rect)
    return image

def slice_animation(width, height, no_slices):
    return [(w, 0, width, height) for w in range(0, width * no_slices, width)]

