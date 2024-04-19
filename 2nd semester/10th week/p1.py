def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    bebe = {}
    for word in words:
        node = bebe
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = word

    visited = [[False] * len(board[0]) for _ in range(len(board))]

    def dfs(i, j, node, path, result):
        if '#' in node:
            result.append(path)
            node = node['#']

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] or board[i][j] not in node:
            return

        visited[i][j] = True
        path += board[i][j]

        moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        for dx, dy in moves:
            dfs(i + dx, j + dy, node[board[i][j]], path, result)

        path = path[:-1]

    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, bebe, '', result)

    return result


def main():
    n = int(input())
    wrds = list(input().split())
    m, l = map(int, input().split())
    board = []
    for _ in range(l):
        board.append(list(input().split()))
    res = list(set(find_words(board, wrds)))
    print(*res)


if __name__ == '__main__':
    main()