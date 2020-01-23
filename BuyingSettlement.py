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
    def buy_settlement(self):
        if self.lumber >= 1 and self.brick >= 1 and self.sheep >= 1 and self.wheat >= 1:
            self.lumber -= 1
            self.brick -= 1
            self.sheep -= 1
            self.wheat -= 1
            self.settlement += 1
            print('settlement purchased')
        else:
            if self.lumber < 1:
                print ('insufficent lumber')
            if self.brick < 1:
                print ('insufficent brick')
            if self.wheat < 1:
                print ('insufficent wheat')
            if self.sheep < 1:
                print ('insufficent sheep')
            if self.lumber < 1 or self.brick < 1 or self.wheat < 1 or self.sheep < 1:
                print('settlement not purchased')

player1 = Player()

player1.buy_settlement()


