import pygame
import sys
import time


def events(screen, mainbutton, stats, scores, reset, cart, tovar):
    """Обработчик событий"""
    for event in pygame.event.get():  # получение всех событий (действий) пользователя
        if event.type == pygame.QUIT:  # если пользователь закрыл игру (нажал на крестик)
            sys.exit() # окно закрывается

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button

            if mainbutton.rect.collidepoint(mouse_pos):
                # prints current location of mouse
                stats.score += 1
                with open("score.txt", "w") as f:
                    f.write(str(stats.score))

                scores.img_score()
                scores.show_score()

            elif reset.rect.collidepoint(mouse_pos):
                # prints current location of mouse
                stats.score = 0
                with open("score.txt", "w") as f:
                    f.write(str(stats.score))

                scores.img_score()
                scores.show_score()

            elif cart.rect.collidepoint(mouse_pos):
                stats.maingame = False
                stats.shop = True

            elif tovar.rect.collidepoint(mouse_pos):
                if stats.score >= 20 and stats.shop:
                    stats.score -= 20
                    scores.img_score()
                    scores.show_score()
                stats.maingame = True
                stats.shop = False



def update(bg_color, screen, mainbutton, scores, reset, stats, cart, tovar):
    """Обновление экрана"""
    screen.fill(bg_color)  # залить задний фон окна созданным ранее цветом
    scores.show_score()
    if stats.maingame:
        mainbutton.draw()
        reset.draw()
        cart.draw()
    elif stats.shop:
        tovar.draw()




    pygame.display.flip()  # прорисовка
