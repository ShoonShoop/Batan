class Player:
    def __init__(self):
        self.lumber = 1
        self.wheat = 0
        self.sheep = 0
        self.ore = 0
        self.brick = 1
        self.army = 1
        self.settlement = 0
        self.city = 0
        self.road = 0
        self.development_card = 0
    def buy_dev_card(self):
        if self.sheep >= 1 and self.wheat >= 1 and self.ore >= 1:
            self.sheep -= 1
            self.wheat -= 1
            self.ore -= 1
            self.development_card += 1
            print('purchased development card')
        else:
            if self.sheep < 1:
                print('insufficent sheep')
            if self.wheat < 1:
                print('insufficent wheat')
            if self.ore < 1:
                print('insufficent ore')


player3 = Player()

player3.buy_dev_card()





