import pygame
import sys
import math
import numpy as np
# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Collision Test")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Shape class
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

class Line:
    def __init__(self, start, end, color):
        self.shape_type = "line"
        self.start = start
        self.end = end
        self.color = color
        self.kwargs = {'start': start, 'end': end}

    def draw(self):
        pygame.draw.line(screen, self.color, self.start, self.end)

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.color = color
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
            print("Circle circle")
            normal_vector = [self.x_pos - circle.kwargs['x'], self.y_pos - circle.kwargs['y']]
            magnitude = math.sqrt(normal_vector[0]**2 + normal_vector[1]**2)
            normal_vector = [normal_vector[0] / magnitude, normal_vector[1] / magnitude]

            # Calculate the reflection vector
            dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]
            reflection = [self.direction[0] - 2 * dot_product * normal_vector[0],
                          self.direction[1] - 2 * dot_product * normal_vector[1]]

            self.direction = reflection

        # Collision with the lines
        line_collision = False
        for line in lines:
            print("Usao u for")
            print(line1)
            print("-------------------")
            print(line2)
            if check_collision_circle_line(ball.kwargs, line.kwargs, (ball.x_pos, ball.y_pos)):
                print("Circle line")
                line_collision = True
                line_start = line.kwargs['start']
                line_end = line.kwargs['end']

                # Calculate the normal vector of the line
                line_vector = [line_end[0] - line_start[0], line_end[1] - line_start[1]]
                magnitude = math.sqrt(line_vector[0] ** 2 + line_vector[1] ** 2)
                normal_vector = [line_vector[1] / magnitude, -line_vector[0] / magnitude]

                # Calculate the reflection vector
                dot_product = ball.direction[0] * normal_vector[0] + ball.direction[1] * normal_vector[1]
                reflection = [ball.direction[0] - 2 * dot_product * normal_vector[0],
                            ball.direction[1] - 2 * dot_product * normal_vector[1]]

                ball.direction = reflection

        # Update position after collisions
        if line_collision:
            # Only update the position if there was a line collision
            ball.y_pos += ball.direction[1] * ball.speed * 0.5
            ball.x_pos += ball.direction[0] * ball.speed * 0.5




        # Collision with the rectangle
        if self.x_pos - self.radius < rectangle.kwargs['x'] + rectangle.kwargs['width'] and \
            self.x_pos + self.radius > rectangle.kwargs['x'] and \
            self.y_pos - self.radius < rectangle.kwargs['y'] + rectangle.kwargs['height'] and \
            self.y_pos + self.radius > rectangle.kwargs['y']:
                print("Circle rectangle")

                # Calculate normal vector for the rectangle
                normal_vector = [0, 0]
                if self.x_pos < rectangle.kwargs['x']:
                    normal_vector[0] = -1
                elif self.x_pos > rectangle.kwargs['x'] + rectangle.kwargs['width']:
                    normal_vector[0] = 1
                if self.y_pos < rectangle.kwargs['y']:
                    normal_vector[1] = -1
                elif self.y_pos > rectangle.kwargs['y'] + rectangle.kwargs['height']:
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

        # Update position after collisions
        self.y_pos += self.direction[1] * self.speed * 0.5
        self.x_pos += self.direction[0] * self.speed * 0.5

#------------------------------------------------------------------------------------------------------------------

def check_collision_circle_line(circle, line, ball_pos):
    # Calculate the closest point on the line to the circle
    closest_point = closest_point_on_line(circle['x'], circle['y'], line['start'][0], line['start'][1], line['end'][0], line['end'][1], ball_pos)

    print(f"Checking collision circle line")
    print(f"Closest Point: {closest_point}")
    print(f"Line Start: {line['start']}")
    print(f"Line End: {line['end']}")

    # Check if the closest point is within the line segment
    if is_point_on_line_segment(closest_point, line['start'], line['end'], ball_pos):
        print("Point is on line segment")
        # Check if the distance between the circle's center and the closest point is within the circle's radius
        distance_squared = (circle['x'] - closest_point[0])**2 + (circle['y'] - closest_point[1])**2
        radius_squared = circle['radius']**2
        if distance_squared <= radius_squared:
            print("Collision detected!")
            return True
        else:
            print("Distance not within circle's radius")
    else:
        print("Point not on line segment")

    return False



# Helper function to check if a point is on a line segment
def is_point_on_line_segment(point, start, end, ball_pos):
    # Check if the point is within the bounding box of the line segment
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])
    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])

    # Include ball's position in the check
    return min_x <= point[0] <= max_x and min_y <= point[1] <= max_y and ball_pos[0] != point[0] and ball_pos[1] != point[1]




