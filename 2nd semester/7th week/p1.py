# 1) На шахматной доске n × n в некоторой клетке расположен конь. Для каждой клетки найдите мини- мальное число шагов
# коня для её достижения. Асимптотика: O(n2).
import numpy as np


def knight_moves(n, start):
    moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]  # dy и dx

    board = np.array([[float('inf') for _ in range(n)] for _ in range(n)])

    board[start[0]][start[1]] = 0

    queue = [(start, 0)]

    while queue:
        curr, m_count = queue.pop(0)

        for dy, dx in moves:
            new_y, new_x = curr[0] + dy, curr[1] + dx

            if 0 <= new_x < n and 0 <= new_y < n:
                if board[new_y][new_x] > m_count + 1:
                    board[new_y][new_x] = m_count + 1
                    queue.append(([new_y, new_x], m_count + 1))

    return board


def main():
    n = 8
    start_square = [0, 0]  # сначала y координата, потом x
    print(knight_moves(n, start_square))
    '''
    [[0. 3. 2. 5.]
     [3. 4. 1. 2.]
     [2. 1. 4. 3.]
     [5. 2. 3. 2.]]
    '''


if __name__ == '__main__':
    main()