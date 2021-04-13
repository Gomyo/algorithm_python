import sys
from pprint import pprint

sys.stdin = open('전원연결input.txt', 'r')

T = int(input())

delta = [(0,1), (0,-1), (1,0), (-1,0)]

def connect(point, data, r, c):
    res = 0
    cr, cc = point
    while True:
        nr = cr + r
        nc = cc + c
        if data[nr][nc] == 1:
            return 0
        elif nr < 0 or nr >= N or nc < 0 or nc >= N: # power와 연결 완료
            return res
        else:
            res += 1 # 전선길이 1 증가
            data[nr][nc] = 1
    return 0


def dfs(idx, line_sum, data, connected_cores):
    global res, line_res

    if idx == E:
        pprint(data)
        # 여기서 tmp 체크
        if connected_cores > res:
            line_res = line_sum
            res = connected_cores
            return
        elif connected_cores == res:
            if line_sum < line_res:
                line_res = line_sum
                return
    else:
        for dr, dc in delta:
            line_tmp = connect(cores[idx], data, dr, dc)
            # 그 방향으로 갔을 때 연결 가능
            if line_tmp:
                dfs(idx+1, line_sum+line_tmp, data, connected_cores+1)
            # 그쪽 방향으로 연결 불가. 다음 코어로 이동
            else:
                dfs(idx+1, line_sum, data, connected_cores)
    return

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]

    cores = []

    # N-1 by N-1의 '1'만 Core로 체크하면 된다.
    for i in range(1, N-1):
        for j in range(1, N-1):
            if data[i][j]:
                cores.append((i,j))
    res = 0
    line_res = 2000
    E = len(cores)

    # cores를 순회하면서 dfs
    dfs(0, 0, data, 0)

    line = 0

    print(res)