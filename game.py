import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cat = pygame.image.load("assets/cat_sprite.png")
cat = pygame.transform.scale(cat, (50, 50))
cat_x, cat_y = 50, 300
velocity_y = 0
gravity = 0.6
jump_power = -10
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity_y = jump_power  # Tap to jump

    velocity_y += gravity
    cat_y += velocity_y
    screen.blit(cat, (cat_x, cat_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

