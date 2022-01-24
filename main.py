import pygame
from pygame.sprite import Group
from stats import Stats
import controls
from mainbutton import MainButton
from scores import Scores
from player import Player
from price import Price

def run():
    pygame.init()
    FPS = 40
    SCREEN_SIZE = (1200, 700)
    screen = pygame.display.set_mode(SCREEN_SIZE)  # размер окна
    pygame.display.set_caption("Кликер")  # заголовок окна
    bg_color = (126, 242, 116)  # создание цвета заднего фона
    shop_bg_color = (116, 242, 238)  # создание цвета заднего фона
    mainbutton = MainButton(screen, "sprites/main_button.png", 250, 500)
    reset = MainButton(screen, "sprites/reset.png", 590, 740)
    cart = MainButton(screen, "sprites/cart.png", 0, 0)
    leave = MainButton(screen, "sprites/leave.png", 0, 0)
    tovar = MainButton(screen, "sprites/clicksplusone.png", 125, 135)
    player = Player(screen, "sprites/character.png", mainbutton)
    stats = Stats(screen)
    price_plus_click = Price(screen, 20, 160, 330)
    scores = Scores(screen, stats)
    stats.render_room(player, mainbutton)

    while True:
        pygame.time.delay(1000 // FPS)
        player.update_player(stats)
        controls.events(screen, mainbutton, stats, scores, reset, cart, tovar, leave, player, price_plus_click)
        controls.update(bg_color, screen, mainbutton, scores, reset, stats, cart, tovar, leave, player, shop_bg_color, price_plus_click)


run()