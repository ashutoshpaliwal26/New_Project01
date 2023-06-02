''' Creatin a basic Snake Game '''

import pygame

pygame.init()
# Creating Screen for Our Game
screen = pygame.display.set_mode((600,600))

# Giving Title To our Game.
Title = pygame.display.set_caption("Snakey PY")

# Creating Colour Variable 
white = 255,255,255
black = 0,0,0
red = 255,0,0

# variable for Player 
player_x = 60
player_y = 40

#Clock For Game
clock = pygame.time.Clock()

running  = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Giving Keyboard responce to our Game. 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                player_x = player_x + 20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                player_x = player_x - 20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                player_y = player_y - 20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN :
                player_y = player_y + 20
        
    screen.fill(white) #To giving background to our screen

    #Render Your Game Here
    pygame.draw.rect(screen, black,[player_x, player_y,20,20])
    pygame.display.update()

    clock.tick(60) # limits FPS to 60

pygame.quit()
quit()