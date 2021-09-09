T = int(input())
for tc in range(1, T+1):
    N = float(input())
    res = ''
    cnt = -1

    while N:
        if N - 2**cnt >= 0:
            N = N - 2 ** cnt
            res += '1'
        else:
            res += '0'
        cnt -= 1

    if len(res) >= 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, res))