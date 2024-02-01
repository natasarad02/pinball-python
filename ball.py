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
        #self.positions = [self.x_pos, self.y_pos]
        #self.speed = [self.x_speed, self.y_speed]
    def draw(self):
        self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def update_pos(self):
        self.y_pos += self.y_speed * 0.5
        self.x_pos += self.x_speed * 0.5
    def check_gravity(self):
        '''
        if self.x_pos >= 50 and self.x_pos <= 100:
            if self.y_pos < 500 - self.radius - (10 / 2):
                self.y_speed += self.acceleration * 0.5
            else:
                if self.y_speed > 0.3:
                    self.y_speed = self.y_speed * -1 * self.retention
                else:
                    if abs(self.y_speed) <= 0.3:
                        self.y_speed = 0
        elif self.x_pos >= 200 and self.x_pos <= 220:
            if self.y_pos < 500 - self.radius - (10 / 2):
                self.y_speed += self.acceleration * 0.5
            else:
                if self.y_speed > 0.3:
                    self.y_speed = self.y_speed * -1 * self.retention
                else:
                    if abs(self.y_speed) <= 0.3:
                        self.y_speed = 0
        #elif self.x_pos >= 220 and self.x_pos <= 250:

        else:
        '''
        if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
            self.y_speed += self.acceleration * 2
        else:
            if self.y_speed > 0.3:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= 0.3:
                    self.y_speed = 0





class Brick:

    def __init__(self, x, y, height, weight, HEIGHT, WIDTH):
        self.x = x
        self.y = y
        self.h = height
        self.w = weight
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

    def show_and_update(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect((self.x, self.y), (self.w, self.h)))
class Left_Flipper:


class Triangle:
    def __init__(self, x, y, base, height, HEIGHT, WIDTH):
        self.x = x
        self.y = y
        self.base = base
        self.height = height
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.angle = 0

    def __init__(self, x, y, height, width, pivot, HEIGHT, WIDTH, starting_angle = -45):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.pivot = pivot
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, 'purple', (0, 0, width, height))
        self.angle = starting_angle

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        #self.brick_screen = pygame.display.set_mode([width, height])

    def update_left(self, elapsed_time):
        rotation_speed = 100
        self.angle += rotation_speed * elapsed_time
    def update_reset(self, elapsed_time):
        rotation_speed = 100
        self.angle -= rotation_speed * elapsed_time

    def draw_brick(self, color):
        rotated_surface = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_surface.get_rect(topleft=(self.x, self.y))
        self.screen.blit(rotated_surface, rotated_rect.topleft)

    def rotate_left(self, timer):
        while self.angle < 0:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_left(elapsed_time)
            #self.image.fill('purple')
            self.screen.fill('black')

            self.draw_brick('purple')
            pygame.display.flip()


    def reset_rotation(self, timer):
        while self.angle > -45:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_reset(elapsed_time)
            #self.image.fill('purple')
            self.screen.fill('black')
            self.draw_brick('purple')
            pygame.display.flip()

class Right_Flipper:

    def __init__(self, x, y, height, width, pivot, HEIGHT, WIDTH, starting_angle = -135):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.pivot = pivot
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, 'purple', (0, 0, width, height))
        self.angle = starting_angle

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        #self.brick_screen = pygame.display.set_mode([width, height])

    def update_right(self, elapsed_time):
        rotation_speed = 100
        self.angle -= rotation_speed * elapsed_time
    def update_reset(self, elapsed_time):
        rotation_speed = 100
        self.angle += rotation_speed * elapsed_time

    def draw_brick(self, color):
        rotated_surface = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_surface.get_rect(topright=(self.x + self.w, self.y))
        self.screen.blit(rotated_surface, rotated_rect.topleft)

    def rotate_right(self, timer):
        while self.angle > -180:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_right(elapsed_time)
            #self.image.fill('purple')
            self.screen.fill('black')

            self.draw_brick('purple')
            pygame.display.flip()


    def reset_rotation(self, timer):
        while self.angle < -135:
            elapsed_time = timer.tick(30) / 1000.0
            self.update_reset(elapsed_time)
            #self.image.fill('purple')
            self.screen.fill('black')
            self.draw_brick('purple')
            pygame.display.flip()
    '''
    def check_gravity(self, HEIGHT, WIDTH, wall_thickness):
        if self.y_pos < HEIGHT - self.radius - (wall_thickness / 2):
            # No direct modification of self.y_speed here, as gravity is handled in _get_derivative
            pass
        else:
            if self.y_speed > 0.3:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= 0.3:
                    self.y_speed = 0


    def show_and_update(self, color):
        # Calculate the coordinates of the vertices of the triangle
        x1, y1 = self.x, self.y
        x2, y2 = self.x + self.base, self.y + self.height
        x3, y3 = self.x + self.base / 2, self.y

        rotated_triangle = pygame.transform.rotate(pygame.Surface((self.base, self.height)),
                                                   self.angle)

        # Get the rectangle of the rotated triangle
        rotated_rect = rotated_triangle.get_rect(center=(self.x + self.base / 2, self.y + self.height / 2))

        # Draw the rotated triangle
        self.screen.blit(pygame.transform.rotate(pygame.Surface((self.base, self.height)),
                                                 self.angle),
                         rotated_rect.topleft)

        # Increment the rotation angle
        self.angle += 1

        # Draw the triangle
        pygame.draw.polygon(self.screen, color, [(x1, y1), (x2, y2), (x3, y3)])
    '''