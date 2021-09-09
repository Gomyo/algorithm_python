def backtracking(idx):
    global res, tmp
    if tmp > res: # 중간에 res값을 넘어버릴 경우 break
        return

    if idx == N:
        if tmp < res:
            res = tmp

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            # 생각해보니까 어차피 백트래킹이라, 아래 코드로 해도 상관없다.
            # tmp += arr[idx][i]

            tmp += arr[i][idx]
            backtracking(idx+1)
            visited[i] = 0 # False
            tmp -= arr[i][idx]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    visited = [0] * N
    res = 9999 # 최대값이 끽해야 100이다.
    tmp = 0
    backtracking(0)

    print('#{} {}'.format(tc, res))

'''
1
3
2 1 2
5 8 5
7 2 2
'''