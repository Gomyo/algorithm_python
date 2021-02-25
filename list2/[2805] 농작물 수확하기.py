T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(input()) for x in range(N)]
    m = N//2 # 7 -> 3
    # 3 2 1 0 1 2 3
    # 0 1 2 3 4 5 6
    # 1 6
    # 2 5
    # 3 4
    res = 0

    for i in range(N):
        if i < m:
            # i = 0, 1, 2
            for j in range(m-i, m+i+1):
                res += int(farm[i][j])
        elif i > m:
            # 4 = 1, 6 => 2
            # 5 = 2, 7 => 1
            # 6 = 3, 8 => 0
            # 2*m - i
            tmp = 2*m - i
            for j in range(m-tmp, m+tmp+1):
                res += int(farm[i][j])
        else:
            for j in range(N):
                res += int(farm[i][j])

    print('#{} {}'.format(tc, res))
'''
1
5
14054
44250
02032
51204
52212
'''