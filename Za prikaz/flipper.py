import pygame
from pygame import Vector2
# from ball import *
import tkinter as tk
import math

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height * 0.9
WIDTH = screen_width * 0.4

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
wall_thickness = 10

fps = 60

#print(128/WIDTH)
#print(130/WIDTH)
#print(136/WIDTH)
#print(150 / WIDTH)
background_image = pygame.transform.scale(pygame.image.load("pozadina.png"), (WIDTH, HEIGHT))
sun_image = pygame.transform.scale(pygame.image.load("sun.png"), (0.125 * WIDTH, 0.125 * WIDTH))
moon_image = pygame.transform.scale(pygame.image.load("moon_img.png"), (0.127 * WIDTH, 0.127 * WIDTH))
neptune_image = pygame.transform.scale(pygame.image.load("neptune.png"), (0.132 * WIDTH, 0.132 * WIDTH))
hexagon_image = pygame.transform.scale(pygame.image.load("yoda.png"), (0.146 * WIDTH, 0.146 * WIDTH))
original_score_image = pygame.image.load("score.png")
aspect_ratio = original_score_image.get_width() / original_score_image.get_height()
new_height = int(WIDTH / aspect_ratio)
score_image = pygame.transform.scale(original_score_image, (WIDTH, new_height))
kraj = pygame.transform.scale(pygame.image.load("kraj.png"), (WIDTH, HEIGHT))

board_angle = math.radians(30)
g = 9.81
ball_gravity = g * math.sin(board_angle)
pushing_force = 90
gravity_vector = pygame.math.Vector2(0, ball_gravity)
pushing_force_vector = pygame.math.Vector2(0, 1)
ball_mass = 3
#print(ball_mass * ball_gravity)
dt = 0.5
force_at_beginning = pushing_force # - ball_mass * ball_gravity
acceleration_0 = force_at_beginning / ball_mass
# acceleration_0_x = acceleration_0 * math.sqrt(2) / 2
# acceleration_0_y = acceleration_0 * math.sqrt(2) / 2
x_speed_0 = 0  # acceleration_0  * dt * math.sqrt(2)/2
y_speed_0 = 0  # acceleration_0 * dt * math.sqrt(2)/2

y_speed_vector = pygame.math.Vector2(y_speed_0)
x_speed_vector = pygame.math.Vector2(x_speed_0)
direction = x_speed_vector + y_speed_vector + gravity_vector
direction = direction.normalize()

global total_points
total_points = 0

def gravity(ball, ball_gravity, gravity_vector, direction, dt):
    force_reaction = 0.5 * ball.force
    if ball.direction[0] < 0:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(-1, 0)))
    else:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(1, 0)))

    force_x = force_reaction * math.cos(angle)
    force_y = force_reaction * math.sin(angle)
    ball.force = math.sqrt(force_x ** 2 + force_y ** 2)
    force_g = ball.mass * ball_gravity


    if ball.direction[1] < 0:
        force_y += force_g
    else:
        force_y = abs(force_y - force_g)

    acceleration_x = force_x / ball.mass
    acceleration_y = force_y / ball.mass
    ball.x_speed += acceleration_x * dt
    ball.y_speed += acceleration_y * dt
    if ball.y_speed >= 35:
        ball.y_speed -= acceleration_y*dt
    print("Brzine: ", ball.x_speed, ball.y_speed)



def gravity_circle(ball, ball_gravity, gravity_vector, direction, dt):
    force_reaction = 0.5 * ball.force
    if ball.direction[0] < 0:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(-1, 0)))
    else:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(1, 0)))

    force_x = force_reaction * math.cos(angle)
    force_y = force_reaction * math.sin(angle)
    force_g = ball.mass * ball_gravity
    ball.force = math.sqrt(force_x ** 2 + force_y ** 2)


    if ball.direction[1] < 0:
        force_y += force_g
    else:
        force_y = force_y - force_g

    #print("Ugao: ", math.degrees(angle), " x: ", force_x, " y: ", force_y, " g: ", force_g)
    #ball.force = math.sqrt(force_x ** 2 + force_y ** 2)

    acceleration_x = force_x / ball.mass
    acceleration_y = force_y / ball.mass
    ball.x_speed += acceleration_x * dt
    ball.y_speed += acceleration_y * dt
    if ball.y_speed >= 35:
        ball.y_speed -= acceleration_y*dt

