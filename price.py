import pygame.font

class Price():
    """вывод цен"""
    def __init__(self, screen, price_num, x, y):
        """инициализация цены"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (116, 92, 157)
        self.font = pygame.font.SysFont(None, 60)
        self.price_num = price_num
        self.x = x
        self.y = y
        self.img_price()

    def img_price(self):
        """преобразовывает текст из счёта в изображение"""
        self.price_image = self.font.render(f"{self.price_num}", True, self.text_color)
        self.price_rect = self.price_image.get_rect()
        self.price_rect.centerx = self.x
        self.price_rect.centery = self.y


    def show_price(self):
        """вывод счёта на экран"""
        self.screen.blit(self.price_image, self.price_rect)