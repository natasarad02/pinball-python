import pygame
from pygame import Vector2
#from ball import *
import tkinter as tk
import math
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

HEIGHT = screen_height*0.9
WIDTH = screen_width*0.3

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
wall_thickness = 10

fps = 60



class Line:
    def __init__(self, a_x, a_y, b_x, b_y, color, width):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.color = color
        self.width = width
        self.distance = math.sqrt((self.b_x - self.a_x) ** 2 + (self.b_y - self.a_y) ** 2)
        self.rotation_angle = math.asin((self.b_y - self.a_y)/self.distance)
        self.tmp_a_x = self.a_x
        self.tmp_a_y = self.a_y
        self.tmp_b_y = self.b_y
        self.tmp_b_x = self.b_x



    def draw(self):
        pygame.draw.line(screen, self.color, (self.a_x, self.a_y), (self.b_x, self.b_y), self.width)



    def is_collided(self, ball):
        line_vector = pygame.math.Vector2(self.b_x - self.a_x, self.b_y - self.a_y)
        midpoint_y = (self.a_y + self.b_y)/2
        tmp_line_vector = line_vector
        point_vector = pygame.math.Vector2(ball.x_pos - self.a_x, ball.y_pos - self.a_y)
          #0, 0.7 * HEIGHT, 0.13 * WIDTH, 0.771 * HEIGHT
        # Calculate the projection of point_vector onto line_vector
        t = point_vector.dot(line_vector) / line_vector.length_squared()

        # Calculate the closest point on the line to the ball center
        closest_point = pygame.math.Vector2(self.a_x + t * line_vector.x, self.a_y + t * line_vector.y)
        #print(closest_point)
        # Check if the distance between the closest point and the ball center is less than the ball radius
        distance = math.sqrt((closest_point.x - ball.x_pos) ** 2 + (closest_point.y - ball.y_pos) ** 2)

        if self.a_x != self.b_x:
            if ball.x_pos >= self.a_x and ball.x_pos <= self.b_x:

                incident_vector = pygame.math.Vector2(ball.direction[0], ball.direction[1])
                normal_vector = pygame.math.Vector2(-line_vector.y, line_vector.x)
            #print(incident_vector)
                incident_angle = incident_vector.angle_to(normal_vector)
                print(ball.direction)
                if incident_angle < 0:
                    incident_angle += 360

                reflection_vector = incident_vector - 2 * normal_vector.dot(incident_vector) * normal_vector



                if (incident_angle == 180 or incident_angle == 0) and ball.y_pos < midpoint_y or (ball.y_pos > midpoint_y and ball.y_pos < min(self.a_y, self.b_y)):
                    reflection_vector = -normal_vector
                if (incident_angle == 180 or incident_angle == 0) and ball.y_pos > midpoint_y or (ball.y_pos > midpoint_y and ball.y_pos > max(self.a_y, self.b_y)):
                    reflection_vector = normal_vector
                if incident_angle == 90:
                    reflection_vector = line_vector
                reflection_vector.normalize()
                return math.radians(incident_angle), distance <= ball.radius, reflection_vector
            else:
               return None, False, None

        else:
            if ball.y_pos >= self.a_y and ball.y_pos <= self.b_y:

                incident_vector = pygame.math.Vector2(ball.direction[0], ball.direction[1])
                normal_vector = pygame.math.Vector2(-line_vector.y, line_vector.x)
                # print(incident_vector)
                incident_angle = incident_vector.angle_to(normal_vector)
                print(ball.direction)
                if incident_angle < 0:
                    incident_angle += 360

                reflection_vector = incident_vector - 2 * normal_vector.dot(incident_vector) * normal_vector

                if (incident_angle == 180 or incident_angle == 0) and ball.x_pos > self.a_x:
                    reflection_vector = -normal_vector
                if (incident_angle == 180 or incident_angle == 0) and ball.x_pos < self.a_x:
                    reflection_vector = normal_vector
                if incident_angle == 90:
                    reflection_vector = line_vector




                reflection_vector.normalize()
                return math.radians(incident_angle), distance <= ball.radius, reflection_vector
            else:
                return None, False, None
            #if (reflection_vector.x == -74999.4 and reflection_vector.y == 99999.2) or (reflection_vector.x == 74999.4 and reflection_vector.y == -99999.2) or (reflection_vector.x == -74999.4 and reflection_vector.y == -99999.2) or (reflection_vector.x == 74999.4 and reflection_vector.y == 99999.2):
             #   reflection_vector = -normal_vector






        # print(distance <= ball.radius)









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

        if poly_to_circle.magnitude() - max - ball.radius > 0 and poly_to_circle.magnitude() >0:
            return None, False
        else:
            reflection_vector = -poly_to_circle.reflect(poly_to_circle_norm)
            return reflection_vector, True









    def draw(self):
        pygame.draw.polygon(screen, self.color, self.points)

