import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Класс для управления снарядами выпущенными корабблем """

    def __init__(self, ai_game):
        """ Создаёт обьект снаряд в текущей позиции корабля """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        #Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Позиция снарядаа хранится в вещественном формаате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд в вверх"""
        # обновляем позицию снаряда
        self.y += self.settings.bullet_speed
        # обновляем положение снаряда
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовывает снаряд"""
        pygame.draw.rect(self.screen, self.color, self.rect)