def gravity_poly(ball, ball_gravity, gravity_vector, direction, dt):
    force_reaction = 0.55 * ball.force
    if ball.direction[0] < 0:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(-1, 0)))
    else:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(1, 0)))

    force_x = force_reaction * math.cos(angle)
    force_y = force_reaction * math.sin(angle)
    force_g = ball.mass * ball_gravity
    ball.force = math.sqrt(force_x ** 2 + force_y ** 2)


    if ball.direction[1] < 0:
        force_y += force_g
    else:
        force_y = force_y - force_g

    #print("Ugao: ", math.degrees(angle), " x: ", force_x, " y: ", force_y, " g: ", force_g)

    #ball.force = math.sqrt(force_x ** 2 + force_y ** 2)
    acceleration_x = force_x / ball.mass
    acceleration_y = force_y / ball.mass
    ball.x_speed += acceleration_x * dt
    ball.y_speed += acceleration_y * dt
    if ball.y_speed >= 35:
        ball.y_speed -= acceleration_y*dt


def gravity_flipper(ball, ball_gravity, gravity_vector, direction, dt):
    if 0.19 * WIDTH < ball.direction[0] < 0.76 * WIDTH:
        force_reaction = 0.6 * ball.force
    else:
        force_reaction = 0.5 * ball.force

    if ball.direction[0] < 0:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(-1, 0)))
    else:
        angle = math.radians(direction.angle_to(pygame.math.Vector2(1, 0)))

    force_x = force_reaction * math.cos(angle)
    force_y = force_reaction * math.sin(angle)
    force_g = ball.mass * ball_gravity
    ball.force = math.sqrt(force_x ** 2 + force_y ** 2)

    if ball.direction[1] < 0:
        force_y += force_g
    else:
        force_y = force_y - force_g

    #print("Ugao: ", math.degrees(angle), " x: ", force_x, " y: ", force_y, " g: ", force_g)

   # ball.force = math.sqrt(force_x ** 2 + force_y ** 2)
    acceleration_x = force_x / ball.mass
    acceleration_y = force_y / ball.mass
    ball.x_speed += acceleration_x * dt
    ball.y_speed += acceleration_y * dt
    if ball.y_speed >= 35:
        ball.y_speed -= acceleration_y*dt




def rotation(ball):

    omega = math.sqrt(ball.x_speed**2 + ball.y_speed**2)/ball.radius
    rotation_direction = get_rotation_direction((0, -1), ball.direction)
    if rotation_direction == "Clockwise":

        # self.rotation_angle += 40  # +omega * dt, omega += moment_sile/moment_inercije

        ball.rotation_angle += math.degrees(omega * ball.dt)  # 20

    elif rotation_direction == "Counter-clockwise":
        ball.rotation_angle -= math.degrees(omega * ball.dt)  # 20

    ball.rect.center = (ball.x_pos, ball.y_pos)




def Sign(x):
    if x != 0:
        return x / abs(x)
    else:
        return 0


