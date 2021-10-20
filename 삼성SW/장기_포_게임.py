# 1 4
# 2 15
# 3 18
# 4 0
# 5 102

import sys
# sys.stdin = open('장기1.txt')
sys.stdin = open('장기_포_input.txt')

T = int(input())

def dfs(start, move, preys):
    global maxAns, preys_mirror

    if move == 3:
        return

    able = []
    cr, cc = start[0], start[1]
    go = [[0]*N for _ in range(N)]
    for x, y in preys:
        go[x][y] = 1
    go[cr][cc] = 2

    # 상
    cnt = 0
    for i in range(cr-1, -1, -1):
        if cnt == 1:
            able.append((i, cc))
        if go[i][cc] == 1:
            cnt += 1
        if cnt > 1:
            break

    # 하
    cnt = 0
    for i in range(cr+1, N):
        if cnt == 1:
            able.append((i, cc))
        if go[i][cc] == 1:
            cnt += 1
        if cnt > 1:
            break

    # 좌
    cnt = 0
    for i in range(cc-1, -1, -1):
        if cnt == 1:
            able.append((cr,i))
        if go[cr][i] == 1:
            cnt += 1
        if cnt > 1:
            break

    # 우
    cnt = 0
    for i in range(cc+1, N):
        if cnt == 1:
            able.append((cr, i))
        if go[cr][i] == 1:
            cnt += 1
        if cnt > 1:
            break

    for i, j in able:
        for r, c in preys_mirror:
            if (r,c) == (i,j):
                preys_mirror.remove((r,c))
                break

    # able(잡아먹을 수 있는 리스트)에 있는 것들을 하나씩 뿌리뻗으며 dfs
    for r, c in able:
        if go[r][c] == 1:
            preys.remove((r,c))
        dfs((r,c), move+1, preys)
        if go[r][c] == 1:
            preys.append((r,c))

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]
    maxAns = 0
    preys = []

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start = (i, j)
            elif data[i][j] == 1:
                preys.append((i,j))

    preys_mirror = list(preys)
    dfs(start, 0, preys)

    print('#{} {}'.format(tc, len(preys)-len(preys_mirror)))
