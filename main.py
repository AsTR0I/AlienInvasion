import sys #Модуль sys предоставляет программисту набор функций, которые дают информацию о том, как интерпретатор Python взаимодействует с операционной системой.

import pygame #Pygame — это «игровая библиотека», набор инструментов, помогающих программистам создавать игры.
# К ним относятся: Графика и анимация / Звук (включая музыку) / Управление (мышь, клавиатура, геймпад и так далее)

from settings import Settings
#Создание окна
class  AlienInvasion:
     #класс для поведения ресурсами и поведения игры
    def __init__(self):
        pygame.init()
        # присваимваем  self.settings класс Settings()
        self.settings = Settings()
        # задаём наастройки экрна от класса Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)


    def rin_game(self):
        # Запуск основного цикла
        while True:
            # отслеживание соббытий клаавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('end') # выводим в консоле при закрытии
                    sys.exit()
            # При каждом проходе цикла перерисовывает экран
            self.screen.fill(self.settings.bg_color)
            # Отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == "__main__":
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.rin_game()
