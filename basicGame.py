import pygame

pygame.init()
# Creating Screen for Our Game
screen = pygame.display.set_mode((600,600))

# Creating Colour Variable 
white = 255,255,255
black = 0,0,0
red = 255,0,0

# variable for Player 
x=20

#Clock For Game
clock = pygame.time.Clock()

running  = True

def keypressFuntion():
    if event.type == pygame.K_UP:
        for i in range(0,600):
            player = x+i

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white) #To giving background to our screen

    #Render Your Game Here

    pygame.display.update()

    clock.tick(60) # limits FPS to 60

pygame.quit()
quit()