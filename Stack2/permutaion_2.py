def comb(idx, cnt, selected):
    global res

    if cnt == 2:
        total_cnt = 0
        first_line = selected[0] + 1
        second_line = selected[1] + 1
        # 하얀색
        for i in range(first_line):
            for j in flag[i]:
                if j != 'W':
                    total_cnt += 1

        # 파란색
        for i in range(first_line, second_line):
            for j in flag[i]:
                if j != 'B':
                    total_cnt += 1

        # 빨간색
        for i in range(second_line, N):
            for j in flag[i]:
                if j != 'R':
                    total_cnt += 1

        if res > total_cnt:
            res = total_cnt

        return

    if idx  == N-1:
        return

    selected[cnt] = idx
    comb(idx+1, cnt+1, selected)
    comb(idx+1, cnt, selected)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N행 M열 , 최대 50행 50열
    flag = [list(input()) for x in range(N)]
    res = 2147483647
    selected = [None, None]

    comb(0, 0, selected)
    print('#{} {}'.format(tc, res))
