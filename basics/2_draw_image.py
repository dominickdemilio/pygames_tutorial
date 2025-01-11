# Example file showing a circle moving on display_surface
import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

# create a surface
spaceship_surf = pygame.image.load(
    "basics/assets/spaceship.png"
).convert_alpha()  # function to make the game run faster

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    display_surface.blit(spaceship_surf, (100, 150))
    pygame.display.update()

pygame.quit()
