def data_refactor(data, N):
    res = []
    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(data[i][j])
        res.append(tmp)
    return res

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    arr2 = data_refactor(arr, N)
    res = 0

    for i in range(N):
        cnt = 0
        cnt2 = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if not arr[i][j] or j == N-1:
                if cnt == K:
                    res += 1
                cnt = 0
            if arr2[i][j]:
                cnt2 += 1
            if not arr2[i][j] or j == N-1:
                if cnt2 == K:
                    res += 1
                cnt2 = 0

    print(f'#{tc} {res}')