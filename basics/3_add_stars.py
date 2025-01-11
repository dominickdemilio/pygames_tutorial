# Example file showing a circle moving on display_surface
import pygame
from random import randint

# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

# create a surface
spaceship_surf = pygame.image.load(
    "basics/assets/spaceship.png"
).convert_alpha()  # function to make the game run faster
spaceship_x = 10

# create star surface
star_surf = pygame.image.load("basics/assets/star.png").convert_alpha()

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    display_surface.blit(spaceship_surf, (spaceship_x, 150))
    spaceship_x += 0.1
    for i in range(20):
        display_surface.blit(
            star_surf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
        )

    # update the display
    pygame.display.update()

pygame.quit()
