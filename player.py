import pygame

class Player():
    """Игрок"""

    def __init__(self, screen, dir, mainbutton):
        """инициализация игрока"""
        self.screen = screen
        self.image = pygame.image.load(dir)  # загрузка спрайта врага
        self.rect = self.image.get_rect()  # новый прямоугольник из спрайта
        self.screen_rect = screen.get_rect()  # новый прямоугольник из окна
        self.rect.centerx = self.screen_rect.centerx  # приравнивание пушки к середине окна по оси x
        self.rect.centery = self.screen_rect.centery  # приравнивание пушки к середине окна по оси y
        self.center_x = float(self.rect.centerx)  # сделать пиксели вещественным числом
        self.center_y = float(self.rect.centery)  # сделать пиксели вещественным числом
        self.mainbutton = mainbutton

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def update_player(self, stats):
        """обновление позиции пушки"""

        if self.move_right:
            if self.center_x <= self.screen_rect.right:
                self.center_x += 0.7
            if stats.current_room == 0 and self.center_x >= self.screen_rect.right:
                stats.current_room = 1
                stats.coming_pos = 0
                stats.render_room(self, self.mainbutton)



        elif self.move_left:
            if self.center_x > self.screen_rect.left:
                self.center_x -= 0.7
            if stats.current_room == 1 and self.center_x <= self.screen_rect.left:
                stats.current_room = 0
                stats.coming_pos = 1
                stats.render_room(self, self.mainbutton)


        elif self.move_up and self.center_y > self.screen_rect.top:
            self.center_y -= 0.7


        elif self.move_down and self.center_y < self.screen_rect.bottom:
            self.center_y += 0.7


        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def draw(self):
        """вывод игрока на экран"""
        self.screen.blit(self.image, self.rect)



