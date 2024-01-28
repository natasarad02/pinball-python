import pygame
from ball import *
import math
pygame.init()
import tkinter as tk
root = tk.Tk()
import numpy as np
import NANS_lib as lb
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.9
WIDTH = screen_width*0.35;

def collision_ball_brick(ball, brick):
    '''
    If a collision between ball and brick occurs this function returns true and position of ball center, otherwise returns false and 0
      3 | 1 | 4
    ------------
      2 |   | 2
    ------------
      5 | 1 | 6
    '''
    
    p = 0

    if ball.x_pos < brick.x_pos: # 2 or 3 or 5
        tempX = brick.x_pos
        p = 10
    elif ball.x_pos > brick.x_pos + brick.y_pos:  # 4 or 2 or 6
        tempX = brick.x_pos + brick.y_pos
        p = 12
    else:
        tempX = ball.x_pos
        p = 1
    
    if p != 1:
        if ball.y_pos < brick.y_pos: # 3 or 1 or 4
            tempY = brick.y
            if p == 10:
                p = 3
            elif p == 12:
                p = 4
        elif ball.y >= brick.y + brick.h: # 5 or 1 or 6
            tempY = brick.y + brick.h
            if p == 10:
                p = 5
            elif p == 12:
                p = 6
        else:
            tempY = ball.y
            p = 2
    elif ball.y < brick.y:
        tempY = brick.y
    else:
        tempY = brick.y + brick.h


    if math.sqrt((tempX - ball.x)**2 + (tempY - ball.y)**2) <= ball.r:
        return True, p
    else:
        return False, 0
    
def calculate_velocity(x1, y1, x2, y2, vx, vy, p, w, h):  #x1, y1 je krug
    '''
    Returns velocity of ball after collision with brick
    '''
    if p == 1:
        return vx, -vy
    elif p == 2:
        return -vx, vy
    elif p == 3:
        fx1 = np.array([x1, x2])
        fy1 = np.array([y1, y2])
        p = lb.lagrange_interpolation(fx1, fy1)
        interscCR = np.polyval(p, 0)
        koef = math.sqrt(2) / math.sqrt((0 - x2)**2 + (interscCR - y2)**2)
        vx = abs(0 - x2) * koef
        vy = abs(interscCR - y2) * koef
        return -vy, -vx
    elif p == 4:
        x2 = x2 + w
        fx1 = np.array([x1,x2])
        fy1 = np.array([y1,y2])
        p = lb.lagrange_interpolation(fx1, fy1)
        interscCR = np.polyval(p, WIDTH)
        koef = math.sqrt(2) / math.sqrt((WIDTH - x2)**2 + (interscCR - y2)**2)
        vx = (WIDTH - x2) * koef
        vy = (interscCR - y2) * koef
        return -vy, -vx
    elif p == 5:
        y2 = y2 + h
        fx1 = np.array([x1, x2])
        fy1 = np.array([y1, y2])
        p = lb.lagrange_interpolation(fx1, fy1)
        interscCR = np.polyval(p, 0)
        koef = math.sqrt(2) / math.sqrt((0 - x2)**2 + (interscCR - y2)**2)
        vx = (0 - x2) * koef
        vy = (interscCR - y2) * koef
        return -vy, -vx
    elif p == 6:
        x2 = x2 + w
        y2 = y2 + h
        fx1 = np.array([x1,x2])
        fy1 = np.array([y1,y2])
        p = lb.lagrange_interpolation(fx1, fy1)
        interscCR = np.polyval(p, WIDTH)
        koef = math.sqrt(2) / math.sqrt((WIDTH - x2)**2 + (interscCR - y2)**2)
        vx  = -(WIDTH - x2) * koef
        vy = -(interscCR - y2) * koef
        return -vy, -vx

    return vx, vy

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
brick = Brick(50, 400, 20, 40, HEIGHT, WIDTH)
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
    a, b = collision_ball_brick(ball, brick)
    if(a):
        self.vx, self.vy = calculate_velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()