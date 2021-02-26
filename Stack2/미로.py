def dfs(r,c):
    global res

    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if (r,c) == (e[0],e[1]):
        res = 1
        return

    visited.append((r,c))
    for i in delta:
        nx = r + i[0]
        ny = c + i[1]
        if 0 <= nx < N and 0 <= ny < N and (maze[nx][ny] == 0 or maze[nx][ny] == 3) and (nx, ny) not in visited:
            dfs(nx, ny)
    return e

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 12345 -> int, input() 으로 가져오면 알아서 잘려서 들어온다.
    maze = [list(map(int, input())) for x in range(N)]
    res = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s = (i, j)
            elif maze[i][j] == 3:
                e = (i, j)
    visited = []
    dfs(s[0],s[1])
    print('#{} {}'.format(tc, res))

'''
1
5
13101
10101
10101
10101
10021
'''