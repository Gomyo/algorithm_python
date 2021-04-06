T = 10

for _ in range(1, T+1):
    tc = int(input())
    pw = list(map(int, input().split()))
    dec = 1

    while pw[-1] > 0:
        pw.append(pw.pop(0) - dec)
        dec += 1
        if dec > 5:
            dec = 1

    pw[-1] = 0
    print('#{}'.format(tc), *pw)
