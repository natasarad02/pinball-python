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
        if ball.x_pos > self.a_x and ball.x_pos < self.b_x:
            line_vector = pygame.math.Vector2(self.b_x - self.a_x, self.b_y - self.a_y)
            point_vector = pygame.math.Vector2(ball.x_pos - self.a_x, ball.y_pos - self.a_y)

        # Calculate the projection of point_vector onto line_vector
            t = point_vector.dot(line_vector) / line_vector.length_squared()

        # Calculate the closest point on the line to the ball center
            closest_point = pygame.math.Vector2(self.a_x + t * line_vector.x, self.a_y + t * line_vector.y)

        # Check if the distance between the closest point and the ball center is less than the ball radius
            distance = math.sqrt((closest_point.x - ball.x_pos) ** 2 + (closest_point.y - ball.y_pos) ** 2)

            normal_vector = pygame.math.Vector2(-line_vector.y, line_vector.x)
            incident_angle = point_vector.angle_to(normal_vector)

            if incident_angle < 0:
                incident_angle += 360

        # print(distance <= ball.radius)
            return math.radians(incident_angle), distance <= ball.radius
        else:
            return None, False
    def rotate_left(self):
        self.b_x = self.a_x + self.distance#math.tan(self.rotation_angle) * (self.b_y - self.a_y)
        self.b_y = self.a_y
        self.draw()
    def rotate_reset_left(self):
        self.b_x = self.tmp_b_x
        self.b_y = self.tmp_b_y

    def rotate_right(self):
        self.a_x = self.b_x - self.distance#math.tan(self.rotation_angle) * (self.a_y - self.b_y)
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

    def update(self, flippers, circle_obstacles):
        # Collision with obstacle_circle
        for i in range(len(flippers)):
            incident_angle, isCollided = flippers[i].is_collided(self)
            #print(incident_angle)

            if isCollided == True:

                reflection_angle =  incident_angle + math.radians(180)
                print(math.degrees(reflection_angle))
                self.direction = [math.cos(reflection_angle), math.sin(reflection_angle)]
                length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
                reflection = [self.direction[0] / length, self.direction[1] / length]
                self.direction = reflection





            #reflection_vector = pygame.math.Vector2()
            #reflection_vector.from_polar((self.x_speed , incident_angle + 180))
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
           # self.x_speed = self.retention * self.x_speed
           # self.y_speef = self.retention * self.y_speed



        '''
        for i in range(len(flippers)):

            if flippers[i].is_rotated == True:
                if self.x_pos - self.radius < flippers[i].x + left_flipper.w and \
                    self.x_pos + self.radius > flippers[i].x and \
                    self.y_pos - self.radius < flippers[i].y + left_flipper.h and \
                    self.y_pos + self.radius > flippers[i].y:
              #  print("Circle rectangle")

                # Calculate normal vector for the rectangle
                        normal_vector = [0, 0]
                        if self.x_pos < flippers[i].x:
                            normal_vector[0] = -1
                        elif self.x_pos > flippers[i].x + left_flipper.w:
                            normal_vector[0] = 1
                        if self.y_pos < flippers[i].y:
                            normal_vector[1] = -1
                        elif self.y_pos > flippers[i].y + left_flipper.h:
                            normal_vector[1] = 1

                # Calculate the reflection vector
                        dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
                        reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                            self.direction[1] - 2 * dot_product * normal_vector[1]]

                        self.direction = reflection
            else:
                pass

         '''


        # Collision with window edges
        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > WIDTH:
            self.direction[0] *= -1
          #  self.x_speed = self.retention * self.x_speed
          #  self.y_speed = self.retention * self.y_speed

        if self.y_pos - self.radius < 0 or self.y_pos + self.radius > HEIGHT:
            self.direction[1] *= -1
          #  self.x_speed = self.retention * self.x_speed
         #   self.y_speed = self.retention * self.y_speed

        self.y_pos += self.direction[1] * self.y_speed * 0.5
        self.x_pos += self.direction[0] * self.x_speed * 0.5




    #def draw(self):
     #   self.circle = pygame.draw.circle(self.screen, self.color, (self.x_pos, self.y_pos), self.radius)








def draw_walls():
    left = pygame.draw.line(screen, 'purple', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'purple', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'purple', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'purple', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list


ball = Ball(250, 50, 30, 'blue', 100, 4000, .9, 2, 2, 1, 0.02, HEIGHT, WIDTH, fps)


circle_obstacle1 = Circle(200, 400, 50, 'green')
circle_obstacle2 = Circle(380, 200, 50, 'green')
circle_obstacle3 = Circle(550, 400, 50, 'green')
circle_obstacles = [circle_obstacle1, circle_obstacle2, circle_obstacle3]

line = Line(100, 700, 380, 850, 'red', 6)
timer = pygame.time.Clock()
left_flipper = Line(100, 1000, 300, 1150, 'purple', 30)
right_flipper = Line(480, 1150, 680, 1000, 'purple', 30)
flippers = [left_flipper, right_flipper]
run = True
while run:

    timer.tick(fps)
    screen.fill('black')
    walls = draw_walls()
    ball.draw()
    circle_obstacle1.draw()
    circle_obstacle2.draw()
    circle_obstacle3.draw()
    #line.draw()
     # Check collision with the right flipper
    ball.update(flippers, circle_obstacles)


   # brick.update_pivot()
   # brick.draw_brick('purple')
    left_flipper.draw()
    right_flipper.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_flipper.rotate_left()
              # left_flipper.rotate_left(timer)
            else:

                right_flipper.rotate_right()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_flipper.rotate_reset_left()
                #left_flipper.reset_rotation(timer)
            else:

               right_flipper.rotate_reset_right()
    #elapsed_time = timer.tick(30) / 1000.0
    #brick.update(elapsed_time)





    pygame.display.flip()
pygame.quit()