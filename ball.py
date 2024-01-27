import pygame

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

    def check_gravity(self):
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
            if self.y_pos < self.HEIGHT - self.radius - (10 / 2):
                self.y_speed += self.acceleration * 0.5
            else:
                if self.y_speed > 0.3:
                    self.y_speed = self.y_speed * -1 * self.retention
                else:
                    if abs(self.y_speed) <= 0.3:
                        self.y_speed = 0

        if (self.x_pos < self.radius + (10 / 2) and self.x_speed < 0) or \
                (self.x_pos > self.WIDTH - self.radius - (0.3 / 2) and self.x_speed > 0):
            self.x_speed *= -1 * self.retention
            if abs(self.x_speed) < 0.3:
                self.x_speed = 0
        if self.y_speed == 0 and self.x_speed != 0:
            if self.x_speed > 0:
                self.x_speed -= self.friction
            elif self.x_speed < 0:
                self.x_speed += self.friction

    def update_pos(self):
       self.y_pos += self.y_speed * 0.5
       self.x_pos += self.x_speed * 0.5

class Brick:

    def __init__(self, x, y, height, weight, HEIGHT, WIDTH):
        self.x = x
        self.y = y
        self.h = height
        self.w = weight
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

    def show_and_update(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect((self.x, self.y), (self.w, self.h)))

class Triangle:
    def __init__(self, x, y, base, height, HEIGHT, WIDTH):
        self.x = x
        self.y = y
        self.base = base
        self.height = height
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.angle = 0

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