import pygame
import sys
import time


def events(screen, mainbutton, stats, scores, reset, cart, tovar, leave, player, price_plus_click):
    """Обработчик событий"""
    for event in pygame.event.get():  # получение всех событий (действий) пользователя
        if event.type == pygame.QUIT:  # если пользователь закрыл игру (нажал на крестик)
            sys.exit() # окно закрывается

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button
            print(mouse_pos)

            if mainbutton.rect.collidepoint(mouse_pos) and stats.maingame:
                # prints current location of mouse
                stats.score += stats.deg
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

            elif cart.rect.collidepoint(mouse_pos) and not stats.shop:
                stats.maingame = False
                stats.shop = True

            elif leave.rect.collidepoint(mouse_pos) and stats.shop:
                stats.maingame = True
                stats.shop = False

            elif tovar.rect.collidepoint(mouse_pos):
                if stats.score >= price_plus_click.price_num and stats.shop:
                    stats.score -= price_plus_click.price_num
                    stats.deg += 1
                    price_plus_click.price_num *= 2
                    scores.img_score()
                    scores.show_score()
                    price_plus_click.img_price()
                    price_plus_click.show_price()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                player.move_right = True
            elif event.key == pygame.K_a:  # нажатая клавиша - A
                player.move_left = True
            elif event.key == pygame.K_w:
                player.move_up = True
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = True
            player.update_player()



        elif event.type == pygame.KEYUP:  # если отжата клавиша
            if event.key == pygame.K_d:  # отжатая клавиша - D
                player.move_right = False
            elif event.key == pygame.K_a:  # отжатая клавиша - A
                player.move_left = False
            elif event.key == pygame.K_w:
                player.move_up = False
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = False
            player.update_player()




def update(bg_color, screen, mainbutton, scores, reset, stats, cart, tovar, leave, player, shop_bg_color, price_plus_click):
    """Обновление экрана"""
    if stats.maingame:
        screen.fill(bg_color)
        mainbutton.draw()
        reset.draw()
        cart.draw()
        player.draw()
        scores.show_score()
    elif stats.shop:
        screen.fill(shop_bg_color)
        tovar.draw()
        leave.draw()
        price_plus_click.show_price()
        scores.show_score()
    pygame.display.flip()




    pygame.display.flip()  # прорисовка