class Line:
    def __init__(self, a_x, a_y, b_x, b_y, color, width):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.color = color
        self.width = width
        self.distance = math.sqrt((self.b_x - self.a_x) ** 2 + (self.b_y - self.a_y) ** 2)
        self.rotation_angle = math.asin((self.b_y - self.a_y) / self.distance)
        self.tmp_a_x = self.a_x
        self.tmp_a_y = self.a_y
        self.tmp_b_y = self.b_y
        self.tmp_b_x = self.b_x

    def draw(self):
        pygame.draw.line(screen, self.color, (self.a_x, self.a_y), (self.b_x, self.b_y), self.width)

    def transparent(self):
        self.color = (0, 0, 0, 0)
    def pink(self):
        self.color = (255, 20, 147)

    def is_collided(self, ball):
        if ball.x_pos >= self.a_x - ball.radius and ball.x_pos <= self.b_x + ball.radius and self.a_x != self.b_x:
            midpoint_y = (self.a_y + self.b_y) / 2
            # midpoint_x = (self.a_x + self.b_x) / 2
            line_vector = pygame.math.Vector2(self.b_x - self.a_x, self.b_y - self.a_y)
            circle_to_line = pygame.math.Vector2(ball.x_pos - self.a_x, ball.y_pos - self.a_y)
            cross_product = line_vector.x * circle_to_line.y - line_vector.y * circle_to_line.x
            isLeft = False
            isRight = False

            if cross_product > 0:

                normal_vector = line_vector.rotate(-90)

            elif cross_product < 0:
                normal_vector = line_vector.rotate(90)
            else:
                normal_vector = None

            projection = circle_to_line.dot(normal_vector.normalize())

            if abs(projection) <= ball.radius:
                incident_vector = pygame.math.Vector2(ball.direction[0], ball.direction[1])
                incident_angle = incident_vector.angle_to(normal_vector)
                reflection_vector = incident_vector - 2 * incident_vector.dot(
                    normal_vector.normalize()) * normal_vector.normalize()

                if incident_angle == 180 or incident_angle == 0:
                    reflection_vector = -normal_vector
                if incident_angle == 90:
                    reflection_vector = line_vector

                reflection_vector.normalize()
                return math.radians(incident_angle), True, reflection_vector

            else:
                return None, False, None
        elif self.a_x == self.b_x:
            if ball.y_pos < self.b_y and ball.y_pos > self.a_y:
                midpoint_y = (self.a_y + self.b_y) / 2
                # midpoint_x = (self.a_x + self.b_x) / 2
                line_vector = pygame.math.Vector2(self.b_x - self.a_x, self.b_y - self.a_y)
                circle_to_line = pygame.math.Vector2(ball.x_pos - self.a_x, ball.y_pos - self.a_y)
                cross_product = line_vector.x * circle_to_line.y - line_vector.y * circle_to_line.x
                isLeft = False
                isRight = False

                if cross_product > 0:

                    normal_vector = line_vector.rotate(-90)

                elif cross_product < 0:
                    normal_vector = line_vector.rotate(90)
                else:
                    normal_vector = None

                projection = circle_to_line.dot(normal_vector.normalize())

                if abs(projection) <= ball.radius:
                    incident_vector = pygame.math.Vector2(ball.direction[0], ball.direction[1])
                    incident_angle = incident_vector.angle_to(normal_vector)
                    reflection_vector = incident_vector - 2 * incident_vector.dot(
                        normal_vector.normalize()) * normal_vector.normalize()

                    if incident_angle == 180 or incident_angle == 0:
                        reflection_vector = -normal_vector
                    # if incident_angle == 90:
                    #    reflection_vector = line_vector

                    reflection_vector.normalize()
                    return math.radians(incident_angle), True, reflection_vector
                else:
                    return None, False, None
            else:
                return None, False, None

        else:
            return None, False, None

def RotatePoly(points, angle):
    rotated_points = []
    theta = math.radians(angle)
    cosang, sinang = math.cos(theta), math.sin(theta)
    n = len(points)
    pointx = points[0][0]  # sum(p[0] for p in points) / n
    pointy = points[0][1]  # sum(p[1] for p in points) / n

    for p in points:
        x, y = p[0], p[1]
        tx, ty = x - pointx, y - pointy
        new_x = (tx * cosang + ty * sinang) + pointx
        new_y = (-tx * sinang + ty * cosang) + pointy
        rotated_points.append((new_x, new_y))

    return rotated_points


class Poly:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.lines = self.create_lines()

    def create_lines(self):
        lines = []
        num_points = len(self.points)
        for i in range(num_points):
            line = Line(
                self.points[i][0], self.points[i][1],
                self.points[(i + 1) % num_points][0], self.points[(i + 1) % num_points][1],
                'blue', 10
            )
            lines.append(line)
            line.draw()
        return lines

    def is_collided(self, ball):
        vector = pygame.math.Vector2()
        average_x = sum(x for x, y in self.points) / len(self.points)
        average_y = sum(y for x, y in self.points) / len(self.points)
        center_poly = pygame.math.Vector2(average_x, average_y)
        # isCollided = False
        max = -math.inf
        poly_to_circle = pygame.math.Vector2(ball.x_pos - center_poly.x, ball.y_pos - center_poly.y)
        poly_to_circle_norm = poly_to_circle.normalize()

        for i in range(1, len(self.points)):
            current_poly_corner = pygame.math.Vector2(self.points[i][0], self.points[i][1])
            v = pygame.math.Vector2(current_poly_corner.x - center_poly.x, current_poly_corner.y - center_poly.y)
            current_projection = v.dot(poly_to_circle_norm)

            if max < current_projection:
                max = current_projection

        if poly_to_circle.magnitude() - max - ball.radius > 0 and poly_to_circle.magnitude() > 0:
            return None, None, False
        else:
            reflection_vector = -poly_to_circle.reflect(poly_to_circle_norm)
            incident_vector = pygame.math.Vector2(ball.direction[0], ball.direction[1])
            incident_angle = incident_vector.angle_to(poly_to_circle_norm)
            return incident_angle, reflection_vector, True

    def draw(self):
        pygame.draw.polygon(screen, self.color, self.points)


