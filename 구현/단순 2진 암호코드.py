T = int(input())

for tc in range(1, T+1):
    R, C = map(int, input().split())

    data = [list(input()) for x in range(R)]

    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if data[i][j] == '1':
                code = data[i][j-55:j+1]
                break

    def converter(str):
        if str == '0001101':
            return 0
        elif str == '0011001':
            return 1
        elif str == '0010011':
            return 2
        elif str == '0111101':
            return 3
        elif str == '0100011':
            return 4
        elif str == '0110001':
            return 5
        elif str == '0101111':
            return 6
        elif str == '0111011':
            return 7
        elif str == '0110111':
            return 8
        elif str == '0001011':
            return 9

    isten = 0
    res = 0

    for i in range(0, 56, 7):
        if i%2:
            res += converter(''.join(code[i:i+7]))
            isten += converter(''.join(code[i:i+7]))
        else:
            res += converter(''.join(code[i:i+7]))
            isten += 3 * converter(''.join(code[i:i+7]))

    if not isten%10:
        print('#{} {}'.format(tc, res))
    else:
        print('#{} 0'.format(tc))

