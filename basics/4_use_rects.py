# Example file showing a circle moving on display_surface
import pygame
from random import randint

# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True

# create a surface
spaceship_surf = pygame.image.load(
    "basics/assets/spaceship.png"
).convert_alpha()  # function to make the game run faster
spaceship_rect = spaceship_surf.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
)

# create star surface
star_surf = pygame.image.load("basics/assets/star.png").convert_alpha()
star_positions = [
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)
]

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # move the spaceship
    # if spaceship_rect.right < WINDOW_WIDTH:
    #     spaceship_rect.x += 0.1

    display_surface.blit(spaceship_surf, spaceship_rect)

    # update the display
    pygame.display.update()

pygame.quit()
