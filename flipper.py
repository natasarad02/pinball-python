import pygame
from pygame import Vector2
#from ball import *
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.9
WIDTH = screen_width*0.5;

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
wall_thickness = 10

fps = 60

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
        self.in_free_fall = True
        #self.positions = [self.x_pos, self.y_pos]
        #self.speed = [self.x_speed, self.y_speed]

    def update_pos(self):
        self.y_pos += self.y_speed * 0.5
        self.x_pos += self.x_speed * 0.5
    def handle_collision_with_flipper(self, left_flipper, right_flipper):

            # Check collision with the left flipper
           if self.x_pos >= left_flipper.x and self.x_pos <= (left_flipper.x + left_flipper.w)/2 and self.y_pos == 1000:
               if left_flipper.angle != -45:

                   self.y_speed = -1 * self.y_speed
                  # self.y_speed += self.acceleration * 0.5
               else:
                   if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
                       self.y_speed += self.acceleration * 0.5
                   else:
                       if self.y_speed > 0.3:
                           self.y_speed = self.y_speed * -1 * self.retention
                       else:
                           if abs(self.y_speed) <= 0.3:
                               self.y_speed = 0
           elif self.x_pos >= (left_flipper.x + left_flipper.w)/2 and self.x_pos <= (left_flipper.x + left_flipper.w) and self.y_pos == 1000:
               if left_flipper.angle != -45:
                   #self.force += 30
                #   self.acceleration = self.force / self.mass
                   self.y_speed = -1 * (self.y_speed)
                  # self.y_speed += self.acceleration * 0.5
               else:
                   if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
                       self.y_speed += self.acceleration * 0.5
                   else:
                       if self.y_speed > 0.3:
                           self.y_speed = self.y_speed * -1 * self.retention
                       else:
                           if abs(self.y_speed) <= 0.3:
                               self.y_speed = 0
           else:
               if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
                   self.y_speed += self.acceleration * 0.5
               else:
                   if self.y_speed > 0.3:
                       self.y_speed = self.y_speed * -1 * self.retention
                   else:
                       if abs(self.y_speed) <= 0.3:
                           self.y_speed = 0








    def draw(self):
        self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)




class Left_Flipper:

    def __init__(self, x, y, height, width, pivot, HEIGHT, WIDTH, starting_angle = -45):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.pivot = pivot
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, 'purple', (0, 0, width, height))
        self.angle = starting_angle

       # self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        #self.brick_screen = pygame.display.set_mode([width, height])

    def update_left(self, elapsed_time):
        rotation_speed = 100
        self.angle += rotation_speed * 0.5
    def update_reset(self, elapsed_time):
        rotation_speed = 100
        self.angle -= rotation_speed * 0.5

    def draw_brick(self, color):
        rotated_surface = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_surface.get_rect(topleft=(self.x, self.y))
        screen.blit(rotated_surface, rotated_rect.topleft)

    def rotate_left(self, timer):
        while self.angle < 0:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_left(elapsed_time)
            #self.image.fill('purple')
            #self.screen.fill('black')

            self.draw_brick('purple')
            pygame.display.flip()


    def reset_rotation(self, timer):
        while self.angle > -45:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_reset(elapsed_time)
            #self.image.fill('purple')
           # self.screen.fill('black')
            self.draw_brick('purple')
            pygame.display.flip()

class Right_Flipper:
    def __init__(self, x, y, height, width, pivot, HEIGHT, WIDTH, starting_angle=-135):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.pivot = pivot
        self.flipper_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.flipper_surface, 'purple', (0, 0, width, height))
        self.angle = starting_angle

    def update_right(self, elapsed_time):
        rotation_speed = 100
        self.angle -= rotation_speed * 0.5

    def update_reset(self, elapsed_time):
        rotation_speed = 100
        self.angle += rotation_speed * 0.5

    def draw_brick(self, color):
        rotated_surface = pygame.transform.rotate(self.flipper_surface, self.angle)
        rotated_rect = rotated_surface.get_rect(topright=(self.x + self.w, self.y))
        screen.blit(rotated_surface, rotated_rect.topleft)

    def rotate_right(self, timer):
        while self.angle > -180:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_right(elapsed_time)
            self.draw_brick('purple')
            pygame.display.flip()

    def reset_rotation(self, timer):
        while self.angle < -135:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_reset(elapsed_time)
            self.draw_brick('purple')
            pygame.display.flip()


def draw_walls():
    left = pygame.draw.line(screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list


ball = Ball(250, 50, 20, 'blue', 100, 50, .75, 0, 0, 1, 0.02, HEIGHT, WIDTH, fps)
timer = pygame.time.Clock()
left_flipper = Left_Flipper(150, 1000, 35, 200, Vector2(150, 1000), HEIGHT, WIDTH)
right_flipper = Right_Flipper(400, 1000, 35, 200, Vector2(500, 1000), HEIGHT, WIDTH)
run = True
while run:

    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()
    ball.draw()

    ball.handle_collision_with_flipper(left_flipper, right_flipper)  # Check collision with the right flipper
    ball.update_pos()


   # brick.update_pivot()
   # brick.draw_brick('purple')
    left_flipper.draw_brick('purple')
    right_flipper.draw_brick('purple')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

               left_flipper.rotate_left(timer)
            else:
                right_flipper.rotate_right(timer)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_flipper.reset_rotation(timer)
            else:
                right_flipper.reset_rotation(timer)
    #elapsed_time = timer.tick(30) / 1000.0
    #brick.update(elapsed_time)





    pygame.display.flip()
pygame.quit()