import time
import os
import random
import settings as st

def map_generate(x, y):
    map = []
    for i in range(y):
        line = []
        for j in range(x):
            if i == 0 or j == 0 or i == y-1 or j == x-1:
                line.append('W')
            else:
                line.append('.')
        map.append(line)

    map[st.MAP_PLAYER_Y][st.MAP_PLAYER_X] = 'P'
    map[st.MAP_FINISH_Y][st.MAP_FINISH_X] = 'F'

    for i in range(1, y-1):
        for j in range(1, x-1):
            if map[i][j] != 'F' and map[i][j] != 'P':
                counter = 0
                if map[i-1][j-1] == 'W':
                    counter += 1
                if map[i][j-1] == 'W':
                    counter += 1
                if map[i+1][j-1] == 'W':
                    counter += 1
                if map[i-1][j] == 'W':
                    counter += 1
                if map[i+1][j] == 'W':
                    counter += 1
                if map[i-1][j+1] == 'W':
                    counter += 1
                if map[i][j+1] == 'W':
                    counter += 1
                if map[i+1][j+1] == 'W':
                    counter += 1
                if counter == 0:
                    if random.randint(0, 10) > 4:
                        map[i][j] = 'W'
                if 0 < counter < 3:
                    if random.randint(0, 10) > 6:
                        map[i][j] = 'W'
                if 2 < counter < 6:
                    if random.randint(0, 10) > 9:
                        map[i][j] = 'W'

                map[st.MAP_PLAYER_Y][st.MAP_PLAYER_X - 1] = '.'
                map[st.MAP_PLAYER_Y][st.MAP_PLAYER_X + 1] = '.'
                map[st.MAP_PLAYER_Y - 1][st.MAP_PLAYER_X] = '.'
                map[st.MAP_PLAYER_Y - 1][st.MAP_PLAYER_X - 1] = '.'
                map[st.MAP_PLAYER_Y - 1][st.MAP_PLAYER_X + 1] = '.'
                # Задняя стенка
                # map[st.MAP_PLAYER_Y + 1][st.MAP_PLAYER_X] = '.'
                # map[st.MAP_PLAYER_Y + 1][st.MAP_PLAYER_X - 1] = '.'
                # map[st.MAP_PLAYER_Y + 1][st.MAP_PLAYER_X + 1] = '.'
    return map


def distance_counter(map, x, y, player_x, player_y):
    distance_map = []
    for i in range(y):
        line = []
        for j in range(x):
            if map[i][j] == 'W':
                line.append('W')
            else:
                line.append(999)
        distance_map.append(line)
    distance_map[player_y][player_x] = 0

    distance_queue = []
    map_x, map_y = player_x, player_y
    if map_y-1 >= 0 and distance_map[map_y-1][map_x] != 'W' and distance_map[map_y-1][map_x] > distance_map[map_y][map_x]+1:
        distance_map[map_y-1][map_x] = distance_map[map_y][map_x] + 1
        distance_queue.append([map_y-1, map_x])
    if map_y+1 < y and distance_map[map_y+1][map_x] != 'W' and  distance_map[map_y+1][map_x] > distance_map[map_y][map_x]+1:
        distance_map[map_y+1][map_x] = distance_map[map_y][map_x] + 1
        distance_queue.append([map_y+1, map_x])
    if map_x-1 >= 0 and distance_map[map_y][map_x-1] != 'W' and distance_map[map_y][map_x-1] > distance_map[map_y][map_x]+1:
        distance_map[map_y][map_x-1] = distance_map[map_y][map_x] + 1
        distance_queue.append([map_y, map_x-1])
    if map_x+1 < x and distance_map[map_y][map_x+1] != 'W' and  distance_map[map_y][map_x+1] > distance_map[map_y][map_x]+1:
        distance_map[map_y][map_x+1] = distance_map[map_y][map_x] + 1
        distance_queue.append([map_y, map_x+1])

    while len(distance_queue) > 0:
        map_y, map_x = distance_queue.pop(0)
        if map_y - 1 >= 0 and distance_map[map_y - 1][map_x] != 'W' and distance_map[map_y - 1][map_x] > \
                distance_map[map_y][map_x] + 1:
            distance_map[map_y - 1][map_x] = distance_map[map_y][map_x] + 1
            distance_queue.append([map_y - 1, map_x])
        if map_y + 1 < y and distance_map[map_y + 1][map_x] != 'W' and distance_map[map_y + 1][map_x] > \
                distance_map[map_y][map_x] + 1:
            distance_map[map_y + 1][map_x] = distance_map[map_y][map_x] + 1
            distance_queue.append([map_y + 1, map_x])
        if map_x - 1 >= 0 and distance_map[map_y][map_x - 1] != 'W' and distance_map[map_y][map_x - 1] > \
                distance_map[map_y][map_x] + 1:
            distance_map[map_y][map_x - 1] = distance_map[map_y][map_x] + 1
            distance_queue.append([map_y, map_x - 1])
        if map_x + 1 < x and distance_map[map_y][map_x + 1] != 'W' and distance_map[map_y][map_x + 1] > \
                distance_map[map_y][map_x] + 1:
            distance_map[map_y][map_x + 1] = distance_map[map_y][map_x] + 1
            distance_queue.append([map_y, map_x + 1])

        # Отображение поиска расстояния
        # os.system('cls||clear')
        # for line in distance_map:
        #     for elem in line:
        #         if len(str(elem)) < 2:
        #             print(f'  {elem}', end=" ")
        #         elif len(str(elem)) < 3:
        #             print(f' {elem}', end=" ")
        #         else:
        #             print(elem, end=" ")
        #     print()
        # time.sleep(0.001)
    return distance_map[st.MAP_FINISH_Y][st.MAP_FINISH_X]


# Press the green button in the gutter to run the script.
def map_create():
    finish_distance = 999
    new_map = []
    while finish_distance > 50 or finish_distance < 30:
        new_map = map_generate(st.MAP_WIDTH, st.MAP_HEIGHT)
        finish_distance = distance_counter(new_map, st.MAP_WIDTH, st.MAP_HEIGHT, st.MAP_PLAYER_X, st.MAP_PLAYER_Y)
    # Вывод сгенерированной карты и расстояния от старта до финиша в консоль
    # print(finish_distance)
    # for line in new_map:
    #     print(' '.join(line))
    return new_map

