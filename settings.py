class Settings:
    # Класс для хранения настроек игры Alien invasion

    def __init__(self):
        #инициализирует настройки игры

        #параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,100,255)
        # Заголовок экрана
        self.caption = 'AliensWar'
        # ship speed
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed =-1.5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (255,255,0)
        self.bullet_allowed = 3
        #alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direcrion = 1 - moving to right, -1 to left
        self.fleet_direction = 1 # moving to right