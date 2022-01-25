import pygame
import sys
import time


def events(screen, mainbutton, stats, scores, cart, tovar, leave, player, robot_helper, tovar1):
    """Обработчик событий"""
    for event in pygame.event.get():  # получение всех событий (действий) пользователя
        if event.type == pygame.QUIT:  # если пользователь закрыл игру (нажал на крестик)
            with open("score.txt", "w") as f:
                f.write(str(stats.score))
                f.write("\n")
                f.write(str(stats.deg))
                f.write("\n")
                f.write(str(stats.robots_1))
            sys.exit()  # окно закрывается

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button
            # print(mouse_pos)

            if mainbutton.rect.collidepoint(mouse_pos) and stats.maingame and mainbutton.on:
                # prints current location of mouse
                stats.score += stats.deg

                scores.img_score()
                scores.show_score()

            elif cart.rect.collidepoint(mouse_pos) and not stats.shop:
                stats.maingame = False
                stats.shop = True

            elif leave.rect.collidepoint(mouse_pos) and stats.shop:
                stats.maingame = True
                stats.shop = False

            elif tovar.rect.collidepoint(mouse_pos):
                if stats.score >= tovar.price_num and stats.shop:
                    stats.score -= tovar.price_num
                    stats.deg += 1
                    tovar.price_num *= 2
                    scores.img_score()
                    scores.show_score()
                    tovar.img_price()
                    tovar.draw()

            elif tovar1.rect.collidepoint(mouse_pos):
                if stats.score >= tovar1.price_num and stats.shop:
                    stats.score -= tovar1.price_num
                    stats.robots_1 += 1
                    tovar1.price_num *= 2
                    robot_helper.on = True

                    scores.img_score()
                    scores.show_score()
                    tovar1.img_price()
                    tovar1.draw()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                player.move_right = True
            elif event.key == pygame.K_a:  # нажатая клавиша - A
                player.move_left = True
            elif event.key == pygame.K_w:
                player.move_up = True
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = True
            player.update_player(stats)



        elif event.type == pygame.KEYUP:  # если отжата клавиша
            if event.key == pygame.K_d:  # отжатая клавиша - D
                player.move_right = False
            elif event.key == pygame.K_a:  # отжатая клавиша - A
                player.move_left = False
            elif event.key == pygame.K_w:
                player.move_up = False
            elif event.key == pygame.K_s:  # нажатая клавиша - A
                player.move_down = False
            player.update_player(stats)





def update(bg_color, screen, mainbutton, scores, stats, cart, tovar, leave, player, shop_bg_color, robot_helper, tovar1):
    """Обновление экрана"""
    if stats.maingame:
        # stats.render_room(player)
        screen.blit(stats.bg, stats.bg_rect)
        if stats.current_room == 0:
            mainbutton.draw()
        cart.draw()
        player.draw()
        scores.show_score()
        if robot_helper.on:
            robot_helper.draw()
    elif stats.shop:
        screen.fill(shop_bg_color)
        tovar.draw()
        tovar1.draw()
        leave.draw()
        scores.show_score()
    pygame.display.flip()


    pygame.display.flip()  # прорисовка
