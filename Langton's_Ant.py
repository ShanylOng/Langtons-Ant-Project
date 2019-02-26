import pygame as pg
from pygame import freetype
import numpy as np

pg.display.init()
pg.freetype.init()

# fixed display elements setup

screen_width = 1010
screen_height = 810
win = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption("Langton's Ant")
win.fill((255, 255, 255))

font = pg.freetype.SysFont('Consolas', 15)

font.render_to(win, (0, 0), "Gridbase:", (0, 0, 0))
font.render_to(win, (0, 80), "Delay(ms):", (0, 0, 0))
font.render_to(win, (0, 160), "Maximum Iterations:", (0, 0, 0))
font.render_to(win, (0, 240), "Command:", (0, 0, 0))
font.render_to(win, (20, 260), "No. of Colours:", (0, 0, 0))
font.render_to(win, (20, 320), "Command Specs:", (0, 0, 0))
font.render_to(win, (20, 500), "START", (255, 0, 0))

font.render_to(win, (30, 40), "5  10  20  40  80", (255, 0, 0))
font.render_to(win, (7, 120), "50  100  200  500  1000", (255, 0, 0))
font.render_to(win, (12, 200), "50  100  200  400  Max", (255, 0, 0))
# font.render_to(win, (30, 280))

gridbase = 10   # factors of 800
drawgrid = True
drawgrid_x = 200
drawgrid_y = 0

while drawgrid:
    pg.draw.line(win, (0, 0, 0), (drawgrid_x, 0), (drawgrid_x, 800), 1)
    drawgrid_x += gridbase
    pg.draw.line(win, (0, 0, 0), (200, drawgrid_y), (1000, drawgrid_y), 1)
    drawgrid_y += gridbase

    if drawgrid_y > 800:
        drawgrid = False

pg.display.update()

run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
