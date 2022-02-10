import pygame as pg

import color
import options as opt
import objects as obj
import functions as fnc

pg.init()  # Инициализируется окно программы
screen = pg.display.set_mode([opt.WIDTH, opt.HEIGHT])  # Задаются размеры окна
pg.display.set_caption("Flappy Bird")  # Задается название в шапке окна
clock = pg.time.Clock()  # Задаются внутренние часы программы

# Создаются группы спрайтов
all_sprites = pg.sprite.Group()
pipe = pg.sprite.Group()
bird = pg.sprite.Group()

def create_bird():
    """Создает птичку."""
    flappy_bird = obj.Bird()
    all_sprites.add(flappy_bird)
    bird.add(flappy_bird)
    return flappy_bird
    
def create_pipes():
    """Создает трубы."""
    pipe_top = obj.Pipe('top', opt.SAPWN_LINE)
    pipe_bottom = obj.Pipe('bottom', opt.SAPWN_LINE, pipe_top.height)
    all_sprites.add(pipe_top, pipe_bottom)
    pipe.add(pipe_top, pipe_bottom)
    opt.PIPE_LAST_SPAWN = pg.time.get_ticks()

def bird_collide():
    """Проверка столкновения."""
    if pg.sprite.spritecollide(flappy_bird, pipe, True):
        all_sprites.empty()
        opt.BIRD_ALIVE = False
        opt.RUN_GAME = False
        fnc.draw_text(screen, 'Пройдено труб: %s !' % int(opt.PLAYER_SCORE), 
                        opt.HEIGHT//12, opt.WIDTH//2, opt.HEIGHT//2, color.BLUE)
        fnc.draw_text(screen, 'Нажмите LCtrl для перезапуска', 
                        opt.HEIGHT//12, opt.WIDTH//2, opt.HEIGHT - opt.HEIGHT//5, color.BLUE)

# Создаются объекты
flappy_bird = create_bird()
create_pipes()

RUNNING = True
while RUNNING:    
    clock.tick(opt.FPS)  # Контроль частоты кадров
    
    # Проверка событий
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            RUNNING = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flappy_bird.takeoff = True
            if event.key == pg.K_LCTRL:
                opt.RUN_GAME = True

    if not opt.BIRD_ALIVE and opt.RUN_GAME:
        opt.BIRD_ALIVE = True
        flappy_bird = create_bird()
        create_pipes()
        opt.PLAYER_SCORE = 0

    # Отрисовка труб
    if opt.BIRD_ALIVE and opt.RUN_GAME:
        opt.PRESENT_TIME = pg.time.get_ticks()
        if opt.PRESENT_TIME - opt.PIPE_LAST_SPAWN >= opt.PIPE_SPAWN_TIME:
            create_pipes()

    bird_collide()  # Контроль столкновений

    all_sprites.update()  # Обновление спрайтов

    if opt.RUN_GAME:
        screen.fill(color.LIGHT_BLUE)  # Заливка фона

    all_sprites.draw(screen)  # Отрисовка спрайтов
    
    # Отображение очков
    fnc.draw_text(screen, str(int(opt.PLAYER_SCORE)), opt.HEIGHT//16, 
                    opt.WIDTH//40, opt.HEIGHT//40, color.BLUE)
    fnc.draw_text(screen, 'Управление: SPACE', opt.HEIGHT//40, 
                    opt.WIDTH//12, opt.HEIGHT - opt.HEIGHT//30, color.BLUE)
    
    pg.display.flip()  # Смена кадра дисплея
pg.quit()
