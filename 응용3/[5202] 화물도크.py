import sys
sys.stdin = open('5202input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    times = sorted([list(map(int, input().split())) for x in range(N)], key=lambda x:x[1], reverse=True)
    res = 0
    end_time = 0
    while times:
        s, e = times.pop()
        if s >= end_time:
            res += 1
            end_time = e
    print('#{} {}'.format(tc, res))