class Flipper(Poly):
    def __init__(self, points, color):
        super().__init__(points, color)
        # self.image = pygame.image.load("flipper.png")
        # self.image = pygame.transform.scale(self.image, (100, 100))
        # self.surface = pygame.Surface((int(WIDTH), int(HEIGHT)), pygame.SRCALPHA)
        self.points = points
        self.tmp_points = self.points
        self.color = color

    def rotate_right(self):
        self.points = RotatePoly(self.points, -45)
        self.draw()

    def draw_left_flipper(self):
        self.draw()
        # self.surface.blit(self.image, (0, 0))

    def rotate_left(self):
        self.points = RotatePoly(self.points, 45)
        # #print(self.points)
        self.draw()

    def rotate_reset(self):
        self.points = self.tmp_points
        self.draw()

    def draw_right_flipper(self):
        pass


class Circle:
    def __init__(self, x_pos, y_pos, radius, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


class Ball(Circle):
    def __init__(self, x_pos, y_pos, radius, color, picture, mass, force, retention, y_speed, x_speed, id, friction,
                 HEIGHT,
                 WIDTH, fps, acceleration, dt, direction):

        super().__init__(x_pos, y_pos, radius, color)
        self.mass = mass
        self.retention = retention

        self.id = id
        self.circle = ''
        self.friction = friction
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.force = force
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.dt = dt
        self.fps = fps
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.wall_thickness = 10
        self.acceleration = acceleration
        self.force = force
        self.in_free_fall = True
        self.direction = [0, -1]
        self.y_speed = y_speed
        self.x_speed = x_speed
        # izmenjeno dole
        self.image_original = pygame.image.load(picture)
        self.image_original = pygame.transform.scale(self.image_original,
                                                     (2 * radius, 2 * radius))  # Scale the original image
        self.image = self.image_original.copy()  # Use a copy of the original image for drawing
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.rotation_angle = 0  # Initial rotation angle

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image_original, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)

    def update(self, line_obstacles, circle_obstacles, poly_obstacles, flippers):
        #rotation_params(self)
        rotation(self)




        for i in range(len(line_obstacles)):
            self.incident_angle, isCollided, reflection_vector = line_obstacles[i].is_collided(self)
            # #print(incident_angle)


            if isCollided:
                #print("Collision")

                #print(math.degrees(self.incident_angle))
                #print(reflection_vector)
                old_direction = self.direction
                self.direction = [reflection_vector.x,
                                  reflection_vector.y]  # [math.cos(reflection_angle), math.sin(reflection_angle)]
                #print(get_rotation_direction(old_direction, self.direction))
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]
                self.direction = reflection
                direction = pygame.math.Vector2(self.direction[0], self.direction[1])
                gravity(self, ball_gravity, gravity_vector, direction, dt)
                rotation(self)

        for i in range(len(flippers)):

            self.incident_angle, reflection_vector, isCollided = flippers[i].is_collided(self)
            if isCollided:
                self.direction = [reflection_vector.x,
                                  reflection_vector.y]  # [math.cos(reflection_angle), math.sin(reflection_angle)]
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]

                self.direction = reflection

                direction = pygame.math.Vector2(self.direction)
                gravity_flipper(self, ball_gravity, gravity_vector, direction, dt)
                rotation(self)


        for i in range(len(poly_obstacles)):
            self.incident_angle, reflection_vector, isCollided = poly_obstacles[i].is_collided(self)
            if isCollided:
                if(poly_obstacles[i]==hexagon):
                    global total_points
                    total_points+=60
                elif(poly_obstacles[i]== trapezoid_left):
                    total_points+=10
                elif(poly_obstacles[i]== trapezoid_right):
                    total_points+=10

                self.direction = [reflection_vector.x,
                                  reflection_vector.y]  # [math.cos(reflection_angle), math.sin(reflection_angle)]
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]

                self.direction = reflection

                direction = pygame.math.Vector2(self.direction)
                gravity_poly(self, ball_gravity, gravity_vector, direction, dt)
                rotation(self)


        for i in range(len(circle_obstacles)):

            distance_squared1 = (self.x_pos - circle_obstacles[i].x_pos) ** 2 + (
                    self.y_pos - circle_obstacles[i].y_pos) ** 2
            sum_radii_squared1 = (self.radius + circle_obstacles[i].radius) ** 2
            # self.x_speed += self.acceleration * 0.5
            # self.y_speed += self.acceleration * 0.5
            if distance_squared1 <= sum_radii_squared1:
                total_points+=30
                normal_vector = [self.x_pos - circle_obstacles[i].x_pos, self.y_pos - circle_obstacles[i].y_pos]
                magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
                normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

                # Calculate the reflection vector
                dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
                reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                              self.direction[1] - 2 * dot_product * normal_vector[1]]

                self.direction = reflection

                direction = pygame.math.Vector2(self.direction)
                incident_vector = pygame.math.Vector2(self.direction[0], self.direction[1])
                self.incident_angle = incident_vector.angle_to(normal_vector)
                gravity_circle(self, ball_gravity, gravity_vector, direction, dt)

                rotation(self)


        self.x_pos += self.direction[0] * self.x_speed * self.dt
        self.y_pos += self.direction[1] * self.y_speed * self.dt



    # def draw(self):
    #   self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)


