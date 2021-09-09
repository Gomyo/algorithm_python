T = int(input())

def cal(l_short, l_long):
    # 문제에 최저 값 조건이 없어서 최종 결과가 음수가 나오면 통과가 안되어야 하는데 우선 된다.
    res = 0

    for i in range(len(l_long) - len(l_short) + 1):
        tmp = 0
        for j in range(len(l_short)):
            tmp += l_short[j] * l_long[j + i]
        if res < tmp:
            res = tmp
    return res

for t in range(1, T + 1):
    n, m = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    res = 0

    if n < m:
        res = cal(aj, bj)
    else:
        res = cal(bj, aj)

    print(f'#{t} {res}')
