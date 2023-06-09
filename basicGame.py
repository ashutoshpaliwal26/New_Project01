''' Creatin a basic Snake Game '''

import pygame
import random

pygame.init()
# Creating Screen for Our Game
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# Function for Text Rendering on screen
def RenderText(text, color, x, y, fsize):
    Font = pygame.font.SysFont(None, fsize)
    screen_text = Font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Giving Title To our Game.
Title = pygame.display.set_caption("Snake PY")

def welcome():
    exit_game = False
    green = 2,99,12
    white = 255,255,255
    bg = 242, 85, 68
    black = 0,0,0
    screen.fill(bg)
    RenderText("Snake Py", white, 130, 250, 160)
    RenderText("Press ! Space to Play", black, 200, 350, 50)
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():

        
    # Creating Colour Variable 
    white = 255,255,255
    black = 0,0,0
    red = 255,0,0
    green = 2,99,12
    yellow = 230, 250,0
    blue = 0,0,255
    bg = 242, 85, 68

    # variable for Snake 
    player_x = 50
    player_y = 95
    velocity_x = 0
    velocity_y = 0
    inti_velocity = 3

    # Variables for food 
    food_x = random.randint(100,700)
    food_y = random.randint(100,700)
    score = 0

    running  = True



    #Snake Length Variables 
    snk_list = []
    snk_length = 1

    GameOver = False


    def plot(Screen, color, coordinate_list , size):
        for x, y in coordinate_list:
            pygame.draw.rect(Screen, color,[x, y, size, size])
        

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()   

    while running:

        if GameOver:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            screen.fill(bg)
            RenderText("SNAKE PY", blue, 100, 200, 150)
            RenderText("Game Over", red, screen_width/4, 600, 100)
            RenderText("Press Enter ! To Continue", black ,250, 750, 30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                

            if score > int(hiscore) :
                hiscore = score

            

        else:
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
                    score = score + 10
                    food_x = random.randint(0,800)
                    food_y = random.randint(0,800)
                    snk_length += 5
                    if (score%50) == 0:
                        inti_velocity = inti_velocity+1

            

            screen.fill(bg) #To giving background to our screen
            pygame.draw.rect(screen, black, [10, 40, 780,750])
            pygame.draw.rect(screen, bg, [15, 45, 770, 740])
            RenderText("Score : " + str(score), blue, 10, 15, 20)
            RenderText("High Score : " + hiscore, blue, 690, 15, 20)

            # Creatin Snake's Head
            head = []
            head.append(player_x)
            head.append(player_y)
            snk_list.append(head) 

            if len(snk_list)  > snk_length :
                del snk_list[0]

            if (player_x < 15 or player_x > 765) or (player_y < 45 or player_y > 755):
                GameOver = True

            if head in snk_list[:-1]:
                GameOver = True



            #Render Your Game Here
            pygame.draw.rect(screen, red , [food_x, food_y, 20 ,20])
            # pygame.draw.rect(screen, black,[player_x, player_y,20,20])
            plot(screen, black, snk_list, 20)
        pygame.display.update()

        clock.tick(60) # limits FPS to 60

    pygame.quit()
    quit()

welcome()