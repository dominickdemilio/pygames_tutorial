# Example file showing a circle moving on display_surface
import pygame
from random import randint


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "basics/assets/spaceship.png"
        ).convert_alpha()
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300

    def update(self, dt):
        self.rect.center += self.direction * self


# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()

# create spaceship
spaceship = Spaceship(all_sprites)

# create surfaces
star_surf = pygame.image.load("basics/assets/star.png").convert_alpha()
star_positions = [
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)
]

meteor_surf = pygame.image.load("basics/assets/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
)

laser_surf = pygame.image.load("basics/assets/laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# game loop
while running:
    dt = clock.tick(60) / 1000

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get wasd input
    keys = pygame.key.get_pressed()

    spaceship.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    spaceship.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    spaceship.direction = (
        spaceship.direction.normalize()
        if spaceship.direction.length() > 0
        else spaceship.direction
    )

    # get spacebar input
    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
        print("Pew pew!")

    # draw the main surface
    display_surface.fill("darkgray")

    # draw stars
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # draw meteor
    display_surface.blit(meteor_surf, meteor_rect)

    # draw laser
    display_surface.blit(laser_surf, laser_rect)

    # move the spaceship
    spaceship.rect.center += spaceship.direction * spaceship.speed * dt

    # draw the spaceship
    all_sprites.draw(display_surface)

    # update the display
    pygame.display.update()

pygame.quit()
