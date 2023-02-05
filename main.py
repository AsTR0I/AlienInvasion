import sys # Модуль sys предоставляет программисту набор функций, которые дают информацию о том, как интерпретатор Python взаимодействует с операционной системой.
import pygame  # Pygame — это «игровая библиотека», набор инструментов, помогающих программистам создавать игры.
# К ним относятся: Графика и анимация / Звук (включая музыку) / Управление (мышь, клавиатура, геймпад и так далее)
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


# Создание окна
class AlienInvasion():
    # класс для поведения ресурсами и поведения игры
    def __init__(self):
        pygame.init()
        # присваиваем
        self.start_time = time.monotonic()
        # присваиваем  self.screen класс screen
        # присваимваем  self.settings класс Settings()
        self.settings = Settings()
        # задаём настройки экрна от класса Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def run_game(self):
        # Запуск основного цикла
        while True:
            # отслеживание событий клавиатуры и мыши
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_alien()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f'\nПроизошёл выход из игры\nВремя в игре: {int(time.monotonic() - self.start_time)}с')  # выводим в консоле при закрытии
                sys.exit()
                # Отслеживание клавиатуры
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        # Реагирует на нажатие клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_SPACE:
                self.fire_bullet()
            # клвиша для вызодаа из игры
            elif event.key == pygame.K_ESCAPE:
                print(f'\nПроизошёл выход из игры\nВремя в игре: {int(time.monotonic() - self.start_time)}с')
                sys.exit()

    def _check_keyup_event(self, event):
        # Реагирует на отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.ship.moving_right = False


    def fire_bullet(self):
        '''Отправка пули'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        #обновляет позиции снарядов
        self.bullets.update()

        # Удаление старых снарядов
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            if len(self.bullets) == 0:
                print(f'Длина снаряда = {len(self.bullets)},снаряд был удалён')
            # alien hit test
            # if hit then delite bullet and alien
            collision = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)
            print(self.bullets, self.aliens,)

    def _create_alien(self,alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    def _create_fleet(self):
        """Создание флота вторжения"""
        # alien creation
        # Создание пришельца и вычмисления кол-ва пришельцев в ряду
        # Интервал между соседними пришельцами = ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """ определяет кол-во рядов, помещающихся наа экран"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #создание флота вторжения
        for row_number in range(number_rows):
            # Python set add() - это встроенная функция, которая используется для добавления элемента в любой набор.
            for alien_number in range(number_aliens_x):
                # создание пришельца и размещения его в ряду
                self._create_alien(alien_number, row_number)

    def _update_alien(self):
        # updating all aliens position on the fleet
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self):
        # reacting to the edges
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #lowers the fleet and change fleet direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= - 1
    def _update_screen(self):
        '''Обновление экрана'''
        # При каждом проходе цикла перерисовывает экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Чтобы пришелец появился наа экране, программа вызывает метод draw()
        self.aliens.draw(self.screen)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()




if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
