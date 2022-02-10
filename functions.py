import pygame as pg

import random as rnd

def random_yes():
    """Возвращает случайное лоическое значение."""
    return rnd.choice([True, False])

def draw_text(surf, text, size, x, y, color):
    """Выводит текст на дисплей."""
    font_name = pg.font.match_font('Arial', True)
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
