import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Класс, представляющий одного пришельца'''
    def __init__(self, ai_game):
        '''Инициализация пришельца и задаём его начальную позицию'''
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Загрузка изображения
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Every new alien born in left - top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтаальной позиции пришельца
        self.x = float(self.rect.x)
    def check_edges(self):
        # return True if alien is near the display edge
        screen_rect = self.screen.get_rect()
        if  self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    def update(self):
        #перемещение прищельцаа вправо
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x