def get_rotation_direction(previous_direction, current_direction):

    if previous_direction == (0, 0) or current_direction == (0, 0):
        return "No rotation"

    if previous_direction[0] > 0 and current_direction[1] > 0:
        return "Counter-clockwise"
    elif previous_direction[1] > 0 and current_direction[0] < 0:
        return "Counter-clockwise"
    elif previous_direction[0] < 0 and current_direction[1] < 0:
        return "Counter-clockwise"
    elif previous_direction[1] < 0 and current_direction[0] > 0:
        return "Counter-clockwise"
    elif previous_direction[0] > 0 and current_direction[1] < 0:
        return "Clockwise"
    elif previous_direction[1] < 0 and current_direction[0] < 0:
        return "Clockwise"
    elif previous_direction[0] < 0 and current_direction[1] > 0:
        return "Clockwise"
    elif previous_direction[1] > 0 and current_direction[0] > 0:
        return "Clockwise"

    else:
        return "No rotation"


ball = Ball(WIDTH * 0.925, HEIGHT * 0.95, 0.03 * WIDTH, 'blue', "planet.png", ball_mass, force_at_beginning, .9,
            y_speed_0, x_speed_0,
            1, 0.02, HEIGHT, WIDTH, fps, acceleration_0, dt, direction)
# ball = Ball(250, 550, 0.03*WIDTH, 'blue', 100, 6000, .9, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)

circle_obstacle1 = Circle(WIDTH * 0.24, 0.33 * HEIGHT, 0.055 * WIDTH, (29, 7, 73))
circle_obstacle2 = Circle(0.494 * WIDTH, 0.159 * HEIGHT, 0.055 * WIDTH, (29, 7, 73))
circle_obstacle3 = Circle(0.71 * WIDTH, 0.333 * HEIGHT, 0.055 * WIDTH, (29, 7, 73))
circle_obstacles = [circle_obstacle1, circle_obstacle2,
                    circle_obstacle3]  # [circle_obstacle1, circle_obstacle2, circle_obstacle3]

left = Line(0, 0, 0, HEIGHT, (255, 20, 147), 6)  # screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
right = Line(WIDTH, 0, WIDTH, HEIGHT, (255, 20, 147),
             6)  # screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
top = Line(0, 0.05 * HEIGHT, WIDTH, 0.05 * HEIGHT, (255, 20, 147),
           6)  # screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
bottom = Line(0, HEIGHT, WIDTH, HEIGHT, (255, 20, 147),
              6)  # screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)

timer = pygame.time.Clock()

