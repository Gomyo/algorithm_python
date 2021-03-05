def search_size(r,c):
    i, j = 0, 0

    # i : 행의 길이
    while r+i < N and arr[r+i][c] != 0:
        i += 1
    # j : 열의 길이
    while c+j < N and arr[r][c+j] != 0:
        j += 1

    res.append([i,j,i*j])
    init(r,c,i,j)

# 화학물질을 빈용기로 변환
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r + r_cnt):
        for j in range(c, c + c_cnt):
            arr[i][j] = 0

def counting_sort(idx):
    cnt = [0] * 10001
    rn = len(res)
    sort_res = [0] * rn

    # 1. 카운팅 하는 과정
    for i in range(rn):
        cnt[res[i][idx]] += 1

    # 2. 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 3. 정렬하여 넣는 과정
    for i in range(len(res)-1, -1, -1):
        sort_res[cnt[res[i][idx]]-1] = res[i]
        cnt[res[i][idx]] -= 1

    return sort_res

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    visited = [[0] * (N) for x in range(N)]
    res = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                search_size(i, j)

    res = counting_sort(0) # 행을 기준으로 정렬
    res = counting_sort(2) # 행렬의 크기로 다시한번 정렬

    print('#{} {}'.format(tc, len(res)), end=" ")
    for a,b,c in res:
        print('{} {}'.format(a, b), end=" ")
    print()