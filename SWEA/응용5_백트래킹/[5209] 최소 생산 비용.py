T = int(input())

def dfs(idx, val):
    global res

    if val >= res:
        return

    if idx == N:
        if res > val:
            res = val
        return

    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            dfs(idx+1, val+data[idx][i])
            selected[i] = 0

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]

    res = 2147483647
    selected = [0]*N
    dfs(0,0)
    print('#{} {}'.format(tc, res))