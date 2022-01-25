import pygame

import stats


class Unclickable_object():
    def __init__(self, screen, dir_list, x, y, place, stats, scores):
        """инициализация обьекта"""
        self.screen = screen
        self.dir_list = []
        for i in range(len(dir_list)):
            self.dir_list.append(pygame.image.load(dir_list[i]))
        self.image = pygame.image.load(dir_list[0]) # загрузка спрайта обьекта
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.animcount = 0
        self.scores = scores
        self.place = place
        self.on = True if stats.robots_1 != 0 else False
        self.stats = stats

    def draw(self):
        """вывод Обьекта на экран"""
        if self.stats.current_room == self.place:
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.screen.blit(self.image, self.rect)

        self.image = self.dir_list[self.animcount // 13]
        self.animcount += 1
        if self.animcount >= 50:
            self.stats.score += self.stats.robots_1
            self.scores.img_score()
            self.animcount = 0

