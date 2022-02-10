import pygame as pg
import color
import options as opt
import functions as fnc

def map_draw(surf):
    """Рисует карту."""
 
    fnc.draw_text(surf, "Игрок №1", opt.WIDTH//50, 
                  opt.WIDTH//4, opt.HEIGHT//40, color.WHITE)
    fnc.draw_text(surf, "Игрок №2", opt.WIDTH//50, 
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT//40, color.WHITE)
    
    fnc.draw_text(surf, "Управление: L-CTRL", opt.WIDTH//60, 
                  opt.WIDTH//4, opt.HEIGHT - opt.HEIGHT//28, color.GRAY)
    fnc.draw_text(surf, "Управление: R-CTRL", opt.WIDTH//60, 
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT - opt.HEIGHT//28, color.GRAY)
