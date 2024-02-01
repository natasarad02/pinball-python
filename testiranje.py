import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
FLIPPER_COLOR = (255, 0, 0)
BALL_COLOR = (0, 0, 255)
FLIPPER_WIDTH = 20
FLIPPER_HEIGHT = 100
BALL_RADIUS = 15

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball Game")

# Create left flipper
left_flipper_pivot = [WIDTH // 4, HEIGHT - 20]
left_flipper_angle = 0
left_flipper_length = FLIPPER_HEIGHT
left_flipper_rotation_speed = 5

# Create right flipper
right_flipper_pivot = [WIDTH * 3 // 4, HEIGHT - 20]
right_flipper_angle = 0
right_flipper_length = FLIPPER_HEIGHT
right_flipper_rotation_speed = -5

# Create ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, -5]

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left_flipper_angle += left_flipper_rotation_speed
    if keys[pygame.K_RIGHT]:
        left_flipper_angle -= left_flipper_rotation_speed

    if keys[pygame.K_a]:
        right_flipper_angle += right_flipper_rotation_speed
    if keys[pygame.K_d]:
        right_flipper_angle -= right_flipper_rotation_speed

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check collisions with walls
    if ball_pos[0] - BALL_RADIUS < 0 or ball_pos[0] + BALL_RADIUS > WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Check collision with left flipper
    left_flipper_rect = pygame.Rect(left_flipper_pivot[0], left_flipper_pivot[1], FLIPPER_WIDTH, left_flipper_length)
    if left_flipper_rect.collidepoint(ball_pos[0], ball_pos[1]):
        ball_speed[1] = -abs(ball_speed[1])

    # Check collision with right flipper
    right_flipper_rect = pygame.Rect(right_flipper_pivot[0] - FLIPPER_WIDTH, right_flipper_pivot[1], FLIPPER_WIDTH, right_flipper_length)
    if right_flipper_rect.collidepoint(ball_pos[0], ball_pos[1]):
        ball_speed[1] = -abs(ball_speed[1])

    # Draw everything
    screen.fill(BACKGROUND_COLOR)

    # Draw left flipper
    pygame.draw.line(screen, FLIPPER_COLOR, left_flipper_pivot,
                     (left_flipper_pivot[0] + left_flipper_length * math.cos(math.radians(left_flipper_angle)),
                      left_flipper_pivot[1] - left_flipper_length * math.sin(math.radians(left_flipper_angle)) ),
                     FLIPPER_WIDTH)

    # Draw right flipper
    pygame.draw.line(screen, FLIPPER_COLOR, right_flipper_pivot,
                     (right_flipper_pivot[0] + right_flipper_length * math.cos(math.radians(right_flipper_angle)),
                      right_flipper_pivot[1] - right_flipper_length * math.sin(math.radians(right_flipper_angle))),
                     FLIPPER_WIDTH)

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
