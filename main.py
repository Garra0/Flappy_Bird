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
    score_Index = score.get_rect(center=(x/2, 50))
    screen.blit(score, score_Index)

pygame.init()
sett=Settings()


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

# texts
ground_index = ground.get_rect(bottomleft=(0, y))# ground index + info folder about 'bottomleft'
score = font.render('Osama shalabi',False,'Black')# text style
score_index = score.get_rect(center=(x/2,50))

# load bird :birdDown,birdUp
bird_down = pygame.image.load('images/bird/bird_down.png').convert_alpha()
# the image info size:2343x1592 , div 30 = 78x53
bird_down = pygame.transform.scale(bird_down,(78, 53))#give the bird size
bird_index = bird_down.get_rect(bottomleft=(x/3, y/2-100))

bird_up = pygame.image.load('images/bird/bird_up.png').convert_alpha()
# the image info size:2343x1592 , div 30 = 78x53
bird_up = pygame.transform.rotozoom(bird_up, 180, 2)
bird_up = pygame.transform.scale(bird_up,(78*2, 53*2))#give the bird size
bird_up_index = bird_up.get_rect(center=(x/2,y-30))




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
start_up = pillar_up.get_rect(midtop=(800, 190))

# make list for the down pillar
pillar_down_index =[]
for i in range(0,4):
    # 30m to know that , i must use 'copy()' thanks chat GPT.
    pillar_down_index.append(start_down.copy())
    start_down.x+=250+pirral_x/4

# make list for the up pillar
pillar_up_index =[]
for i in range(0,4):
    pillar_up_index.append(start_up.copy())
    start_up.x+=250+pirral_x/4

# to let the bird fly when there event
bird_gravity = 0
# the game avtive flag
game_active = True
start_time = 0

# text when bird lose
game_start = font.render('Flappy Bird', False, (111, 196, 169))
game_start_index = game_start.get_rect(center=(x/2,120))

while True:
    for event in pygame.event.get():
        # if you close the screen , then the event will stop the run and end the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if game run , then we have events
        if game_active:
            # mouse or space click , let the bird fly
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird_gravity -= 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_gravity -= 7
        # to let the game active again just press L_SPACE
        else:
            if event. type == pygame. KEYDOWN and event. key == pygame. K_SPACE:
                game_active =True
                # give start_time number to reset the score time
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        # use sky,ground,text,bird,pillar
        screen.blit(sky, (0, 0))
        screen.blit(ground, ground_index)
        # background for the score:
        pygame.draw.rect(screen, 'Pink', score_index)
        pygame.draw.rect(screen, 'Pink', score_index, 10)
        # screen.blit(score, score_index)
        display_score()

        # display the pirllar and the space moving in y 30-400 = 410 random number
        for i in range(0, 4):
            screen.blit(pillar_down, pillar_down_index[i])
            screen.blit(pillar_up, pillar_up_index[i])

        # 2 commits for no thing:
        # -useless loop ,but y know:...
        # for down,up in zip(pillar_down_index,pillar_up_index):

        # pillar shift decrease
        for i in range(0, 4):
            pillar_down_index[i].x -= 3
            pillar_up_index[i].x -= 3

        # restart the pillars when leave the screen
        for i in range(0, 4):
            s = random.randint(30, 320)
            if pillar_down_index[i].x <= 0 - pirral_x / 2:
                pillar_down_index[i].bottom = s
                pillar_down_index[i].x = 1000
                # pillar_down_index[i].y += s

            if pillar_up_index[i].x <= 0 - pirral_x / 2:
                pillar_up_index[i].y = s + 160
                pillar_up_index[i].x = 1000
                # pillar_up_index[i].y += s

        bird_gravity += 0.3
        bird_index.y += bird_gravity
        # if bird touch the ground:
        if bird_index.bottom >= ground_index.top: bird_index.bottom = ground_index.top
        screen.blit(bird_down, bird_index)  # down
        # screen.blit(bird_up,bird_index)#up

        # if happen colliderect
        for i in range(0, 4):
            # if happen collision between bird and pillars or ground
            if bird_index.colliderect(pillar_down_index[i]) or\
                    bird_index.colliderect(pillar_up_index[i]) or\
                    bird_index.bottom >= ground_index.top:
                # stop the game, when there are no more frames to display
                game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(bird_up,bird_up_index)
        screen.blit(game_start,game_start_index)

    


    pygame.display.update()#to display the frames and new events
    clock.tick(60)# the speed

