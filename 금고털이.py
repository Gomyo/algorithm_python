T = int(input())

def dfs(depth, ret):
    global res

    if ret >= res:
        return
    if depth >= 4:
        if ret < res:
            res = ret
        return

    # 시계방향 이동
    tmp1 = ord(before[depth]) - ord(after[depth])

    if tmp1 < 0:
        tmp1 += 26

    ret += tmp1 * (depth*2+1)
    dfs(depth+1, ret)
    ret -= tmp1 * (depth*2+1)

    # 반시계방향 이동
    tmp2 = ord(after[depth]) - ord(before[depth])

    if tmp2 < 0:
        tmp2 += 26

    cal2 = (depth*2)
    if cal2 < 1:
        cal2 = 1
    ret += tmp2 * cal2

    dfs(depth+1, ret)

for tc in range(1, T+1):
    before = input()
    after = input()
    # 시 반
    # 1, 1
    # 3, 2
    # 5, 4
    # 7, 6
    res = 1e9
    dfs(0, 0)
    print('#{} {}'.format(tc, res))


