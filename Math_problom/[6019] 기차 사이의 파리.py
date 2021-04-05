T = int(input())

for tc in range(1, T + 1):
    d, a, b, f = map(int, input().split())

    res = float((d / (a + b)) * f)
    print('#%d %0.6f' % (tc, res))

'''
1
250 10 15 20
'''