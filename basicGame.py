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
blue = 0,0,255

# variable for Snake 
player_x = 20
player_y = 20
velocity_x = 0
velocity_y = 0
inti_velocity = 5

# Variables for food 
food_x = random.randint(0,780)
food_y = random.randint(0,780)
score = 0

#Clock For Game
clock = pygame.time.Clock()

running  = True

# Function for Text Rendering on screen
fontsize = 20
def RenderText(text, color, x, y, fsize):
    Font = pygame.font.SysFont(None, fsize)
    screen_text = Font.render(text, True, color)
    screen.blit(screen_text, (x, y))


#Snake Length Variables 
snk_list = []
snk_length = 1

GameOver = False


def plot(Screen, color, coordinate_list , size):
    for x, y in coordinate_list:
        pygame.draw.rect(Screen, color,[x, y, size, size])
    pass
    

while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        # Giving Keyboard responce to our Game. 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                velocity_x =+  inti_velocity
                velocity_y = 0
                # player_x += 20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                velocity_x =- inti_velocity
                velocity_y = 0
                # player_x =- 20
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                velocity_x = 0
                velocity_y =- inti_velocity
                # player_y =+ 20
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                velocity_x = 0
                velocity_y =+ inti_velocity
                # player_y =- 200
        
        


    # Giving Velocity to our snake.
    player_x = player_x + velocity_x
    player_y = player_y + velocity_y

    if abs(player_x - food_x)<20 and abs(player_y - food_y)<20:
            score = score + 1
            print("Score : ", score)
            food_x = random.randint(0,800)
            food_y = random.randint(0,800)
            snk_length += 5
            if (score%5) == 0:
                inti_velocity = inti_velocity+1
                print("Increasing Velocity.................")

      

    screen.fill(white) #To giving background to our screen
    RenderText("Score : " + str(score*10), blue, 10, 10, 20)

    # Creatin Snake's Head
    head = []
    head.append(player_x)
    head.append(player_y)
    snk_list.append(head) 

    if len(snk_list)  > snk_length :
        del snk_list[0]

    #Render Your Game Here
    pygame.draw.rect(screen, red , [food_x, food_y, 20 ,20])
    # pygame.draw.rect(screen, black,[player_x, player_y,20,20])
    plot(screen, black, snk_list, 20)
    pygame.display.update()

    clock.tick(60) # limits FPS to 60

pygame.quit()
quit()