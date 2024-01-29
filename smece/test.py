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

    def intersects(self, x, y, radius):
        # Calculate the distance from the center of the ball to the line
        distance = abs((self.end[1] - self.start[1]) * x - (self.end[0] - self.start[0]) * y + self.end[0] * self.start[1] - self.end[1] * self.start[0]) / math.dist(self.start, self.end)
        
        # Check if the distance is less than the radius of the ball
        return distance <= radius


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
        # Update ball position based on direction and speed
        self.x_pos += self.direction[0] * self.speed
        self.y_pos += self.direction[1] * self.speed

        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > WIDTH:
            self.direction[0] *= -1

        if self.y_pos - self.radius < 0 or self.y_pos + self.radius > HEIGHT:
            self.direction[1] *= -1

        # Check for collisions with lines
        for line in lines:
            if line.intersects(self.x_pos, self.y_pos, self.radius):
                # Calculate the normal vector of the line
                line_vector = (line.end[0] - line.start[0], line.end[1] - line.start[1])
                line_length = math.dist(line.start, line.end)
                normal_vector = (-line_vector[1] / line_length, line_vector[0] / line_length)

                # Calculate the dot product of the ball's direction and the line's normal
                dot_product = self.direction[0] * normal_vector[0] + self.direction[1] * normal_vector[1]

                # Reflect the ball's direction based on the line's normal
                self.direction[0] -= 2 * dot_product * normal_vector[0]
                self.direction[1] -= 2 * dot_product * normal_vector[1]

                # Ensure the ball is outside the line to prevent immediate re-collision
                self.x_pos += self.direction[0] * self.speed
                self.y_pos += self.direction[1] * self.speed

# ... (rest of your code remains unchanged)


# ... (rest of your code remains unchanged)


# Create shapes
line1 = Line((100, 200), (200, 200), WHITE)
line2 = Line((300, 400), (400, 300), WHITE)
lines = [line1, line2]

# Create ball
ball = Ball(50, 50, 20, WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position and check for collisions
    ball.update()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    ball.draw()
    
    for line in lines:
        line.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
