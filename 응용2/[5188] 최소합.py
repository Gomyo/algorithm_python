T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for x in range(N)]
    dp = [[0]*N for x in range(N)]

    for i in range(N):
        for j in range(N):
            tmp = 0
            if 0 <= i-1 < N:
                if 0 <= j-1 <N:
                    if dp[i-1][j] <= dp[i][j-1]:
                        tmp = dp[i-1][j]
                    else:
                        tmp = dp[i][j-1]
                else:
                    tmp = dp[i-1][j]
            elif 0 <= j-1 < N:
                tmp = dp[i][j-1]
            dp[i][j] = tmp + data[i][j]

    print('#{} {}'.format(tc, dp[-1][-1]))