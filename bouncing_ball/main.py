"""
Computational Physics: Interactive Bouncing Ball Simulation
-------------------------------------------------------------
"""

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1100, 720
FPS = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Bouncing Ball Simulation")

BLACK = (0,0,0)
WHITE = (255,255,255)

ball_radius = 20

ball_x = WIDTH//2
ball_y = HEIGHT//2
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_x += ball_speed_x
    ball_y += ball_speed_y


    if ball_x-ball_radius <0 or ball_x + ball_radius>WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y-ball_radius <0 or ball_y + ball_radius>HEIGHT:
        ball_speed_y = -ball_speed_y

    SCREEN.fill(BLACK)
    pygame.draw.circle(SCREEN,WHITE,(ball_x,ball_y),ball_radius)
    pygame.display.flip()

    clock.tick(60)

