import pygame
from ball import Ball
pygame.init()

HEIGHT = 800
WIDTH = 400

screen = pygame.display.set_mode([WIDTH, HEIGHT])
wall_thickness = 10
def draw_walls():
    left = pygame.draw.line(screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list

ball = Ball(50, 50, 30, 'blue', 100, .75, 0, 0, 1, 0.02, 800, 400)
fps = 60
timer = pygame.time.Clock()
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()

    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()