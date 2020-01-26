class Player:
    def __init__(self):
        self.lumber = 1
        self.wheat = 5
        self.sheep = 1
        self.ore = 5
        self.brick = 1
        self.army = 1
        self.settlement = 0
        self.city = 0
        self.road = 0
        self.development_card = 0
    def buy_city(self):
        if self.wheat >= 2 and self.ore >= 3:
            self.wheat -= 2
            self.ore -= 3
            self.city += 1
            print('city purchased')
        else:
            if self.wheat < 2:
                print('insufficent wheat')
            if self.ore < 3:
                print('insufficent ore')

player1 = Player()

player1.buy_city()









