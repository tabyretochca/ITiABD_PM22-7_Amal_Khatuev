import random
def prin(maps):
    print(' ', end='')
    print('  0  1  2')
    for i in range(3):
        print(i, '', end = '')
        for j in range(3):
            print(maps[i][j].center(3), end = '')
        print()
turn = 0
maps = [[str(random.randint(1,9))for i in range(3)] for j in range(3)]
counter1y = [3, 3, 3]
counter2x = [3, 3, 3]
prin(maps)
x1, y1 = [int(i) for i in input('Введите координаты: ').split()]
maps[y1][x1] = '(' + maps[y1][x1] + ')'
counter2x[x1]-=1
turn = 2
prin(maps)
x2, y2 = [int(i) for i in input('Введите координаты: ').split()]
while x2 != x1:
    x2, y2 = [int(i) for i in input('Введите координаты: ').split()]
maps[y2][x2] = '(' + maps[y2][x2] + ')'
counter1y[y2]-=1
turn = 1
prin(maps)
while True:
    if counter1y[y2]!=0:
        x1, y1 = [int(i) for i in input('Введите координаты: ').split()]
        while y1!= y2:
            x1, y1 = [int(i) for i in input('Введите координаты: ').split()]
        maps[y1][x1] = '(' + maps[y1][x1] + ')'
        counter2x[x1] -= 1
    elif counter2x[x2]==0:
        break
    if counter2x[]:
    prin(maps)


