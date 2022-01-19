import pygame
from pygame.sprite import Group
from counts import Stats
import controls
from mainbutton import MainButton
from scores import Scores
from player import Player

def run():
    pygame.init()
    SCREEN_SIZE = (1200, 700)
    screen = pygame.display.set_mode(SCREEN_SIZE)  # размер окна
    pygame.display.set_caption("Кликер")  # заголовок окна
    bg_color = (126, 242, 116)  # создание цвета заднего фона
    shop_bg_color = (116, 242, 238)  # создание цвета заднего фона
    mainbutton = MainButton(screen, "sprites/main_button.png", 250, 500)
    reset = MainButton(screen, "sprites/reset.png", 590, 740)
    cart = MainButton(screen, "sprites/cart.png", 0, 0)
    leave = MainButton(screen, "sprites/leave.png", 0, 0)
    tovar = MainButton(screen, "sprites/tovar.png", 300, 400)
    player = Player(screen, "sprites/character.png")
    stats = Stats()
    scores = Scores(screen, stats)

    while True:
        player.update_player()
        controls.events(screen, mainbutton, stats, scores, reset, cart, tovar, leave, player)
        controls.update(bg_color, screen, mainbutton, scores, reset, stats, cart, tovar, leave, player, shop_bg_color)


run()