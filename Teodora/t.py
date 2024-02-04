import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Score Display Example")

# Set up the font
font = pygame.font.Font(None, 36)  # You can customize the font and size

# Set up the score variable
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the score (you can replace this with your game logic)
    score += 1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render the score
    score_text = font.render("{}".format(score), True, (0, 0, 0))  # Black text

    # Get the rect of the text surface
    score_rect = score_text.get_rect()

    # Position the score on the screen (e.g., top-left corner)
    score_rect.topleft = (10, 10)

    # Blit the score surface onto the screen
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
