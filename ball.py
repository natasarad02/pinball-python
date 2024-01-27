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


    def update_pos(self):
        dt = 1.0 / 60  # Time step
        dt = 1.0 / 120 # Time step


        # RK4 integration for both x and y positions
        k1x, k1y = self._get_derivative()
        k2x, k2y = self._get_derivative(x=self.x_pos + 0.5 * k1x * dt, y=self.y_pos + 0.5 * k1y * dt)
        k3x, k3y = self._get_derivative(x=self.x_pos + 0.5 * k2x * dt, y=self.y_pos + 0.5 * k2y * dt)
        k4x, k4y = self._get_derivative(x=self.x_pos + k3x * dt, y=self.y_pos + k3y * dt)

        # Update positions
        self.x_pos += (k1x + 2 * k2x + 2 * k3x + k4x) * dt / 6
        self.y_pos += (k1y + 2 * k2y + 2 * k3y + k4y) * dt / 6


    def _get_derivative(self, x=None, y=None):
        # Compute derivatives for RK4 integration
        if x is None:
            x = self.x_pos
        if y is None:
            y = self.y_pos

        # Your physics calculations go here
        # For example, include gravity, friction, and other forces

        gravity = 9.8  # Acceleration due to gravity (adjust as needed)
        friction_force = -self.friction * self.x_speed  # Friction force (adjust as needed)

        dx_dt = self.x_speed + friction_force  # Change this based on your physics model

        dy_dt = self.y_speed + gravity  # Change this based on your physics model

        dy_dt = (self.y_speed if self.y_speed is not None else 0) + gravity  # Change this based on your physics model


        return dx_dt, dy_dt

'''