import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravitational Pull Example")

# Ball properties
ball_radius = 20
ball_color = (255, 0, 0)
ball_pos = [width // 2, 0]
ball_velocity = [0, 0]

# Gravitational force
gravity = 0.5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key input for controlling the ball (optional)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_velocity[0] -= 1
    if keys[pygame.K_RIGHT]:
        ball_velocity[0] += 1
    if keys[pygame.K_UP]:
        ball_velocity[1] -= 1
    if keys[pygame.K_DOWN]:
        ball_velocity[1] += 1

    # Update ball position based on velocity
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Apply gravitational force
    ball_velocity[1] += gravity

    # Draw the background
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
