import pygame
import sys
import math

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

    def reflect_off_line(self, line):
        # Calculate the vector representing the line
        line_vector = (line.end[0] - line.start[0], line.end[1] - line.start[1])

        # Calculate the vector representing the ball's velocity
        ball_vector = (self.direction[0], self.direction[1])

        # Calculate the dot product of the two vectors
        dot_product = line_vector[0] * ball_vector[0] + line_vector[1] * ball_vector[1]

        # Calculate the length of the line vector squared
        line_length_squared = line_vector[0] ** 2 + line_vector[1] ** 2

        # Calculate the reflection vector
        reflection_vector = (
            2 * dot_product * line_vector[0] / line_length_squared - ball_vector[0],
            2 * dot_product * line_vector[1] / line_length_squared - ball_vector[1]
        )

        # Update the ball's direction with the reflection vector
        self.direction = [reflection_vector[0], reflection_vector[1]]

    def update(self):
        # Collision with the rectangle
        if check_collision(self, rectangle):
            self.reflect_off_line(Line((rectangle.kwargs['x'], rectangle.kwargs['y']),
                                       (rectangle.kwargs['x'] + rectangle.kwargs['width'], rectangle.kwargs['y'])))

        # Collision with the circle
        if check_collision(self, circle):
            print("usao u if")
            self.reflect_off_line(Line((circle.kwargs['x'], circle.kwargs['y']),
                                       (circle.kwargs['x'] + 2 * circle.kwargs['radius'], circle.kwargs['y'])))

        # Update position after collisions
        self.y_pos += self.direction[1] * self.speed * 0.5
        self.x_pos += self.direction[0] * self.speed * 0.5

# Helper function to check collision
def check_collision(shape1, shape2):
    if hasattr(shape1, 'shape_type') and hasattr(shape2, 'shape_type'):
        if shape1.shape_type == "circle" and shape2.shape_type == "circle":
            return check_collision_circle_circle(shape1.kwargs, shape2.kwargs)
        elif shape1.shape_type == "circle" and shape2.shape_type == "rectangle":
            return check_collision_rect_circle(shape2.kwargs, shape1.kwargs)
    return False

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

    return False

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

# Create shapes
rectangle = Shape("rectangle", RED, x=500, y=150, width=50, height=150)
circle = Shape("circle", RED, x=600, y=500, radius=30)

# Create ball
ball = Ball(50, 50, 20, WHITE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball.update()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    ball.draw()
    rectangle.draw()
    circle.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
