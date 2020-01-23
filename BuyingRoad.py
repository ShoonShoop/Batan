class Player:
    def __init__(self):
        self.lumber = 1
        self.wheat = 1
        self.sheep = 1
        self.ore = 5
        self.brick = 1
        self.army = 1
        self.settlement = 0
        self.city = 0
        self.road = 0
        self.development_card = 0
    def buy_road(self):
        if self.brick >= 1 and self.lumber >= 1:
            self.brick -= 1
            self.lumber -= 1
            self.road += 1
            print('road purchased')
        else:
            if self.brick < 1:
                print('insufficent brick')
            if self.lumber < 1:
                print('insufficent lumber')


player2 = Player()

player2.buy_road()
