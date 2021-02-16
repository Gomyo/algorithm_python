def kill_fly(arr, r, c, w):
    res = 0
    for i in range(w):
        for j in range(w):
            res += arr[i + r][j + c]
    return res

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    res = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            kill = kill_fly(arr, r, c, M)
            if kill > res:
                res = kill
    print(f'#{tc} {res}')
'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''