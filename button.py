import pygame


class Button:
    def __init__(self, game):
        self.settings = game.settings

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.r_btn = pygame.image.load("img/rock.png").convert_alpha()
        self.p_btn = pygame.image.load("img/paper.png").convert_alpha()
        self.s_btn = pygame.image.load("img/scissors.png").convert_alpha()
        self.l_btn = pygame.image.load("img/lizard.png").convert_alpha()
        self.sp_btn = pygame.image.load("img/spok.png").convert_alpha()

        # Кнопки
        self.buttons = {
            "rock": {"image": self.r_btn, "rect": None},
            "paper": {"image": self.p_btn, "rect": None},
            "scissors": {"image": self.s_btn, "rect": None},
            "lizard": {"image": self.l_btn, "rect": None},
            "spock": {"image": self.sp_btn, "rect": None},
        }

    def setup_buttons(self):
        """Настройка позиций и размеров кнопок"""
        # Вычисляем позиции для горизонтального размещения кнопок
        total_width = (
            len(self.settings.choices) * self.settings.choice_button_size
            + (len(self.settings.choices) - 1) * self.settings.choice_button_space
        )
        start_x = (self.settings.screen_width - total_width) // 2

        # Устанавливаем прямоугольники для каждой кнопки
        for i, choice in enumerate(self.settings.choices):
            x = start_x + (
                i
                * (self.settings.choice_button_size + self.settings.choice_button_space)
            )
            y = self.settings.choice_area_y - self.settings.choice_button_size // 2
            self.buttons[choice]["rect"] = pygame.Rect(
                x, y, self.settings.choice_button_size, self.settings.choice_button_size
            )

    def create_start_button(self):
        """Создает кнопку начала игры"""
        return pygame.Rect(self.settings.screen_width // 2 - 100, 400, 200, 50)

    def create_restart_button(self):
        """Создает кнопку перезапуска игры"""
        return pygame.Rect(
            self.settings.screen_width // 2 - 100,
            self.settings.screen_height - 100,
            200,
            50,
        )
