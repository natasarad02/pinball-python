import pygame
import sys
import random
import subprocess
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Space Flipper")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (147, 112, 219)  # Purple color for the title

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.SysFont('impact', 120, bold=True)

# Load images and resize them
background_image = pygame.transform.scale(pygame.image.load("space_background.jpg"), (WIDTH, HEIGHT))
planet_image = pygame.transform.scale(pygame.image.load("planet.png"), (250, 250))
moon_image = pygame.transform.scale(pygame.image.load("moon.png"), (100, 100))
rocket_image = pygame.transform.scale(pygame.image.load("rocket.png"), (100, 100))
jupiter_image = pygame.transform.scale(pygame.image.load("jupiter.png"), (200, 200))
saturn_image = pygame.transform.scale(pygame.image.load("saturn2.png"), (330, 180))
text_image = pygame.transform.scale(pygame.image.load("Untitled.png"), (650, 350))

# Button dimensions
button_width, button_height = 250, 50
button_margin = 20

# Button positions
button_positions = [
    (WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height - button_margin),
    (WIDTH // 2 - button_width // 2, HEIGHT // 2),
    (WIDTH // 2 - button_width // 2, HEIGHT // 2 + button_height + button_margin),
    (WIDTH // 2 - button_width // 2, HEIGHT // 2 + 2 * (button_height + button_margin)),
]

# Button labels and corresponding file names
button_labels = ["Simulacija gravitacije", "Prvobitno odbijanje", "Prva verzija flipera", "Fliper Level 1"]
file_names = ["gravitacija.py", "Prvobitno_odbijanje.py", "Medjukorak_flipera.py", "flipper.py"]

# Star positions
stars = [(random.randint(0, WIDTH + 100), random.randint(0, HEIGHT + 100)) for _ in range(1500)]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Check if a button is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, pos in enumerate(button_positions):
                x, y = pos
                if x < mouse_x < x + button_width and y < mouse_y < y + button_height:
                    # Execute the corresponding file in a new process
                    file_name = file_names[i]
                    try:
                        subprocess.Popen(["python", file_name])
                    except FileNotFoundError:
                        print(f"Error: {file_name} not found.")

    # Draw background (black)
    screen.fill(BLACK)

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)

    # Draw planets
    screen.blit(planet_image, (WIDTH * 0.1, HEIGHT // 4))
    screen.blit(saturn_image, (3 * WIDTH // 4 - 100, 3 * HEIGHT // 4 - 100))
    screen.blit(jupiter_image, (WIDTH * 0.9, HEIGHT // 8))
    # Draw moon
    screen.blit(moon_image, (WIDTH // 2 + 270, HEIGHT // 2 - 370))

    # Draw rocket
    screen.blit(rocket_image, (WIDTH // 5, HEIGHT // 2 + 250))
    text_image_rect = text_image.get_rect(center=(WIDTH // 2, HEIGHT // 4.5))
    screen.blit(text_image, text_image_rect.topleft)

    # Draw buttons
    # Draw buttons
    for i, pos in enumerate(button_positions):
        x, y = pos
        button_color = (0, 102, 204) #blue
        if i == len(button_positions) - 1:  # Check if it's the last button
            button_color = (255, 20, 147)  # Change the color to a different shade of pink for the last button
        pygame.draw.rect(screen, button_color, (x, y, button_width, button_height))
        text = font.render(button_labels[i], True, WHITE)
        screen.blit(text, (x + button_width // 2 - text.get_width() // 2, y + button_height // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()