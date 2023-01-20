class Settings:
    # Класс для хранения настроек игры Alien invasion

    def __init__(self):
        #инициаализирует наастройки игры

        #параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,100,255)
        # Заголовок экрана
        self.caption = 'AliensWar'
        # ship speed
        self.ship_speed = 1.5
