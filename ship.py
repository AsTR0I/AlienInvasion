import pygame
from settings import Settings

class Ship:
    #класс для упрааваления кораблём
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings
        #загружает изобраажение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #каждый новвый корабль полявляется у нижнего края экрана
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)

        # Флаги перемещения корабля
        self.moving_right = False
        self.moving_left = False



    def blitme(self):
        #рисует корабль в текущей позиции
        self.screen.blit(self.image,self.rect)

    def update(self):
        # обновляет позицию корабля с учетом флага
        if self.x <= self.settings.screen_width - 60:
            if self.moving_right == True:
                self.x += self.settings.ship_speed
                print(self.x)
        if self.x >= 0:
            if self.moving_left == True:
                self.x -= self.settings.ship_speed
                print(self.x)
        # обновление атрибута rect на основании self.x
        self.rect.x = self.x