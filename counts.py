class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализация статистики"""
        # self.run_game = True
        with open("score.txt", "r") as f:
            self.score = int(f.readline())

        self.maingame = True
        self.shop = False

