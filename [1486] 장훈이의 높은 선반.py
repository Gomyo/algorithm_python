T = int(input())

def dfs(cnt, h):
    global min_height

    if cnt == N:
        if h >= shelf:
            if h < min_height:
                min_height = h
        return

    dfs(cnt+1, h+height[cnt])
    dfs(cnt+1, h)


for tc in range(1, T+1):
    N, shelf = map(int, input().split())
    height = list(map(int, input().split()))

    min_height = 99999999
    dfs(0,0)
    res = min_height - shelf

    print('#{} {}'.format(tc, res))