# Helper function to find the closest point on a line to a given point
def closest_point_on_line(px, py, x1, y1, x2, y2, ball_pos):
    A = px - x1
    B = py - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1 if len_sq == 0 else dot / len_sq

    if param < 0:
        return x1, y1
    elif param > 1:
        return x2, y2
    else:
        return x1 + param * C, y1 + param * D


# Helper function to check collision
def check_collision(shape1, shape2, ball_pos=None):
    if hasattr(shape1, 'shape_type') and hasattr(shape2, 'shape_type'):
        if shape1.shape_type == "circle" and shape2.shape_type == "circle":
            return check_collision_circle_circle(shape1.kwargs, shape2.kwargs)
        elif shape1.shape_type == "circle" and shape2.shape_type == "rectangle":
            return check_collision_rect_circle(shape2.kwargs, shape1.kwargs)
        elif shape1.shape_type == "rectangle" and shape2.shape_type == "rectangle":
            return check_collision_rect_rect(shape1.kwargs, shape2.kwargs)
        elif shape1.shape_type == "circle" and shape2.shape_type == "line":
            return check_collision_circle_line(shape1.kwargs, shape2.kwargs, ball_pos)
    elif hasattr(shape1, 'radius') and hasattr(shape2, 'radius'):
        # Handle the case where shape1 and shape2 are Ball objects
        return check_collision_circle_circle(shape1.__dict__, shape2.__dict__)
    return False



def check_collision_rect_rect(rect1, rect2):
    # Check overlap along the x-axis
    if rect1['x'] + rect1['width'] < rect2['x'] or rect1['x'] > rect2['x'] + rect2['width']:
        return False

    # Check overlap along the y-axis
    if rect1['y'] + rect1['height'] < rect2['y'] or rect1['y'] > rect2['y'] + rect2['height']:
        return False

    # If there is overlap along both axes, it's a collision
    return True



def check_collision_circle_circle(circle1, circle2):
    distance_squared = (circle1["x"] - circle2["x"])**2 + (circle1["y"] - circle2["y"])**2
    sum_radii_squared = (circle1["radius"] + circle2["radius"])**2
    return distance_squared <= sum_radii_squared


def check_collision_rect_circle(rect, circle):
    # Calculate the closest point on the rectangle to the circle
    closest_x = clamp(circle['x'], rect['x'], rect['x'] + rect['width'])
    closest_y = clamp(circle['y'], rect['y'], rect['y'] + rect['height'])

    # Calculate the distance between the circle's center and the closest point on the rectangle
    distance_x = circle['x'] - closest_x
    distance_y = circle['y'] - closest_y

    # Check if the distance is less than the circle's radius
    if math.sqrt(distance_x**2 + distance_y**2) <= circle['radius']:
        return True

    # Check overlap along the separating axes formed by the sides of the rectangle
    axes = [(1, 0), (0, 1)]  # The axes are the normals of the sides of the rectangle
    for axis in axes:
        projection_rect = project_rectangle(rect, axis)
        projection_circle = project_circle(circle, axis)

        if not overlap(projection_rect, projection_circle):
            return False

    return True

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def project_rectangle(rect, axis):
    # Project the rectangle onto the axis
    vertices = [
        (rect['x'], rect['y']),
        (rect['x'] + rect['width'], rect['y']),
        (rect['x'] + rect['width'], rect['y'] + rect['height']),
        (rect['x'], rect['y'] + rect['height'])
    ]
    projections = [dot_product(vertex, axis) for vertex in vertices]
    return min(projections), max(projections)

def project_circle(circle, axis):
    # Project the circle onto the axis
    center_projection = dot_product((circle['x'], circle['y']), axis)
    radius_projection = circle['radius']
    return center_projection - radius_projection, center_projection + radius_projection

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def overlap(projection1, projection2):
    # Check if two 1D projections overlap
    return projection1[1] >= projection2[0] and projection2[1] >= projection1[0]


# Create shapes
rectangle = Shape("rectangle", RED, x=500, y=150, width=50, height=150)
circle = Shape("circle", RED, x=600, y=500, radius=30)
line1 = Line((100, 200), (300, 200), WHITE)
line2 = Line((300, 400), (400, 300), WHITE)
lines = [line1, line2]
# Create ball
ball = Ball(50, 50, 20, WHITE)

# Game loop
# Inside the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball.update()

    # Check collisions
    if check_collision(ball, rectangle):
        ball.direction[0] *= -1  # Reverse direction on collision
        ball.direction[1] *= -1

    if check_collision(ball, circle):
        ball.direction[0] *= -1
        ball.direction[1] *= -1

    for line in lines:
        if check_collision(ball, line, (ball.x_pos, ball.y_pos)):
            print("Game loop")
            ball.direction[0] *= -1
            ball.direction[1] *= -1

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    ball.draw()
    rectangle.draw()
    circle.draw()
    for line in lines:
        line.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)