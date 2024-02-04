import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Ball")

# Ball properties
ball_center = [WIDTH // 2, HEIGHT // 2]
angle = 0

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Rotate the ball around its axis using Euler rotation
    rotated_x = ball_center[0] + BALL_RADIUS * math.cos(math.radians(angle))
    rotated_y = ball_center[1] + BALL_RADIUS * math.sin(math.radians(angle))

    # Draw the rotated ball
    pygame.draw.circle(screen, WHITE, (int(rotated_x), int(rotated_y)), BALL_RADIUS)

    # Update angle for the next frame
    angle += 2  # You can adjust the rotation speed here

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
