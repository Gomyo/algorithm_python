T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    res = 0
    max_val = 0

    for i in data[::-1]:
        if max_val < i:
            max_val = i
        else:
            res += max_val - i

    print('#{} {}'.format(tc, res))

'''
1
3
3 5 9
'''


