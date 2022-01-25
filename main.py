import pygame
from pygame.sprite import Group
from stats import Stats
import controls
from mainbutton import MainButton
from scores import Scores
from player import Player
from unclickable_object import Unclickable_object
from product import Product

def run():
    pygame.init()
    FPS = 40

    SCREEN_SIZE = (1200, 700)
    screen = pygame.display.set_mode(SCREEN_SIZE)  # размер окна
    pygame.display.set_caption("Кликер")  # заголовок окна
    bg_color = (126, 242, 116)  # создание цвета заднего фона
    shop_bg_color = (116, 242, 238)  # создание цвета заднего фона
    stats = Stats(screen)
    mainbutton = MainButton(screen, "sprites/main_button.png", 250, 500)
    cart = MainButton(screen, "sprites/cart.png", 0, 0)
    leave = MainButton(screen, "sprites/leave.png", 0, 0)
    tovar = Product(screen, 20, 125, 135, "sprites/clicksplusone.png", stats)
    tovar1 = Product(screen, 150, 325, 135, "sprites/buyrobot.png", stats)
    player = Player(screen, "sprites/character.png", mainbutton)
    scores = Scores(screen, stats)
    stats.render_room(player, mainbutton)
    robot_helper = Unclickable_object(screen, [
        "sprites/robots/robo_1.png",
        "sprites/robots/robo_2.png",
        "sprites/robots/robo_3.png",
        "sprites/robots/robo_4.png"], 900, 400, 0, stats, scores)

    while True:
        pygame.time.delay(1000 // FPS)
        player.update_player(stats)
        controls.events(screen, mainbutton, stats, scores, cart, tovar, leave, player, robot_helper, tovar1)
        controls.update(bg_color, screen, mainbutton, scores, stats, cart, tovar, leave, player, shop_bg_color, robot_helper, tovar1)


run()