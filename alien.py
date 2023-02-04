import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Класс, представляющий одного пришельца'''
    def __init__(self, ai_game):
        '''Инициализация пришельца и задаём его начальную позицию'''
        super(Alien, self).__init__()
        self.screen = ai_game.screen

        # Загрузка изображения
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every new alien born in left - top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтаальной позиции пришельца
        self.x = float(self.rect.x)