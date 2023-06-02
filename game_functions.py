import pygame
import sys



def check_event(ship,bullets):
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_gravity -= 7
        # to let the game active again just press L_SPACE
        else:
            if event. type == pygame. KEYDOWN and event. key == pygame. K_SPACE:
                game_active =True
                # give start_time number to reset the score time
                start_time = int(pygame.time.get_ticks()/1000)




def update_screen(ai_settings,screen,ship,bullets,aliens,sb):
    # screen.fill(ai_settings.bg_color)
    background = pygame.image.load("images/back.jpg")
    background = pygame.transform.scale(background, (ai_settings.screen_width, ai_settings.screen_height))
    screen.blit(background, (0, 0))
    ship.draw()
    bullets.draw(screen)
    update_bullets(bullets,aliens,ai_settings,sb)
    sb.show_score()
    aliens.draw(screen)

    pygame.display.flip()

def create_fleet(ai_settings,screen,aliens,ship):
    alien=Alien(screen,ai_settings)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    available_space_x=ai_settings.screen_width - 2 * alien_width
    alien_number=int(available_space_x/(2 * alien_width))
    available_space_y=(ai_settings.screen_height-( 3 * alien_height) - ship.rect.height)
    number_rows=int(available_space_y/(2 * alien_height))


    for row_number in range (number_rows):
        for a in range(alien_number):
            alien=Alien(screen,ai_settings)
            alien.x=alien_width + 2 * alien_width * a
            alien.rect.x=alien.x
            alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
            aliens.add(alien)


def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
        ai_settings.fleet_direction*=-1


def update_bullets(bullets,aliens,ai_settings,sb):
    for b in bullets:
        if b.rect.top<=0:
            bullets.remove(b)
            print(len(bullets))
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            ai_settings.score+=ai_settings.alien_points
            sb.prep_score()











