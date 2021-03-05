T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
    arr = [list(input()) for x in range(N)]
    end = len(arr)
    min_val = 2147483647

    w_count = 0
    for w in range(end-2):
        for i in range(M):
            if arr[w][i] != 'W':
                w_count += 1

        b_count = 0
        for b in range(w+1, end-1):
            for j in range(M):
                if arr[b][j] != 'B':
                    b_count += 1

            # 마지막을 무조건 끝까지 red로 칠해야 한다.
            # 따라서 blue 이후 모든 곳을 red로 칠한 뒤, tmp를 계산해 줘야 한다.
            # w_count, b_count의 경우와 약간 다르다.
            r_count = 0
            for r in range(b+1, end):
                for k in range(M):
                    if arr[r][k] != 'R':
                        r_count += 1

            tmp = w_count + b_count + r_count
            if min_val > tmp:
                min_val = tmp

    print('#{} {}'.format(tc, min_val))

'''
1
4 5
WRWRW
BWRWB
WRWRW
RWBWR
'''