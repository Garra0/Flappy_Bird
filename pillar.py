# import pygame
# from pygame.sprite import Sprite
#
# class Pillar(Sprite):
#     def __init__(self,screen,ai_settings):
#         super(Alien,self).__init__()
#         self.screen=screen
#         self.image=pygame.image.load("images/alien.png")
#         self.rect=self.image.get_rect()
#         self.screen_rect=self.screen.get_rect()
#         self.rect.left=self.screen_rect.left+self.rect.width
#         self.rect.top=self.screen_rect.top+ self.rect.height
#         self.x=self.rect.x
#         self.ai_settings=ai_settings
#
#     def update(self):
#         self.x+=(self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
#         self.rect.x=self.x
#
#     def check_edges(self):
#         screen_rect=self.screen.get_rect()
#         if self.rect.right>=self.screen_rect.right:
#             return True
#         elif self.rect.left<=0:
#             return True
#
#
#
#     def draw(self):
#         self.screen.blit(self.image,self.rect)
#
#
