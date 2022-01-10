import pygame
from pygame.sprite import Group
from counts import Stats
import controls
from mainbutton import MainButton
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))  # размер окна
    pygame.display.set_caption("Кликер")  # заголовок окна
    bg_color = (5, 5, 5)  # создание цвета заднего фона
    mainbutton = MainButton(screen, "sprites/main_button.png", 250, 500)
    reset = MainButton(screen, "sprites/reset.png", 590, 740)
    stats = Stats()
    scores = Scores(screen, stats)

    while True:
        controls.events(screen, mainbutton, stats, scores, reset)
        controls.update(bg_color, screen, mainbutton, scores, reset)
        mainbutton.draw()

run()