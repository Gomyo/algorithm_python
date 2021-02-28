day = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for _ in range(T):
    tc, n = map(str, input().split())
    res = {}
    for i in day:
        res[i] = 0
    data = list(map(str, input().split()))
    for i in data:
        res[i] += 1
    print(tc)
    for i in res:
        for j in range(res[i]):
            print(i, end=' ')