import pygame
import sys
import math


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Collision Test")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Shape:
    def __init__(self, shape_type, color, **kwargs):
        self.shape_type = shape_type
        self.color = color
        self.kwargs = kwargs

    def draw(self):
        if self.shape_type == "rectangle":
            pygame.draw.rect(screen, self.color, pygame.Rect(self.kwargs['x'], self.kwargs['y'], self.kwargs['width'], self.kwargs['height']))
        elif self.shape_type == "circle":
            pygame.draw.circle(screen, self.color, (self.kwargs['x'], self.kwargs['y']), self.kwargs['radius'])
        elif self.shape_type == "triangle":
            pygame.draw.polygon(screen, self.color, self.kwargs['vertices'])
        elif self.shape_type == "hexagon":
            pygame.draw.polygon(screen, self.color, self.kwargs['vertices'])


class Ball:
    def __init__(self, x, y, radius, color):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.color = color
        self.mass = 100
        self.speed = 5
        self.direction = [1, 1]  # Movement direction
        self.shape_type = "circle"
        self.kwargs = {'x': x, 'y': y, 'radius': radius} 

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x_pos), int(self.y_pos)), self.radius)


    def update(self):
        # Collision with the circle
        distance_squared = (self.x_pos - circle.kwargs['x'])**2 + (self.y_pos - circle.kwargs['y'])**2
        sum_radii_squared = (self.radius + circle.kwargs['radius'])**2

        if distance_squared <= sum_radii_squared:
            ##print("Circle circle")
            normal_vector = [self.x_pos - circle.kwargs['x'], self.y_pos - circle.kwargs['y']]
            magnitude = math.sqrt(normal_vector[0]**2 + normal_vector[1]**2)
            normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                          self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection


        if self.x_pos - self.radius < rectangle.kwargs['x'] + rectangle.kwargs['width'] and \
            self.x_pos + self.radius > rectangle.kwargs['x'] and \
            self.y_pos - self.radius < rectangle.kwargs['y'] + rectangle.kwargs['height'] and \
            self.y_pos + self.radius > rectangle.kwargs['y']:
                ##print("Circle rectangle")


                normal_vector = [0, 0]
                if self.x_pos < rectangle.kwargs['x']:
                    normal_vector[0] = -1
                elif self.x_pos > rectangle.kwargs['x'] + rectangle.kwargs['width']:
                    normal_vector[0] = 1
                if self.y_pos < rectangle.kwargs['y']:
                    normal_vector[1] = -1
                elif self.y_pos > rectangle.kwargs['y'] + rectangle.kwargs['height']:
                    normal_vector[1] = 1

                dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
                reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                            self.direction[1] - 2 * dot_product * normal_vector[1]]

                self.direction = reflection


        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > WIDTH:
            self.direction[0] *= -1

        if self.y_pos - self.radius < 0 or self.y_pos + self.radius > HEIGHT:
            self.direction[1] *= -1


        self.y_pos += self.direction[1] * self.speed * 0.5
        self.x_pos += self.direction[0] * self.speed * 0.5





def check_collision(shape1, shape2, ball_pos=None):
    if hasattr(shape1, 'shape_type') and hasattr(shape2, 'shape_type'):
        if shape1.shape_type == "circle" and shape2.shape_type == "circle":
            return check_collision_circle_circle(shape1.kwargs, shape2.kwargs)
        elif shape1.shape_type == "circle" and shape2.shape_type == "rectangle":
            return check_collision_rect_circle(shape2.kwargs, shape1.kwargs)
        elif shape1.shape_type == "rectangle" and shape2.shape_type == "rectangle":
            return check_collision_rect_rect(shape1.kwargs, shape2.kwargs)
    elif hasattr(shape1, 'radius') and hasattr(shape2, 'radius'):

        return check_collision_circle_circle(shape1.__dict__, shape2.__dict__)
    return False



def check_collision_rect_rect(rect1, rect2):

    if rect1['x'] + rect1['width'] < rect2['x'] or rect1['x'] > rect2['x'] + rect2['width']:
        return False


    if rect1['y'] + rect1['height'] < rect2['y'] or rect1['y'] > rect2['y'] + rect2['height']:
        return False


    return True



def check_collision_circle_circle(circle1, circle2):
    distance_squared = (circle1["x"] - circle2["x"])**2 + (circle1["y"] - circle2["y"])**2
    sum_radii_squared = (circle1["radius"] + circle2["radius"])**2
    return distance_squared <= sum_radii_squared


def check_collision_rect_circle(rect, circle):

    closest_x = clamp(circle['x'], rect['x'], rect['x'] + rect['width'])
    closest_y = clamp(circle['y'], rect['y'], rect['y'] + rect['height'])


    distance_x = circle['x'] - closest_x
    distance_y = circle['y'] - closest_y


    if math.sqrt(distance_x**2 + distance_y**2) <= circle['radius']:
        return True


    axes = [(1, 0), (0, 1)]
    for axis in axes:
        projection_rect = project_rectangle(rect, axis)
        projection_circle = project_circle(circle, axis)

        if not overlap(projection_rect, projection_circle):
            return False

    return True

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def project_rectangle(rect, axis):

    vertices = [
        (rect['x'], rect['y']),
        (rect['x'] + rect['width'], rect['y']),
        (rect['x'] + rect['width'], rect['y'] + rect['height']),
        (rect['x'], rect['y'] + rect['height'])
    ]
    projections = [dot_product(vertex, axis) for vertex in vertices]
    return min(projections), max(projections)

def project_circle(circle, axis):

    center_projection = dot_product((circle['x'], circle['y']), axis)
    radius_projection = circle['radius']
    return center_projection - radius_projection, center_projection + radius_projection

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def overlap(projection1, projection2):

    return projection1[1] >= projection2[0] and projection2[1] >= projection1[0]



rectangle = Shape("rectangle", RED, x=200, y=150, width=50, height=150)
circle = Shape("circle", RED, x=600, y=500, radius=30)
ball = Ball(50, 50, 20, WHITE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.update()
    

    if check_collision(ball, rectangle):
        ball.direction[0] *= -1
        ball.direction[1] *= -1

    if check_collision(ball, circle):
        ball.direction[0] *= -1
        ball.direction[1] *= -1



    screen.fill((0, 0, 0))
    ball.draw()
    rectangle.draw()
    circle.draw()
    


    pygame.display.flip()


    pygame.time.Clock().tick(60)