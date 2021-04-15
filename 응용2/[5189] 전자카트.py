import sys
sys.stdin = open('5189.txt')

def dfs(idx, cnt, val):
    global result

    if cnt == N-1:
        val += data[idx][0] # 마지막에는 사무실로 돌아와야 함
        if val < result:
            result = val
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1, val+data[idx][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]
    visited = [0] * N
    result = 999999
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, result))