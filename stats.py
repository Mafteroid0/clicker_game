import pygame
class Stats():
    """отслеживание статистики"""

    def __init__(self, screen):
        """инициализация статистики"""
        # self.run_game = True
        self.screen = screen
        with open("score.txt", "r") as f:
            self.score = int(f.readline())
            self.deg = int(f.readline())
            if self.deg <= 0:
                self.deg = 1
            self.robots_1 = int(f.readline())

        self.maingame = True
        self.shop = False
        self.current_room = 0
        self.bg = pygame.image.load("sprites/backgrounds/bg_1.png")
        self.bg_rect = self.bg.get_rect()
        self.coming_pos = 5 # 0 - right; 1 - left; 2 - up; 3 - bottom; 4 - center (default)

    def render_room(self, player, mainbutton):
        if self.current_room == 0:
            mainbutton.on = True
            self.bg = pygame.image.load("sprites/backgrounds/bg_0.png")
            self.bg_rect = self.bg.get_rect()
            self.screen.blit(self.bg, self.bg_rect)
            player.draw()
        elif self.current_room == 1:
            mainbutton.on = False
            self.bg = pygame.image.load("sprites/backgrounds/bg_1.png")
            self.bg_rect = self.bg.get_rect()
            self.screen.blit(self.bg, self.bg_rect)
            player.draw()

        if self.coming_pos == 0:
            player.center_x = 0
            player.center_y = 350

        elif self.coming_pos == 1:
            player.center_x = 1200
            player.center_y = 350

        elif self.coming_pos == 5:
            player.center_x = 600
            player.center_y = 350