class Flipper(Line):
    def __init__(self, a_x, a_y, b_x, b_y, color, width):
        super().__init__(a_x, a_y, b_x, b_y, color, width)

    def rotate_left(self):
        self.b_x = self.a_x + self.distance  # math.tan(self.rotation_angle) * (self.b_y - self.a_y)
        self.b_y = self.a_y
        self.draw()

    def rotate_reset_left(self):
        self.b_x = self.tmp_b_x
        self.b_y = self.tmp_b_y

    def rotate_right(self):
        self.a_x = self.b_x - self.distance  # math.tan(self.rotation_angle) * (self.a_y - self.b_y)
        self.a_y = self.b_y
        self.draw()

    def rotate_reset_right(self):
        self.a_x = self.tmp_a_x
        self.a_y = self.tmp_a_y

class Circle:
    def __init__(self, x_pos, y_pos, radius, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

class Ball(Circle):
    def __init__(self,  x_pos, y_pos, radius, color, mass, force, retention, y_speed, x_speed, id, friction, HEIGHT, WIDTH, fps):

        super().__init__(x_pos, y_pos, radius, color)
        #self.x_pos = x_pos
        #self.y_pos = y_pos
        #self.radius = radius
        #self.color = color
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
        self.x_speed = self.acceleration * 0.5
        self.y_speed = self.acceleration * 0.5

        #self.positions = [self.x_pos, self.y_pos]
        #self.speed = [self.x_speed, self.y_speed]

    def update(self, flippers, circle_obstacles, poly_obstacles):
        # Collision with obstacle_circle

        for i in range(len(flippers)):
            incident_angle, isCollided, reflection_vector = flippers[i].is_collided(self)
            #print(incident_angle)

            if isCollided:


               # print(math.degrees(incident_angle))
                self.direction = [reflection_vector.x, reflection_vector.y]#[math.cos(reflection_angle), math.sin(reflection_angle)]
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]
                self.direction = reflection





            #reflection_vector = pygame.math.Vector2()
            #reflection_vector.from_polar((self.x_speed , incident_angle + 180))

        self.x_pos += self.direction[0] * self.x_speed * 0.5
        self.y_pos += self.direction[1] * self.y_speed * 0.5


        for i in range(len(poly_obstacles)):
            reflection_vector, isCollided = poly_obstacles[i].is_collided(self)
            if isCollided:

                #self.x_speed = 0
                #self.y_speed = 0


                self.direction = [reflection_vector.x,
                                  reflection_vector.y]  # [math.cos(reflection_angle), math.sin(reflection_angle)]
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]
                self.direction = reflection


        for i in range(len(circle_obstacles)):

            distance_squared1 = (self.x_pos - circle_obstacles[i].x_pos)**2 + (self.y_pos - circle_obstacles[i].y_pos)**2
            sum_radii_squared1 = (self.radius + circle_obstacles[i].radius)**2
        #self.x_speed += self.acceleration * 0.5
       # self.y_speed += self.acceleration * 0.5
            if distance_squared1 <= sum_radii_squared1:
                normal_vector = [self.x_pos - circle_obstacles[i].x_pos, self.y_pos - circle_obstacles[i].y_pos]
                magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
                normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
                dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
                reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                          self.direction[1] - 2 * dot_product * normal_vector[1]]

                self.direction = reflection





        # Collision with window edges





    #def draw(self):
     #   self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)








