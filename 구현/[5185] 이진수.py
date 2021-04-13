T = int(input())
for tc in range(1, T+1):
    N, hex = input().split()
    res = ''
    for c in hex:
        val = bin(int(c, 16))[2:]
        zero = 4 - len(val)
        res += zero*'0'+val

    print('#{} {}'.format(tc, res))