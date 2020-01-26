from Settlement import *
from PlayerInfo import *



column = 0
row = 0
while row < 3:
    lot.append(Tile ((x + (column * 72)), (y + (round(row * (48 * math.sqrt(3))))), "water"))
    row += 1
row = 0
column = 1
y -= round(24 * math.sqrt(3))
while row < 4:
    lot.append(Tile ((x + (column * 72)), (y + (round(row * (48 * math.sqrt(3))))), "water"))
    row += 1
row = 0
column = 2
y -= round(24 * math.sqrt(3))
while row < 5:
    lot.append(Tile ((x + (column * 72)), (y + (round(row * (48 * math.sqrt(3))))), "water"))
    row += 1
row = 0
column = 3
y += round(24 * math.sqrt(3))
while row < 4:
    lot.append(Tile ((x + (column * 72)), (y + (round(row * (48 * math.sqrt(3))))), "water"))
    row += 1
row = 0
column = 4
y += round(24 * math.sqrt(3))
while row < 3:
    lot.append(Tile ((x + (column * 72)), (y + (round(row * (48 * math.sqrt(3))))), "water"))
    row += 1
row = 0

def num_of_inters(pos):
    intersections = 0
    for Tile in lot:
        if Tile.inside(pos):
            intersections += 1
    return intersections

radius = 60


def mdown():
    pos = pygame.mouse.get_pos()

def settlement_place(pos):
    if num_of_inters(pos) == 3:
        X = pos[0]
        Y = pos[1]
        indx = 0
        if player.list_settlements:
            while indx < len(player.list_settlements):
                dist = round(math.sqrt(((X - player.list_settlements[indx].x) ** 2) + ((Y - player.list_settlements[indx].y) ** 2)))
                if dist < radius:
                    break
                indx += 1
            if indx == len(player.list_settlements):
                player.list_settlements.append(Settlement(X, Y, 0))
                place_city(pos)
                print(player.list_settlements)
        else:
            place_city(pos)
            player.list_settlements.append(Settlement(X, Y, 0))
            print(player.list_settlements)


def place_city(pos):
    pygame.draw.circle(window, (0, 255, 0), pos, radius, 2)
    pygame.display.update()

run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            settlement_place(pygame.mouse.get_pos())
        for tile in lot:
            tile.draw()










