class Settings:
    """Класс для хранения всех настроек игры  игры "Камень ножницы бумага ящерица Спок" """

    def __init__(self):
        # Параметры экрана
        self.screen_width = 960
        self.screen_height = 640

        # цвета
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 100, 200)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.gray = (128, 128, 128)
        self.light_gray = (200, 200, 200)
        self.dark_gray = (64, 64, 64)

        # Игровые настройки
        self.wins_to_win = 3  # Количество побед для выигрыша
        self.fps = 60

        # Размеры элементов
        self.button_width = 120
        self.button_height = 120

        # Размеры кнопок выбора
        self.choice_button_size = 80
        self.choice_button_space = 20

        # Позиции элементов
        self.player_area_x = 100  # Отступ область игрока слева
        self.computer_area_x = 680  # Отступ области компьютера
        self.choice_area_y = 580  # Отступ кнопок выбора в нижней части экрана
        self.choice_display_y = 300  # Отступ над кнопками для отображение выбора

        # Очки
        self.score_y = 50
        self.result_y = 200

        # Размеры шрифтов
        self.font_large = 32
        self.font_medium = 20
        self.font_small = 16
        self.font_for_button = 14

        # Варианты выбора
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]

        # Правила игры (что побеждает что)
        self.rules = {
            "scissors": [
                "paper",
                "lizard",
            ],  # Ножницы режут бумагу и отрезают голову ящерице
            "paper": [
                "rock",
                "spock",
            ],  # Бумага заворачивает камень и улики против Спока
            "rock": ["lizard", "scissors"],  # Камень давит ящерицу и затупляет ножницы
            "lizard": ["spock", "paper"],  # Ящерица травит Спока и ест бумагу
            "spock": ["scissors", "rock"],  # Спок ломает ножницы и испаряет камень
        }

        # Названия вариантов на русском
        self.choice_names = {
            "rock": "Камень",
            "paper": "Бумага",
            "scissors": "Ножницы",
            "lizard": "Ящерица",
            "spock": "Спок",
        }
