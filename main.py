import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors Â 

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player and obstacle properties
player_size = 30
player_x = screen_width // 2
player_y = screen_height - player_size
player_vel = 5

obstacle_size = 20
obstacle_speed = 5
obstacles = []

# Game loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel 

    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_vel

    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_vel

    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_vel
