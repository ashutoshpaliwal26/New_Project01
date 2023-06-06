''' Creatin a basic Snake Game '''

import pygame
import random

pygame.init()
# Creating Screen for Our Game
screen = pygame.display.set_mode((800,800))

# Giving Title To our Game.
Title = pygame.display.set_caption("Snakey PY")

# Creating Colour Variable 
white = 255,255,255
black = 0,0,0
red = 255,0,0

# variable for Snake 
player_x = 60
player_y = 40
velocity_x = 0
velocity_y = 0

# Variables for food 
food_x = random.randint(0,800)
food_y = random.randint(0,800)
score = 0

#Clock For Game
clock = pygame.time.Clock()

running  = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Giving Keyboard responce to our Game. 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                velocity_x =+  10
                velocity_y = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                velocity_x =- 10
                velocity_y = 0
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                velocity_x = 0
                velocity_y =- 10
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                velocity_x = 0
                velocity_y =+ 10
    
    
    # Giving Velocity to our snake.
    player_x = player_x + velocity_x
    player_y = player_y + velocity_y

    screen.fill(white) #To giving background to our screen

    #Render Your Game Here
    pygame.draw.rect(screen, black,[player_x, player_y,20,20])
    pygame.display.update()

    clock.tick(60) # limits FPS to 60

pygame.quit()
quit()