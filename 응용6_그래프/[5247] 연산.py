T = int(input())

def cal(num, oper):
    if oper == 0:
        return num + 1
    elif oper == 1:
        return num - 1
    elif oper == 2:
        return num * 2
    else:
        return num - 10

from collections import deque

def bfs(n):
    global result, dup_dict
    Q = deque([(n, 0)])

    while Q:
        val, cnt = Q.popleft()

        if val == R:
            result = cnt
            return

        for i in range(4):
            tmp = cal(val, i)
            if 0 < tmp <= 1000000 and dup_dict.get(tmp) is None:
                Q.append((tmp, cnt+1))
                dup_dict[tmp] = 1

for tc in range(1, T+1):
    N, R = map(int, input().split())
    result = 0
    # 같은 수의 중복연산을 막기 위해 체크하는 딕셔너리
    dup_dict = {}
    bfs(N)
    print('#{} {}'.format(tc, result))