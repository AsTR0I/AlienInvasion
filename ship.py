import pygame

class Ship:
    #класс для упрааваления кораблём
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #загружает изобраажение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #каждый новвый корабль полявляется у нижнего края экрана
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        #рисует корабль в текущей позиции
        self.screen.blit(self.image,self.rect)

    def update(self):
        # обновляет позицию корабля с учетом флага
        if self.moving_right == True:
            self.rect.x += 1

        if self.moving_left == True:
            self.rect.x -= 1