import pygame


class Display:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bg = game.bg
        self.font_large = game.font_large
        self.font_medium = game.font_medium
        self.font_small = game.font_small
        self.font_button = game.font_button

    def draw_menu(self):
        """Отрисовка главного меню"""
        # Фон
        self.screen.blit(self.bg, (0, 0))

        # Заголовок
        title = self.font_large.render(
            "Камень ножницы бумага ящерица Спок", True, self.settings.white
        )
        title_rect = title.get_rect(center=(self.settings.screen_width // 2, 80))
        self.screen.blit(title, title_rect)

        # Правила игры
        rules_text = [
            "Правила игры:",
            "• Ножницы режут бумагу и отрезают голову ящерице",
            "• Бумага заворачивает камень и улики против Спока",
            "• Камень давит ящерицу и затупляет ножницы",
            "• Ящерица травит Спока и ест бумагу",
            "• Спок ломает ножницы и испаряет камень",
            "",
            "Игра до 3 побед",
        ]

        y_offset = 150
        for line in rules_text:
            text = self.font_small.render(line, True, self.settings.white)
            text_rect = text.get_rect(
                center=(self.settings.screen_width // 2, y_offset)
            )
            self.screen.blit(text, text_rect)
            y_offset += 25

        # Кнопка старта
        pygame.draw.rect(self.screen, self.settings.green, self.game.start_button)
        pygame.draw.rect(self.screen, self.settings.white, self.game.start_button, 3)
        start_text = self.font_medium.render("Начать игру", True, self.settings.white)
        start_rect = start_text.get_rect(center=self.game.start_button.center)
        self.screen.blit(start_text, start_rect)

    def draw_game(self):
        """Отрисовка игрового экрана"""
        # Фон
        self.screen.blit(self.bg, (0, 0))

        # Заголовки областей
        player_title = self.font_medium.render("Игрок", True, self.settings.white)
        computer_title = self.font_medium.render("Компьютер", True, self.settings.white)

        player_rect = player_title.get_rect(
            center=(self.settings.screen_width // 4, 50)
        )
        computer_rect = computer_title.get_rect(
            center=(3 * self.settings.screen_width // 4, 50)
        )

        self.screen.blit(player_title, player_rect)
        self.screen.blit(computer_title, computer_rect)

        # Счет
        score_text = self.font_large.render(
            f"{self.game.player_score} : {self.game.computer_score}",
            True,
            self.settings.white,
        )
        score_rect = score_text.get_rect(
            center=(self.settings.screen_width // 2, self.settings.score_y)
        )
        self.screen.blit(score_text, score_rect)

        # Отображение выбора игрока и компьютера
        if self.game.player_choice:
            self.draw_player_choice()

        if self.game.computer_choice:
            self.draw_computer_choice()

        # Кнопки выбора игрока
        self.draw_choice_buttons()

        # Результат раунда
        if self.game.result_text:
            self.game.scoreboard.draw_round_result()

    def draw_player_choice(self):
        """Отрисовка выбора игрока над кнопками слева"""
        choice_rect = pygame.Rect(
            self.settings.player_area_x, self.settings.choice_display_y, 150, 150
        )
        pygame.draw.rect(self.screen, self.settings.green, choice_rect)
        pygame.draw.rect(self.screen, self.settings.white, choice_rect, 3)

        # Отображаем изображение выбора
        choice_image = self.game.play_button.buttons[self.game.player_choice]["image"]
        if choice_image:
            scaled_image = pygame.transform.scale(choice_image, (100, 100))
            image_rect = scaled_image.get_rect(center=choice_rect.center)
            self.screen.blit(scaled_image, image_rect)
        else:
            text = self.font_medium.render(
                self.settings.choice_names[self.game.player_choice],
                True,
                self.settings.white,
            )
            text_rect = text.get_rect(center=choice_rect.center)
            self.screen.blit(text, text_rect)

    def draw_computer_choice(self):
        """Отрисовка выбора компьютера над кнопками справа"""
        choice_rect = pygame.Rect(
            self.settings.computer_area_x, self.settings.choice_display_y, 150, 150
        )
        pygame.draw.rect(self.screen, self.settings.red, choice_rect)
        pygame.draw.rect(self.screen, self.settings.white, choice_rect, 3)

        # Отображаем изображение выбора
        choice_image = self.game.play_button.buttons[self.game.computer_choice]["image"]
        if choice_image:
            scaled_image = pygame.transform.scale(choice_image, (100, 100))
            image_rect = scaled_image.get_rect(center=choice_rect.center)
            self.screen.blit(scaled_image, image_rect)
        else:
            text = self.font_medium.render(
                self.settings.choice_names[self.game.computer_choice],
                True,
                self.settings.white,
            )
            text_rect = text.get_rect(center=choice_rect.center)
            self.screen.blit(text, text_rect)

    def draw_choice_buttons(self):
        """Отрисовка кнопок выбора в нижней части экрана"""
        for choice, button_data in self.game.play_button.buttons.items():
            button_rect = button_data["rect"]
            button_image = button_data["image"]

            if button_rect:
                # Цвет кнопки
                color = self.settings.light_gray
                if self.game.player_choice == choice:
                    color = self.settings.green

                pygame.draw.rect(self.screen, color, button_rect)
                pygame.draw.rect(self.screen, self.settings.black, button_rect, 2)

                # Изображение на кнопке (если есть)
                if button_image:
                    # Масштабируем изображение под размер кнопки
                    scaled_image = pygame.transform.scale(
                        button_image, (button_rect.width - 10, button_rect.height - 10)
                    )
                    image_rect = scaled_image.get_rect(center=button_rect.center)
                    self.screen.blit(scaled_image, image_rect)
                else:
                    # Текст на кнопке (если нет изображения)
                    text = self.font_button.render(
                        self.settings.choice_names[choice], True, self.settings.black
                    )
                    text_rect = text.get_rect(center=button_rect.center)
                    self.screen.blit(text, text_rect)

    def draw_game_over(self):
        """Отрисовка экрана окончания игры"""
        # Фон
        self.screen.blit(self.bg, (0, 0))

        # Определяем победителя
        if self.game.player_score >= self.settings.wins_to_win:
            winner_text = "Поздравляем! Вы выиграли!"
            color = self.settings.green
        else:
            winner_text = "Компьютер выиграл!"
            color = self.settings.red

        # Текст победителя
        winner = self.font_large.render(winner_text, True, color)
        winner_rect = winner.get_rect(
            center=(
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 - 100,
            )
        )
        self.screen.blit(winner, winner_rect)

        # Финальный счет
        final_score = self.font_medium.render(
            f"Финальный счет: {self.game.player_score} : {self.game.computer_score}",
            True,
            self.settings.white,
        )
        score_rect = final_score.get_rect(
            center=(
                self.settings.screen_width // 2,
                self.settings.screen_height // 2 - 50,
            )
        )
        self.screen.blit(final_score, score_rect)

        # Кнопка перезапуска
        pygame.draw.rect(self.screen, self.settings.blue, self.game.restart_button)
        pygame.draw.rect(self.screen, self.settings.white, self.game.restart_button, 3)
        restart_text = self.font_medium.render(
            "Играть снова", True, self.settings.white
        )
        restart_rect = restart_text.get_rect(center=self.game.restart_button.center)
        self.screen.blit(restart_text, restart_rect)
