from Tile import *



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

def mdown():
    pos = pygame.mouse.get_pos()
    if num_of_inters(pos) == 3:
        return True

def place_city():
    if mdown():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(window, (0, 255, 0), pos, 5, 1)
        pygame.display.update()

run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            place_city()
        for tile in lot:
            tile.draw()










