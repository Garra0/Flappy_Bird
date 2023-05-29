# imports
import pygame
from sys import exit
import random

pygame.init()

# Screen
# -size
x = 1000
y = 600
# -make screen
screen = pygame.display.set_mode((x, y))
# -screen title
pygame.display.set_caption("flappy Bird")


# add clock to timing the speed
clock = pygame.time.Clock()


# load the sky , ground and text
sky = pygame.image.load('images/background/Sky.png').convert()#sky
ground = pygame.image.load('images/background/ground.png').convert()#ground
font = pygame.font.Font('font/Pixeltype.ttf', 20)#text

ground_index = ground.get_rect(bottomleft=(0, y))# ground index + info folder about 'bottomleft'
text = font.render('Osama shalabi',False,'Black')# text style


# load bird :birdDown,birdUp
bird_down = pygame.image.load('images/bird/bird_down.png').convert_alpha()
# the image info size:2343x1592 , div 30 = 78x53
bird_down = pygame.transform.scale(bird_down,(78, 53))#give the bird size
bird_index = bird_down.get_rect(bottomleft=(x/3, y/2-100))

bird_up = pygame.image.load('images/bird/bird_up.png').convert_alpha()
# the image info size:2343x1592 , div 30 = 78x53
bird_up = pygame.transform.scale(bird_up,(78, 53))#give the bird size
# bird_index = bird_up.get_rect(bottomleft=(x/3-100, y/2-100))



# load pillars
pillar_down = pygame.image.load('images/pillar/pillar_down.png').convert_alpha()
pillar_up = pygame.image.load('images/pillar/pillar_up.png').convert_alpha()

# pirral size , get_size()[0] = x - get_size()[1] = y
pirral_x, pirral_y = pillar_down.get_size()[0], pillar_down.get_size()[1]
# dimensions the image new size (x*y)
pillar_down = pygame.transform.scale(pillar_down,(pirral_x/2, pirral_y))
pillar_up = pygame.transform.scale(pillar_up,(pirral_x/2, pirral_y))


# make list of pillars size 4:
# make the rect 'where the pillar start?'
# space between pillars 120 , More than twice the height of the bird
start_down = pillar_down.get_rect(midbottom=(800, 70))
start_up = pillar_up.get_rect(midtop=(800, 190))

# make list for the down pillar
pillar_down_index =[]
for i in range(0,4):
    # 30m to know that , i must use 'copy()' thanks chat GPT.
    pillar_down_index.append(start_down.copy())
    start_down.x+=250

# make list for the up pillar
pillar_up_index =[]
for i in range(0,4):
    pillar_up_index.append(start_up.copy())
    start_up.x+=250


while True:
    for event in pygame.event.get():
        # if you close the screen , then the event will stop the run and end the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame


    # use sky,ground,text,bird,pillar
    screen.blit(sky, (0,0))
    screen.blit(ground, ground_index)
    screen.blit(text,(0,100))
    screen.blit(bird_down,bird_index)#down
    # screen.blit(bird_up,bird_index)#up


    # display the pirllar and the space moving in y 70-400 = 370 random number
    for i in range(0, 4):
        screen.blit(pillar_down, pillar_down_index[i])
        screen.blit(pillar_up, pillar_up_index[i])

    # 2 commits for no one:
    # -useless loop ,but y know:...
    # -for down,up in zip(pillar_down_index,pillar_up_index):

    # pillar shift decrease
    for i in range(0,4):
        pillar_down_index[i].x-=4
        pillar_up_index[i].x-=4

    # restart the pillars when leave the screen
    for i in range(0,4):
        s = random.randint(70, 320)
        if pillar_down_index[i].x <= 0:
            pillar_down_index[i].bottom= s
            pillar_down_index[i].x=1000
            # pillar_down_index[i].y += s

        if pillar_up_index[i].x <= 0:
            pillar_up_index[i].y = s+120
            pillar_up_index[i].x=1000
            # pillar_up_index[i].y += s




    # bird_index.y+=6

#     if snail_rect.right <=0: snail_rect.x=800
#
#     screen.blit(snail_surf,snail_rect)
#     screen.blit(player_surf, player_rect)


    pygame.display.update()#to display the frames and new events
    clock.tick(60)# the speed

