# Screen options
WIDTH = 1280  # Ширина окна программы
HEIGHT = 720  # Высота окна программы
FPS = 60  # Частота кадров программы

# Game options
DEATH_LINE_X = - WIDTH//4  # Линия смерти по оси X
DEATH_LINE_Y = HEIGHT + HEIGHT//10  # Линия смерти по оси Y
SAPWN_LINE = WIDTH + WIDTH//10  # Линия возрождения
CENTER_X = WIDTH//2  # Центр экрана по Х
CENTER_Y = HEIGHT//2  # Центр экрана по Y
GRAVITY = HEIGHT//100  # Сила притяжения
PRESENT_TIME = None  # Метка времени
RUN_GAME = True  # Состояние игры

# Bird options
BIRD_HEGHT = HEIGHT//18  # Высота птички
BIRD_WIDTH = WIDTH//32  # Ширина птички
TAKEOFF_SPEED = HEIGHT//80  # Скорость взлета
TAKEOFF_HEIGHT = HEIGHT//40  # Высота взлета
BIRD_ALIVE = True  # Состояние прички

# Pipe options
PIPE_HEIGHT = HEIGHT//22  # Начальная высота труб
PIPE_WIDTH = WIDTH//14  # Ширина трубы
PIPE_MOVE_SPEED = HEIGHT//300  # Скорость перемещения труб
PIPE_WINDOW = HEIGHT//3  # Ширина окна
PIPE_SPAWN_TIME = 2000  # Периодичность вывода труб
PIPE_LAST_SPAWN = None  # Время последнего вывода труб

# Player options
PLAYER_SCORE = 0  # Очки игрока
