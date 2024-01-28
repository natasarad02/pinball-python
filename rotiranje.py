import pygame
import sys

class RotatingObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 128, 255), (0, 0, width, height))
        self.angle = 0

    def update(self, elapsed_time):
        rotation_speed = 50
        self.angle += rotation_speed * elapsed_time

    def draw(self, screen):
        rotated_surface = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_surface.get_rect(topleft=(self.x, self.y))
        screen.blit(rotated_surface, rotated_rect.topleft)

# Pygame initialization
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

rotating_object = RotatingObject(100, 100, 50, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = clock.tick(30) / 1000.0
    rotating_object.update(elapsed_time)

    screen.fill((255, 255, 255))
    rotating_object.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
