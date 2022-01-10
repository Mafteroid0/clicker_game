import pygame
import sys
import time


def events(screen, mainbutton, stats, scores, reset):
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



def update(bg_color, screen, mainbutton, scores, reset):
    """Обновление экрана"""
    screen.fill(bg_color)  # залить задний фон окна созданным ранее цветом
    mainbutton.draw()
    reset.draw()
    scores.show_score()



    pygame.display.flip()  # прорисовка