#print(200 / WIDTH, 45 / HEIGHT, 15 / WIDTH)
# left_flipper = Flipper(0.13 * WIDTH, 0.771 * HEIGHT, 0.347 * WIDTH, 0.046 * HEIGHT, 'orange', WIDTH * 0.026)
# right_flipper = Flipper(0.55 * WIDTH, 0.771 * HEIGHT, 0.347 * WIDTH, 0.046 * HEIGHT, 'orange', WIDTH * 0.026)
left_flipper_points = [(0.2 * WIDTH, 0.755 * HEIGHT), (0.37 * WIDTH, 0.887 * HEIGHT), (0.34 * WIDTH, 0.9 * HEIGHT),
                       (0.15 * WIDTH, 0.78 * HEIGHT)]
right_flipper_points = [(WIDTH - x - 0.05 * WIDTH, y) for x, y in left_flipper_points]
left_flipper = Flipper(left_flipper_points, (255, 20, 147))
right_flipper = Flipper(right_flipper_points, (255, 20, 147))
#print(20 / HEIGHT)

line_wall_left_points = [(0, 0.695 * HEIGHT), (0.22 * WIDTH, 0.785 * HEIGHT), (0.22 * WIDTH, 0.79 * HEIGHT),
                         (0, 0.71 * HEIGHT)]
line_wall_left = Poly(line_wall_left_points, (255, 20, 147))

line_wall_right_points = [(0.75 * WIDTH, 0.78 * HEIGHT), (WIDTH - 0.15 * WIDTH, 0.695 * HEIGHT),
                          (WIDTH - 0.15 * WIDTH, 0.71 * HEIGHT), (0.75 * WIDTH, 0.795 * HEIGHT)]
line_wall_right = Poly(line_wall_right_points, (255, 20, 147))

tunnel_top_wall_points = [(0.8 * WIDTH, 0.2 * HEIGHT), (0.815 * WIDTH, 0.2 * HEIGHT),
                          (WIDTH - 0.15 * WIDTH, 0.25 * HEIGHT), (WIDTH - 0.15 * WIDTH - 0.015 * WIDTH, 0.25 * HEIGHT)]
tunnel_top_wall = Poly(tunnel_top_wall_points, (255, 20, 147))
# tunnel_top_window_points = [(0.9 * WIDTH, 0), (WIDTH, 0.25 * HEIGHT), (WIDTH, 0.265 * HEIGHT), (0.9 * WIDTH, 0.015 * HEIGHT)]
# tunnel_top_window_wall = Poly(tunnel_top_window_points, (255, 20, 147))

tunnel_top_window_wall_small = Line(0.83 * WIDTH, 0, WIDTH, 0.15 * HEIGHT, (255, 20, 147), 15)
score_board_points = [(0, 0), (WIDTH, 0), (WIDTH, 0.05 * HEIGHT), (0, 0.05 * HEIGHT)]
score_board = Poly(score_board_points, 'pink')
# tunnel_wall_left = Line(2*0.05*WIDTH, 0.4 * HEIGHT, 2*0.05*WIDTH, 0.65 * HEIGHT, 'white', 20)
# tunnel_right_points = [(WIDTH - 0.15 * WIDTH, 0.25 * HEIGHT), (WIDTH - 0.15 * WIDTH + 0.015 * WIDTH, 0.25 * HEIGHT), (WIDTH - 0.15 * WIDTH, HEIGHT), ]
tunnel_window_left = Line(0, 0.4 * HEIGHT, 0, 0.7 * HEIGHT, (255, 20, 147), 20)
tunnel_window_right = Line(WIDTH - 0.15 * WIDTH, 0.25 * HEIGHT, WIDTH - 0.15 * WIDTH, HEIGHT, (255, 20, 147), 15)
# tunnel_left = Line(2*0.05*WIDTH, 0.65 * HEIGHT, 4*0.045*WIDTH, 0.7 * HEIGHT, 'white', 20)
# left_tunnel = [tunnel_wall_left, line_wall_left, tunnel_window_left]

line_obstacles = [left, right, top, tunnel_window_right,
                  tunnel_top_window_wall_small]  # [line_wall_left, line_wall_right, left, right, top, bottom]#[line4, left, right, top, bottom]#[left_flipper, right_flipper, line_wall_left, line_wall_right, left, right, top, bottom] #, line1, line2, line3, line4]
