import sys

sys.stdin = open("1226input.txt", "r")


def bfs(r, c):
    queue = [(r, c)]
    visited = [(r, c)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        cr, cc = queue.pop(0)

        if arr[cr][cc] == 3:
            return 1

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 0 or arr[nr][nc] == 3) and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.append((nr, nc))
    return 0


T = 10

for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for x in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s = (i, j)

    res = bfs(s[0], s[1])

    print('#{} {}'.format(tc, res))