T = int(input())

for tc in range(1, T+1):
    m = int(input())
    flag = 5
    coin = 50000
    res = []

    while coin >= 10:
        if m//coin:
            res.append(str(m//coin))
        else:
            res.append('0')
        m %= coin
        coin //= flag
        if flag == 2:
            flag = 5
        else:
            flag = 2
    print(f'#{tc}')
    print(' '.join(res))