import pygame
import random


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.font_medium = game.font_medium

    def make_choice(self, choice):
        """Игрок делает выбор"""
        if self.game.show_result_timer > 0:
            return

        self.game.player_choice = choice
        self.game.computer_choice = random.choice(self.settings.choices)
        result = self.determine_winner(
            self.game.player_choice, self.game.computer_choice
        )

        # Обновляем счет
        if result == "player":
            self.game.player_score += 1
            self.game.result_text = "Вы выиграли раунд!"
        elif result == "computer":
            self.game.computer_score += 1
            self.game.result_text = "Компьютер выиграл раунд!"
        else:
            self.game.result_text = "Ничья!"

        # Показываем результат на 2 секунды
        self.game.show_result_timer = 120

        # Проверяем окончание игры
        if (
            self.game.player_score >= self.settings.wins_to_win
            or self.game.computer_score >= self.settings.wins_to_win
        ):
            self.game.game_state = "game_over"

    def determine_winner(self, player_choice, computer_choice):
        """Определяет победителя раунда"""
        if player_choice == computer_choice:
            return "tie"

        if computer_choice in self.settings.rules[player_choice]:
            return "player"
        else:
            return "computer"

    def update(self):
        """Обновление состояния игры"""
        if self.game.show_result_timer > 0:
            self.game.show_result_timer -= 1
            if self.game.show_result_timer == 0:
                self.game.player_choice = None
                self.game.computer_choice = None
                self.game.result_text = ""

    def draw_round_result(self):
        """Отрисовка результата раунда"""
        if "выиграли" in self.game.result_text:
            color = self.settings.green
        elif "Компьютер" in self.game.result_text:
            color = self.settings.red
        else:
            color = self.settings.gray

        # Фон для текста результата
        text_surface = self.font_medium.render(self.game.result_text, True, color)
        text_rect = text_surface.get_rect(
            center=(self.settings.screen_width // 2, self.settings.result_y)
        )

        # Подложка
        padding = 20
        bg_rect = text_rect.inflate(padding * 2, padding)
        pygame.draw.rect(self.screen, self.settings.white, bg_rect)
        pygame.draw.rect(self.screen, color, bg_rect, 3)

        self.screen.blit(text_surface, text_rect)