def draw_walls():
    left = pygame.draw.line(screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list


ball = Ball(WIDTH * 0.32, HEIGHT * 0.045, 0.03*WIDTH, 'blue', 100, 6000, .9, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)
'''
print(250/WIDTH, 50/HEIGHT)
print(200/WIDTH, 400/HEIGHT)
print(380/WIDTH, 200/HEIGHT)
print(550/WIDTH, 400/HEIGHT)
print(100/WIDTH, 1000/HEIGHT, 300/WIDTH, 1150/HEIGHT)
print(480/WIDTH, 1150/HEIGHT, 680/WIDTH, 1000/HEIGHT)
print(30/WIDTH, 50/WIDTH)
'''
circle_obstacle1 = Circle(WIDTH * 0.26, 0.308 * HEIGHT, 0.065 * WIDTH, 'green')
circle_obstacle2 = Circle(0.494 * WIDTH, 0.154 * HEIGHT, 0.065 * WIDTH, 'green')
circle_obstacle3 = Circle(0.716 * WIDTH, 0.308 * HEIGHT, 0.065 * WIDTH, 'green')
circle_obstacles = [circle_obstacle1, circle_obstacle2, circle_obstacle3]


line1 = Line(100, 700, 380, 850, 'red', 6)
line2 = Line(50, 200, 50, 500, 'red', 6)
line3 = Line(500, 850, 700, 700, 'red', 6)
line4 = Line(400, 400, 700, 400, 'red', 6)

left = Line(0, 0, 0, HEIGHT, 'purple', 6)#screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
right = Line(WIDTH, 0, WIDTH, HEIGHT, 'purple', 6) #screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
top = Line(0, 0, WIDTH, 0, 'purple', 6) #screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
bottom = Line(0, HEIGHT, WIDTH, HEIGHT, 'purple', 6) #screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)

timer = pygame.time.Clock()

left_flipper = Flipper(0.13 * WIDTH, 0.771 * HEIGHT, 0.39 * WIDTH, 0.887 * HEIGHT, 'purple', 50)
right_flipper = Flipper(0.625 * WIDTH, 0.887 * HEIGHT, 0.885 * WIDTH, 0.771 * HEIGHT, 'purple', 50)
#left_flipper_points = [(0.13 * WIDTH, 0.771 * HEIGHT), (0.39 * WIDTH, 0.887 * HEIGHT),, (0.38 * WIDTH, 0.887 * HEIGHT + 30/HEIGHT)]
#right_flipper_points = [(0.625 * WIDTH, 0.887 * HEIGHT), (0.885 * WIDTH, 0.771 * HEIGHT), ]

line_wall_left = Line(0.01 * WIDTH, 0.7 * HEIGHT, 0.13 * WIDTH, 0.771 * HEIGHT, 'white', 20)
line_wall_right = Line(0.885 * WIDTH, 0.771 * HEIGHT,WIDTH, 0.7 * HEIGHT, 'white', 20)

#tunnel_wall_left = Line(2*0.05*WIDTH, 0.4 * HEIGHT, 2*0.05*WIDTH, 0.65 * HEIGHT, 'white', 20)
tunnel_window_left = Line(0, 0.4 * HEIGHT, 0, 0.7 * HEIGHT, 'white', 20)
tunnel_window_right = Line(WIDTH, 0.4 * HEIGHT, WIDTH, 0.7 * HEIGHT, 'white', 20)
#tunnel_left = Line(2*0.05*WIDTH, 0.65 * HEIGHT, 4*0.045*WIDTH, 0.7 * HEIGHT, 'white', 20)
#left_tunnel = [tunnel_wall_left, line_wall_left, tunnel_window_left]

flippers_and_line_obstacles = [left_flipper, right_flipper, line_wall_left, line_wall_right, tunnel_window_right, tunnel_window_left, left, right, top, bottom] #, line1, line2, line3, line4]

trapezoid_points_left = [(0.05 * WIDTH, 0.6 * HEIGHT), (0.1 * WIDTH, 0.55 * HEIGHT), (0.2 * WIDTH, 0.7 * HEIGHT), (0.13 * WIDTH, 0.7 * HEIGHT)]
trapezoid_points_right = [(WIDTH - x, y) for x, y in trapezoid_points_left]
hexagon_points = [
    (WIDTH / 2 + 50, HEIGHT / 2 - 87),
    (WIDTH / 2 + 100, HEIGHT / 2),
    (WIDTH / 2 + 50, HEIGHT / 2 + 87),
    (WIDTH / 2 - 50, HEIGHT / 2 + 87),
    (WIDTH / 2 - 100, HEIGHT / 2),
    (WIDTH / 2 - 50, HEIGHT / 2 - 87)
]

trapezoid_left = Poly(trapezoid_points_left, 'red')
trapezoid_right = Poly(trapezoid_points_right, 'red')
hexagon = Poly(hexagon_points, 'yellow')
poly_obstacles = [trapezoid_left, trapezoid_right, hexagon]
run = True
while run:

    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()
    ball.draw()
    '''
    line1.draw()
    line2.draw()
    line3.draw()
    line4.draw()
    '''
    left.draw()
    right.draw()
    top.draw()
    bottom.draw()
    circle_obstacle1.draw()
    circle_obstacle2.draw()
    circle_obstacle3.draw()

    line_wall_left.draw()
    line_wall_right.draw()
    trapezoid_left.draw()
    trapezoid_right.draw()
    hexagon.draw()
    #trapezoid.create_lines()


     # Check collision with the right flipper
    ball.update(flippers_and_line_obstacles, circle_obstacles, poly_obstacles)


   # brick.update_pivot()
   # brick.draw_brick('purple')
    left_flipper.draw()
    right_flipper.draw()

    tunnel_window_left.draw()
    tunnel_window_right.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_flipper.rotate_left()
              # left_flipper.rotate_left(timer)
            elif event.key == pygame.K_RIGHT:

                right_flipper.rotate_right()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_flipper.rotate_reset_left()
                #left_flipper.reset_rotation(timer)
            elif event.key == pygame.K_RIGHT:

               right_flipper.rotate_reset_right()
    #elapsed_time = timer.tick(30) / 1000.0
    #brick.update(elapsed_time)





    pygame.display.flip()
pygame.quit()