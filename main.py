import pygame
from ball import *

pygame.init()
import tkinter as tk
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.9
WIDTH = screen_width*0.35;


screen = pygame.display.set_mode([WIDTH, HEIGHT])
wall_thickness = 10
def draw_walls():
    left = pygame.draw.line(screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list

fps = 60
ball = Ball(60, 50, 20, 'blue', 100, 50, .75, 0, 0, 1, 0.02, HEIGHT, WIDTH, fps)
timer = pygame.time.Clock()
brick = Brick(50, 500, 20, 40, HEIGHT, WIDTH)
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()

    brick.show_and_update("green")
    ball.draw()
    ball.check_gravity()
    ball.update_pos()
    #ball.y_speed = ball.check_gravity(HEIGHT, WIDTH, wall_thickness)
    #ball.update_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()