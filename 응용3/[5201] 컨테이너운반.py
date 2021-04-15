import sys
sys.stdin = open('5201input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
    c_idx, t_idx = 0, 0

    while t_idx < M and c_idx < N:
        if containers[c_idx] <= trucks[t_idx]:
            t_idx += 1
            answer += containers[c_idx]
        c_idx += 1

    print('#{} {}'.format(tc, answer))