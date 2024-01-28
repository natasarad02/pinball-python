import pygame
from pygame import Vector2
#from ball import *
import tkinter as tk
import math
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.9
WIDTH = screen_width*0.3;

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
        self.direction = [1, 1]
        #self.positions = [self.x_pos, self.y_pos]
        #self.speed = [self.x_speed, self.y_speed]

    def update(self, left_flipper, right_flipper, obstacle_circle1, obstacle_circle2, obstacle_circle3):
        # Collision with obstacle_circle1
        distance_squared1 = (self.x_pos - obstacle_circle1.x_pos)**2 + (self.y_pos - obstacle_circle1.y_pos)**2
        sum_radii_squared1 = (self.radius + obstacle_circle1.radius)**2

        if distance_squared1 <= sum_radii_squared1:
            normal_vector = [self.x_pos - obstacle_circle1.x_pos, self.y_pos - obstacle_circle1.y_pos]
            magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
            normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                          self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection
        # Collision with obstacle_circle2
        distance_squared2 = (self.x_pos - obstacle_circle2.x_pos) ** 2 + (self.y_pos - obstacle_circle2.y_pos) ** 2
        sum_radii_squared2 = (self.radius + obstacle_circle2.radius) ** 2

        if distance_squared2 <= sum_radii_squared2:
            normal_vector = [self.x_pos - obstacle_circle2.x_pos, self.y_pos - obstacle_circle2.y_pos]
            magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
            normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                              self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection
        # Collision with obstacle_circle2
        distance_squared3 = (self.x_pos - obstacle_circle3.x_pos) ** 2 + (self.y_pos - obstacle_circle3.y_pos) ** 2
        sum_radii_squared3 = (self.radius + obstacle_circle3.radius) ** 2

        if distance_squared3 <= sum_radii_squared3:
            normal_vector = [self.x_pos - obstacle_circle3.x_pos, self.y_pos - obstacle_circle3.y_pos]
            magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
            normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                              self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection

        if self.x_pos - self.radius < left_flipper.x + left_flipper.w and \
            self.x_pos + self.radius > left_flipper.x and \
            self.y_pos - self.radius < left_flipper.y + left_flipper.h and \
            self.y_pos + self.radius > left_flipper.y:
              #  print("Circle rectangle")

                # Calculate normal vector for the rectangle
                normal_vector = [0, 0]
                if self.x_pos < left_flipper.x:
                    normal_vector[0] = -1
                elif self.x_pos > left_flipper.x + left_flipper.w:
                    normal_vector[0] = 1
                if self.y_pos < left_flipper.y:
                    normal_vector[1] = -1
                elif self.y_pos > left_flipper.y + left_flipper.h:
                    normal_vector[1] = 1

                # Calculate the reflection vector
                dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
                reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                            self.direction[1] - 2 * dot_product * normal_vector[1]]

                self.direction = reflection
        if self.x_pos - self.radius < right_flipper.x + right_flipper.w and \
                self.x_pos + self.radius > right_flipper.x and \
                self.y_pos - self.radius < right_flipper.y + right_flipper.h and \
                self.y_pos + self.radius > right_flipper.y:
            #  print("Circle rectangle")

            # Calculate normal vector for the rectangle
            normal_vector = [0, 0]
            if self.x_pos < right_flipper.x:
                normal_vector[0] = -1
            elif self.x_pos > right_flipper.x + right_flipper.w:
                normal_vector[0] = 1
            if self.y_pos < right_flipper.y:
                normal_vector[1] = -1
            elif self.y_pos > right_flipper.y + right_flipper.h:
                normal_vector[1] = 1

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                          self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection


        # Collision with window edges
        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > WIDTH:
            self.direction[0] *= -1

        if self.y_pos - self.radius < 0 or self.y_pos + self.radius > HEIGHT:
            self.direction[1] *= -1

        self.y_pos += self.direction[1] * self.acceleration * 0.5
        self.x_pos += self.direction[0] * self.acceleration * 0.5




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
           # print(self.y)


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


ball = Ball(250, 50, 30, 'blue', 100, 1500, .75, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)
circle_obstacle1 = Ball(200, 400, 50, 'green', 100, 1000, .75, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)
circle_obstacle2 = Ball(380, 200, 50, 'green', 100, 1000, .75, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)
circle_obstacle3 = Ball(550, 400, 50, 'green', 100, 1000, .75, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)
timer = pygame.time.Clock()
left_flipper = Left_Flipper(150, 1000, 35, 200, Vector2(150, 1000), HEIGHT, WIDTH)
right_flipper = Right_Flipper(400, 1000, 35, 200, Vector2(500, 1000), HEIGHT, WIDTH)
run = True
while run:

    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()
    ball.draw()
    circle_obstacle1.draw()
    circle_obstacle2.draw()
    circle_obstacle3.draw()
     # Check collision with the right flipper
    ball.update(left_flipper, right_flipper, circle_obstacle1, circle_obstacle2, circle_obstacle3)


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