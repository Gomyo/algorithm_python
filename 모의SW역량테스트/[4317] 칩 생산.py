# 지금 나에게는 어렵다.
# 격자 모양에서 2x2 종이를 최대한 많이 배치하고 싶다.
T = int(input())

def setNemo(dr, dc, val):
    global used
    used[dr][dc] = used[dr][dc+1] = used[dr+1][dc] = used[dr+1][dc+1] = val
    if val == 1:
        used[dr][dc] = 2

def isClean(dr, dc):
    global used
    if dc >= w - 1:
        return 0
    if data[dr][dc] + data[dr][dc+1] + data[dr+1][dc] + data[dr+1][dc+1] > 0:
        return 0
    if used[dr][dc] + used[dr][dc+1] + used[dr+1][dc] + used[dr+1][dc+1] > 0:
        return 0
    return 1

def getState(dr):
    global w
    state = 0

    for i in range(w - 1):
        state <<= 1
        if used[dr][i] == 2:
            state |= 0x1
    return state

def getMaxChipCnt(stage):
    global h, w, memo
    dr = int(stage / w)
    dc = stage % w
    state = 0

    if dr == h-2 and dc == w - 1:
        return 0
    # dc가 맨 끝에 도착하면
    if dc == w - 1:
        state = getState(dr)
        if memo[dr][state] != 0:
            return memo[dr][state]

    max_ret = 0
    # 네모 설치한다
    if isClean(dr, dc):
        setNemo(dr, dc, 1)
        max_ret = getMaxChipCnt(stage+1) + 1
        setNemo(dr, dc, 0)

    # 네모 설치 안한다
    ret = getMaxChipCnt(stage + 1)
    if ret > max_ret:
        max_ret = ret

    if dc == w-1:
        memo[dr][state] = max_ret
    return max_ret

for tc in range(1, T+1):
    h, w = map(int, input().split())

    # 1. 트리형태 ( branch 수와 level 수를 명확하게 )
    # 2. 가지치기. 재귀 문제는 used (used) 를 잘 써야 한다.
    data = [list(map(int, input().split())) for x in range(h)]
    used = [[0]*w for x in range(h)]
    memo = [[0]*((1 << h) + 10) for x in range(w)]

    result = getMaxChipCnt(0)

    print('#{} {}'.format(tc, result))

