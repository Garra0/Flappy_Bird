# imports
import pygame
from sys import exit
import random
from settings import Settings
def display_score():
    # get_ticks is number of clocks
    # after div by 1k that make seconds
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    # f'{current_time}' to change current_time to string
    # (64,64,64) is the color (R,B,G)
    score = font.render(f'Score: {current_time}' , False,(64,64,64))
    # score place in the screen
    score_Index = score.get_rect(center=(x-120, 50))
    screen.blit(score, score_Index)

pygame.init()

# would I use classes and functions?  I will think other time...
sett = Settings()

# width and hight the screen
x=1000
y=600
# -make screen
screen = pygame.display.set_mode((sett.screen_width,sett.screen_height))
# -screen title
pygame.display.set_caption("flappy Bird")



# add clock to timing the speed
clock = pygame.time.Clock()


# load the sky , ground and text
sky = pygame.image.load('images/background/Sky.png').convert()#sky
ground = pygame.image.load('images/background/ground.png').convert()#ground
font = pygame.font.Font('font/Pixeltype.ttf', 50)#text

sky_index = sky.get_rect(midtop=(0, 0))# sky index + info folder about 'top'
# texts
ground_index = ground.get_rect(bottomleft=(0, y))# ground index + info folder about 'bottomleft'
score = font.render('Osama shalabi',False,'Black')# text style
score_index = score.get_rect(center=(x-100,46))

# load bird :birdDown,birdUp
bird_down = pygame.image.load('images/bird/bird_down.png').convert_alpha()
# the image info size:2343x1592 , div 30 = 78x53
bird_down = pygame.transform.scale(bird_down,(78, 53))#give the bird size
# bird_down = pygame.transform.rotozoom(bird_down, -20, 1)
bird_index = bird_down.get_rect(bottomleft=(x/3, y/2-100))

bird_up = pygame.image.load('images/bird/bird_up.png').convert_alpha()
bird_up=pygame.transform.scale(bird_up,(78, 53))

# the image info size:2343x1592 , div 30 = 78x53
bird_died = pygame.transform.rotozoom(bird_up, 180, 2)
bird_died = pygame.transform.scale(bird_died,(78*2, 53*2))#give the bird size
bird_up_index = bird_died.get_rect(center=(x/2,y-30))




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
# space between pillars 160 , More than twice the height of the bird
start_down = pillar_down.get_rect(midbottom=(800, 30))
start_up = pillar_up.get_rect(midtop=(800, 210))

# make lists for the down and up pillars
pillar_down_index =[]
pillar_up_index =[]

for i in range(0, 4):
    # 30m to know that , i must use 'copy()' thanks chat GPT.
    pillar_down_index.append(start_down.copy())
    pillar_up_index.append(start_up.copy())
    # 1- the space between the pillars in the list...
    start_down.x += 250 + pirral_x / 4
    start_up.x += 250 + pirral_x / 4

    # 2- the space between the top and bot pillars in y position...
    s = random.randint(30, 320)
    # use the 'botton' Important because the top pillar will end in it
    pillar_down_index[i].bottom = s
    # wrong line:
    # pillar_down_index[i].y += s
    pillar_up_index[i].y = s + 180

# to let the bird fly when there event
bird_gravity = 0
# the game avtive flag
game_active = True
start_time = 0

# text when bird lose
game_start = font.render('Flappy Bird', False, (111, 196, 169))
game_start_index = game_start.get_rect(center=(x/2,120))

# list of hearts
heart = pygame.image.load('images/heart/heart.png').convert_alpha()
heart_x, heart_y = heart.get_size()[0]/25, heart.get_size()[1]/25
heart = pygame.transform.scale(heart,(heart_x, heart_y))

# dimensions the image new size (x*y)



def display_inActive():
    # display the sky
    screen.blit(sky, (0, 0))
    # display the ground
    screen.blit(ground, ground_index)

        # pillars:

    # display the pirllar list
    for i in range(0, 4):
        screen.blit(pillar_down, pillar_down_index[i])
        screen.blit(pillar_up, pillar_up_index[i])

    # 2 commits for nothing and no one :
    # -useless loop ,but y know:...
    # for down,up in zip(pillar_down_index,pillar_up_index):

    # pillar shift decrease
    for i in range(0, 4):
        pillar_down_index[i].x -= 3
        pillar_up_index[i].x -= 3

    # restart the pillars when its leave the screen
    for i in range(0, 4):
        s = random.randint(30, 320)
        if pillar_down_index[i].x <= 0 - pirral_x / 2:
            pillar_down_index[i].bottom = s
            pillar_down_index[i].x = 1000
            # pillar_down_index[i].y += s

        if pillar_up_index[i].x <= 0 - pirral_x / 2:
            pillar_up_index[i].y = s + 180
            pillar_up_index[i].x = 1000
            # pillar_up_index[i].y += s

            #score:
        # background color for the score:
        pygame.draw.rect(screen, 'Pink', score_index)

        # display hearts
        for i in range(0, hearts_count):
            screen.blit(heart, (10+i*heart_x,10))

        # display the bird
        if bird_flying:
            screen.blit(bird_up, bird_index)
        else:
            screen.blit(bird_down, bird_index)

        # display score
        display_score()

# after the collision we will ReEquipment the round if the heats didnot end
def RoundـReEquipment(pillar_down_index,pillar_up_index):
    # ReEquipment the pillars and bird positions
    for i in range(0, 4):
        s = random.randint(30, 320)
        pillar_down_index[i].bottom = s
        pillar_down_index[i].x += 750
        # pillar_down_index[i].y += s

        pillar_up_index[i].y = s + 180
        pillar_up_index[i].x += 750
        # pillar_up_index[i].y += s






while True:
    # hearts count
    hearts_count =3
    # to dont use RoundـReEquipment fun more than one time in one collision
    f = False
    while hearts_count > 0:
        # will be true after use the space key
        bird_flying = False


        # events
        for event in pygame.event.get():
            # if you close the screen , then the event will stop the run and end the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if game run , then we have events
            if game_active:
                # mouse or space click , let the bird fly
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bird_gravity -= 7
                    # when use space and the bird not above the screen
                if event.type == pygame.KEYDOWN and bird_index.top > sky_index.top:
                    if event.key == pygame.K_SPACE:
                        bird_gravity -= 7
                        bird_flying = True
                        

            # to let the game active again just press L_SPACE
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    # give start_time number to reset the score time
                    start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            # when the game active the screen will display :
            display_inActive()




            # bird down 0.3 every clock
            bird_gravity += 0.3
            bird_index.y += bird_gravity
            # if bird touch the ground or try fly above the screen :
            if bird_index.bottom >= ground_index.top:
                bird_index.bottom = ground_index.top



            # screen.blit(bird_down, bird_index)  # down
            # # screen.blit(bird_up,bird_index)#up

            # if happen colliderect
            for i in range(0, 4):
                # if happen collision between bird and pillars or ground
                if bird_index.colliderect(pillar_down_index[i]) or \
                        bird_index.colliderect(pillar_up_index[i]) or \
                        bird_index.bottom >= ground_index.top:
                    # stop the game, when there are no more frames to display
                    game_active = False
                    f=True
        else:
            screen.fill((94, 129, 162))
            screen.blit(bird_up, bird_up_index)
            screen.blit(game_start, game_start_index)
            # f -> to dont use RoundـReEquipment fun more than one time in one collision
            if hearts_count > 1 and f:
                hearts_count -= 1
                f=False
                RoundـReEquipment(pillar_down_index,pillar_up_index)

        pygame.display.update()  # to display the frames and new events
        clock.tick(60)  # the speed

    




