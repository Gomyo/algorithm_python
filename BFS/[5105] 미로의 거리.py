def bfs(r,c):
    visited = []
    queue = []
    queue.append((r,c,0))
    delta = [(1,0),(0,1),(-1,0),(0,-1)]

    while queue:
        cr, cc, cd = queue.pop(0)

        if maze[cr][cc] == 3:
            return cd-1

        for i in delta:
            nr = cr + i[0]
            nc = cc + i[1]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and (nr,nc) not in visited:
                queue.append((nr,nc,cd+1))
                visited.append((nr,nc))
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for x in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s = (i,j)

    res = bfs(s[0],s[1])

    print('#{} {}'.format(tc, res))