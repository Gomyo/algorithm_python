def visit(r,c):
    i, j = 0, 0

    # i : 행의 길이
    while r+i < N and arr[r+i][c] != 0:
        i += 1
    # j : 열의 길이
    while c+j < N and arr[r][c+j] != 0:
        j += 1

    for a in range(r, r+i):
        for b in range(c, c+j):
            visited[a][b] = 1

    res.append([i,j])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    visited = [[0] * (N) for x in range(N)]
    res = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] and visited[i][j] == 0:
                visit(i,j)
    # sort
    res = sorted(res, key=lambda x: (x[0]*x[1], x[0]))

    print('#{} {}'.format(tc, len(res)), end=" ")
    for a,b in res:
        print(a,b, end=" ")
    print()