flippers = [left_flipper, right_flipper]
trapezoid_points_left = [(0.12 * WIDTH, 0.47 * HEIGHT), (0.17 * WIDTH, 0.5 * HEIGHT), (0.27 * WIDTH, 0.65 * HEIGHT),
                         (0.22 * WIDTH, 0.65 * HEIGHT)]
trapezoid_points_right = [(WIDTH - x - 0.08 * WIDTH, y) for x, y in trapezoid_points_left]
hexagon_points = [(0.4 * WIDTH, 0.45 * HEIGHT), (0.44 * WIDTH, 0.4 * HEIGHT), (0.54 * WIDTH, 0.4 * HEIGHT),
                  (0.58 * WIDTH, 0.45 * HEIGHT), (0.54 * WIDTH, 0.5 * HEIGHT), (0.44 * WIDTH, 0.5 * HEIGHT)]

trapezoid_left = Poly(trapezoid_points_left, (0, 102, 204))
trapezoid_right = Poly(trapezoid_points_right, (0, 102, 204))
hexagon = Poly(hexagon_points, 'dark gray')
poly_obstacles = [trapezoid_left, trapezoid_right, hexagon, line_wall_left, line_wall_right,
                  tunnel_top_wall]  # [trapezoid_left, trapezoid_right, hexagon]
run = True

lives = 2
score = 0
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 45)
while run:

    screen.blit(background_image, (0, 0))

    timer.tick(fps)

    ball.draw()
    if (ball.y_pos > HEIGHT):
        ball = Ball(WIDTH * 0.925, HEIGHT * 0.95, 0.03 * WIDTH, 'blue', "planet.png", ball_mass, force_at_beginning, .9,
                    y_speed_0,
                    x_speed_0, 1, 0.02, HEIGHT, WIDTH, fps, acceleration_0, dt, direction)
        lives -=1
        ball.draw()
        
    
    left.draw()
    right.draw()
    top.draw()
    bottom.draw()

    circle_obstacle1.draw()
    sun_image_position = (WIDTH * 0.187, 0.287 * HEIGHT)
    screen.blit(sun_image, sun_image_position)

    circle_obstacle3.draw()
    moon_image_position = (WIDTH * 0.657, 0.29 * HEIGHT)
    screen.blit(moon_image, moon_image_position)

    circle_obstacle2.draw()
    neptune_image_position = (WIDTH * 0.438, 0.115 * HEIGHT)
    screen.blit(neptune_image, neptune_image_position)

    line_wall_left.draw()
    line_wall_right.draw()
    trapezoid_left.draw()
    trapezoid_right.draw()
    hexagon.draw()
    yoda_pos = (WIDTH * 0.42, 0.393 * HEIGHT)
    screen.blit(hexagon_image, yoda_pos)

    left_flipper.draw()
    # left_flipper.draw()
    right_flipper.draw()

    tunnel_window_left.draw()
    tunnel_window_right.draw()
    tunnel_top_wall.draw()
    # tunnel_top_window_wall.draw()
    tunnel_top_window_wall_small.draw()
    score_board.draw()
    screen.blit(score_image, (0, 0))
    score = total_points
    score_text = font2.render("{}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH*0.3, HEIGHT*0.01))
    lives_text = font2.render("{}".format(lives), True, (255, 255, 255))
    screen.blit(lives_text, (WIDTH*0.78, HEIGHT*0.01))
    ball.update(line_obstacles, circle_obstacles, poly_obstacles, flippers)

    if(lives==0):
        screen.blit(kraj, (0, 0))
        score = total_points
        score_text = font.render("{}".format(score), True, (255, 255, 255))
        screen.blit(score_text, (WIDTH*0.2, HEIGHT*0.42))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and lives>0:
                left_flipper.rotate_left()
            elif event.key == pygame.K_RIGHT and lives>0:
                right_flipper.rotate_right()
            elif event.key == pygame.K_SPACE and lives>0:
                ball.x_speed = ball.acceleration * dt
                ball.y_speed = ball.acceleration * dt

                #print(ball.y_speed)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and lives>0:
                left_flipper.rotate_reset()
                # left_flipper.reset_rotation(timer)
            elif event.key == pygame.K_RIGHT and lives>0:
                right_flipper.rotate_reset()

    pygame.display.flip()
pygame.quit()