"""
Computational Physics: Interactive Bouncing Ball Simulation
-------------------------------------------------------------
"""

import pygame

pygame.init()

# CONSTANTS

WIDTH, HEIGHT = 1100, 720

clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Bouncing Ball Simulation")

FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)

ball_radius = 30

ball_x = WIDTH//2
ball_y = WIDTH//100

velocity_y = 0
gravity = 0.5
bounce = 0.5
floor_y = HEIGHT - ball_radius

running = True

# Main loop
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velocity_y += gravity
    ball_y += velocity_y

    # Bounce off the floor
    if ball_y >= floor_y:
        ball_y = floor_y
        velocity_y = -velocity_y * bounce

        # Stop tiny, endless bounces
        if abs(velocity_y) < 1:
            velocity_y = 0
    


    SCREEN.fill(BLACK)
    pygame.draw.circle(SCREEN,WHITE,(ball_x,ball_y),ball_radius)
    pygame.display.flip()

pygame.quit()
