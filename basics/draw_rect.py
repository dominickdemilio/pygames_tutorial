# Example file showing a circle moving on display_surface
import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

# create a surface
surf = pygame.Surface((200, 100))
surf.fill("blue")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    display_surface.blit(surf, (100, 150))
    pygame.display.update()

pygame.quit()
