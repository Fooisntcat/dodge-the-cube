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

    # Generate obstacles
    if random.randint(0, 100) < 5:
        obstacles.append([screen_width, random.randint(0, screen_height - obstacle_size)])

    # Move obstacles and check for collisions
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
        if player_x + player_size > obstacle[0] and player_x < obstacle[0] + obstacle_size:
            if player_y + player_size > obstacle[1] and player_y < obstacle[1] + obstacle_size:
                running = False
        if obstacle[0] < 0:
            obstacles.remove(obstacle)
            score += 1

    # Fill the screen with white
    screen.fill(white)

    # Draw the player and obstacles
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update() 
