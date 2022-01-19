import pygame.font

class Scores():
    """вывод игрового счёта"""
    def __init__(self, screen, stats):
        """инициализация подсчёта очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (116, 92, 157)
        self.font = pygame.font.SysFont(None, 60)
        self.img_score()

    def img_score(self):
        """преобразовывает текст из счёта в изображение"""
        self.score_image = self.font.render(f"{self.stats.score}", True, self.text_color, (5, 5, 5))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = 595
        self.score_rect.top = 25


    def show_score(self):
        """вывод счёта на экран"""
        self.screen.blit(self.score_image, self.score_rect)