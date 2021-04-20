T = int(input())

def dfs(idx, val):
    global res

    if val <= res: return

    if idx == N:
        if res < val:
            res = val
        return

    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            dfs(idx+1, val*data[idx][i])
            selected[i] = 0

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(lambda x:int(x)/100, input().split())) for x in range(N)]
    selected = [0]*N
    res = 0
    dfs(0,100)
    print('#{} {:6f}'.format(tc, res))