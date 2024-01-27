import pygame

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id, friction, HEIGHT, WIDTH):
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
        self.friction = friction
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

    def draw(self):
        self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self, HEIGHT, WIDTH, wall_thickness):

        if self.y_pos < HEIGHT - self.radius - (wall_thickness / 2):
            self.y_speed += 0.5
        else:
            if self.y_speed > 0.3:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= 0.3:
                    self.y_speed = 0
        if (self.x_pos < self.radius + (wall_thickness / 2) and self.x_speed < 0) or \
                (self.x_pos > WIDTH - self.radius - (wall_thickness / 2) and self.x_speed > 0):
            self.x_speed *= -1 * self.retention
            if abs(self.x_speed) < 0.3:
                self.x_speed = 0
        if self.y_speed == 0 and self.x_speed != 0:
            if self.x_speed > 0:
                self.x_speed -= self.friction
            elif self.x_speed < 0:
                self.x_speed += self.friction

        return self.y_speed


'''
    def update_pos(self, mouse):
        if not self.selected:
            self.y_pos += self.y_speed
            self.x_pos += self.x_speed
        else:
            self.x_pos = mouse[0]
            self.y_pos = mouse[1]

    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected
    
'''


