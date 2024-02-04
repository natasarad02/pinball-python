import pygame

import math
pygame.init()
import tkinter as tk
root = tk.Tk()
import numpy as np

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.8
WIDTH = screen_width*0.35

screen = pygame.display.set_mode([WIDTH, HEIGHT])



import pygame
from pygame import Vector2
class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, force, retention, y_speed, x_speed, id, friction, HEIGHT, WIDTH, fps):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ''
        self.friction = friction ##dodati parametar trenja i za podlogu
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.force = force
        self.fps = fps
        self.HEIGHT = HEIGHT
        self.WIDTH= WIDTH
        self.wall_thickness = 10
        self.acceleration = self.force / self.mass
       
    def draw(self):
        self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def update_pos(self):
        self.y_pos += self.y_speed * 0.5
        self.x_pos += self.x_speed * 0.5
        
    def check_gravity(self):
        if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
            self.y_speed += self.acceleration * 2
        else:
            if self.y_speed > 0.3:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= 0.3:
                    self.y_speed = 0




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
run = True


while run:
    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()

    ball.draw()
    ball.check_gravity()
    ball.update_pos()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()