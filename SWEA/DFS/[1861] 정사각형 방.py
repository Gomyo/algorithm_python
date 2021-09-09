T = int(input())
delta = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(r,c,d):
    global res_val, res_start
    stack = [(r,c,d)]

    while stack:
        cr, cc, cd = stack.pop()

        if cd > res_val:
            res_val = cd
            res_start = data[r][c]

        elif cd == res_val and res_start > data[r][c]:
            res_start = data[r][c]

        for dr, dc in delta:
            nr = dr + cr
            nc = dc + cc
            if 0 <= nr < N and 0 <= nc < N and data[nr][nc] == data[cr][cc]+1:
                stack.append((nr,nc,cd+1))

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]
    res_val = 0
    res_start = -1
    visited = [[0]*N for x in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            visited[i][j] = 1
            dfs(i, j, 1)

    print('#{} {} {}'.format(tc,res_start,res_val))