import pygame as pg

import color
import options as opt
import functions as fnc
import random as rnd

class Bird(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = opt.BIRD_WIDTH
        self.height = opt.BIRD_HEGHT
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (opt.CENTER_X, opt.CENTER_Y)
        self.takeoff_height = opt.TAKEOFF_HEIGHT
        self.takeoff_height_cnt = 0
        self.takeoff_speed = opt.TAKEOFF_SPEED
        self.takeoff = False

    def update(self):
        
        if self.takeoff:
            self.rect.y -= self.takeoff_speed
            self.takeoff_height_cnt += 1
        else:
            self.rect.y += opt.GRAVITY
        
        if self.takeoff_height_cnt >= self.takeoff_height:
            self.takeoff = False
            self.takeoff_height_cnt = 0

        if self.rect.bottom >= opt.HEIGHT:
            self.rect.bottom = opt.HEIGHT

        if self.rect.top <= 0:
            self.rect.top = 0

class Pipe(pg.sprite.Sprite):
    def __init__(self, location, spawn_line, top_height=None):
        pg.sprite.Sprite.__init__(self)
        self.location = location  # Расположение трубы 'top' или 'bottom'
        if self.location == 'top':
            self.height = rnd.randrange(opt.PIPE_HEIGHT, 
                                opt.HEIGHT - opt.PIPE_WINDOW - opt.PIPE_HEIGHT, 
                                opt.HEIGHT//50)
        else:
            self.height = (opt.HEIGHT - top_height - opt.PIPE_WINDOW)
        self.width = opt.PIPE_WIDTH
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = spawn_line
        self.score_up = False  # Флаг контроля прохождения трубы
        
        if self.location == 'top':
            self.rect.top = 0
        else:
            self.rect.bottom = opt.HEIGHT

    def update(self):
        self.rect.x -= opt.PIPE_MOVE_SPEED

        if self.rect.right <= opt.CENTER_X and not self.score_up:
            self.score_up = True
            opt.PLAYER_SCORE += 0.5

        if self.rect.right <= opt.DEATH_LINE_X:
            self.kill()
