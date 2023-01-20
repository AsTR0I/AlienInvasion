import sys #Модуль sys предоставляет программисту набор функций, которые дают информацию о том, как интерпретатор Python взаимодействует с операционной системой.
import pygame #Pygame — это «игровая библиотека», набор инструментов, помогающих программистам создавать игры.
# К ним относятся: Графика и анимация / Звук (включая музыку) / Управление (мышь, клавиатура, геймпад и так далее)

from settings import Settings
from ship import Ship

#Создание окна
class  AlienInvasion():
     #класс для поведения ресурсами и поведения игры
    def __init__(self):
        pygame.init()
        # присваимваем  self.settings класс Settings()
        self.settings = Settings()
        # задаём настройки экрна от класса Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)

        #флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def run_game(self):
        # Запуск основного цикла
        while True:
            # отслеживание событий клавиатуры и мыши
            self._check_events()
            self._update_screen()
            self.ship.update()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('end')  # выводим в консоле при закрытии
                sys.exit()

                #Отслеживание клавиатуры
                # стрелочка вправо
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                    print(self.ship.rect.x)

            elif event.type == pygame.KEYUP:
                # пока корабль влево > 0, мы даём ему двигаться
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False


                # стрелочка влево
            if event.type == pygame.KEYDOWN:
                print(self.ship.rect.x)
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _update_screen(self):
        '''Обновление экрана'''
        # При каждом проходе цикла перерисовывает экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == "__main__":
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()