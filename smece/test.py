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

        # Collision with the lines
        line_collision = False
        for line in lines:
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
        else:
            # If no line collision, update position as before
            self.y_pos += self.direction[1] * self.speed * 0.5
            self.x_pos += self.direction[0] * self.speed * 0.5

        # Collision with window edges
        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > WIDTH:
            self.direction[0] *= -1

        if self.y_pos - self.radius < 0 or self.y_pos + self.radius > HEIGHT:
            self.direction[1] *= -1

        # Update position after collisions
        self.y_pos += self.direction[1] * self.speed * 0.5
        self.x_pos += self.direction[0] * self.speed * 0.5

#------------------------------------------------------------------------------------------------------------------

# Helper function to check collision with circle and line
def check_collision_circle_line(circle, line):
    # Calculate the closest point on the line to the circle
    closest_point_X, closest_point_Y = closest_point_on_line(circle['x'], circle['y'], line['start'][0], line['start'][1], line['end'][0], line['end'][1])

    # Check if the closest point is within the line segment
    if is_point_on_line_segment((closest_point_X, closest_point_Y), line['start'], line['end']):
        # Check if the closest point is within the circle's radius
        distance_squared = (circle['x'] - closest_point_X) ** 2 + (circle['y'] - closest_point_Y) ** 2
        return distance_squared <= circle['radius'] ** 2

    return False





# Helper function to check if a point is on a line segment
def is_point_on_line_segment(point, start, end):
    # Check if the point is within the bounding box of the line segment
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])
    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])

    return min_x <= point[0] <= max_x and min_y <= point[1] <= max_y



# Helper function to find the closest point on a line to a given point
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
        closest_x = x1 + param * C
        closest_y = y1 + param * D
        return closest_x, closest_y



# Helper function to check collision
def check_collision(shape1, shape2, ball_pos=None):
    if hasattr(shape1, 'shape_type') and hasattr(shape2, 'shape_type'):
        if shape1.shape_type == "circle" and shape2.shape_type == "line":
            return check_collision_circle_line(shape1.kwargs, shape2.kwargs, ball_pos)
    return False



def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def project_circle(circle, axis):
    # Project the circle onto the axis
    center_projection = dot_product((circle['x'], circle['y']), axis)
    radius_projection = circle['radius']
    return center_projection - radius_projection, center_projection + radius_projection

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]




# Create shapes

line1 = Line((100, 200), (200, 200), WHITE)
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


    for line in lines:
        if check_collision_circle_line(ball.kwargs, line.kwargs):
            print("Circle line")
            # Calculate the reflection vector
            line_start = line.kwargs['start']
            line_end = line.kwargs['end']
            line_vector = [line_end[0] - line_start[0], line_end[1] - line_start[1]]
            magnitude = math.sqrt(line_vector[0] ** 2 + line_vector[1] ** 2)
            normal_vector = [line_vector[1] / magnitude, -line_vector[0] / magnitude]
            dot_product = ball.direction[0] * normal_vector[0] + ball.direction[1] * normal_vector[1]
            reflection = [ball.direction[0] - 2 * dot_product * normal_vector[0], ball.direction[1] - 2 * dot_product * normal_vector[1]]
            ball.direction = reflection

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    ball.draw()
    
    for line in lines:
        line.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)