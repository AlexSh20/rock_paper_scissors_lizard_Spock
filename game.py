import pygame
import sys
from settings import Settings
from button import Button
from display import Display
from scoreboard import Scoreboard


class RockPaperScissorsLizardSpock:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Камень - ножницы - бумага - ящерица - Спок")
        self.clock = pygame.time.Clock()

        # Загрузка изображений
        self.bg = pygame.image.load("img/background.jpg")
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_width, self.settings.screen_height)
        )

        # Шрифты
        self.font_large = pygame.font.Font(None, self.settings.font_large)
        self.font_medium = pygame.font.Font(None, self.settings.font_medium)
        self.font_small = pygame.font.Font(None, self.settings.font_small)
        self.font_button = pygame.font.Font(None, self.settings.font_for_button)

        # Первоначальное состояние игры
        self.game_state = "menu"  # Всего 3 режима: menu, playing, game_over
        self.show_result_timer = 0

        # Классы, используемые в игре
        self.play_button = Button(self)
        self.display = Display(self)
        self.scoreboard = Scoreboard(self)

        # Позиции кнопок
        self.play_button.setup_buttons()

        # Создание дополнительных кнопок
        self.start_button = self.play_button.create_start_button()
        self.restart_button = self.play_button.create_restart_button()

    def draw(self):
        """Основная функция отрисовки"""
        if self.game_state == "menu":
            self.display.draw_menu()
        elif self.game_state == "playing":
            self.display.draw_game()
        elif self.game_state == "game_over":
            self.display.draw_game_over()

        pygame.display.flip()

    def run(self):
        """Игровой цикл"""
        running = True
        while running:
            running = self.handle_events()
            self.scoreboard.update()
            self.draw()
            self.clock.tick(self.settings.fps)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.game_state == "menu":
                    if self.start_button.collidepoint(mouse_pos):
                        self.start_game()

                elif self.game_state == "playing":
                    # Проверка нажатия на кнопки выбора
                    for choice, button_data in self.play_button.buttons.items():
                        if button_data["rect"] and button_data["rect"].collidepoint(
                            mouse_pos
                        ):
                            self.scoreboard.make_choice(choice)
                            break

                elif self.game_state == "game_over":
                    if self.restart_button.collidepoint(mouse_pos):
                        self.start_game()  # Перезапуск игры

        return True

    def start_game(self):
        """Начинает новую игру"""
        self.game_state = "playing"
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = None
        self.computer_choice = None
        self.result_text = ""
