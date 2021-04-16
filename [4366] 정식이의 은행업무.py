T = int(input())

for tc in range(1, T + 1):
    val2 = list(input())
    val3 = list(input())

    val2_result = set()
    val3_result = set()
    check = 0

    for i in range(len(val2)):
        for j in range(2):
            if val2[i] == str(j):
                continue
            tmp = val2[i]
            val2[i] = str(j)
            val2_result.add(int(''.join(val2), 2))
            val2[i] = tmp

    for i in range(len(val3)):
        if check:
            break
        for j in range(3):
            if val3[i] == str(j):
                continue
            tmp = val3[i]
            val3[i] = str(j)
            if int(''.join(val3), 3) in val2_result:
                res = int(''.join(val3), 3)
                check = 1
                break
            val3[i] = tmp

    print('#{} {}'.format(tc, res))