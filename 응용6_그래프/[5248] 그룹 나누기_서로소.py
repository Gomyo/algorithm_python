def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x,y):
    p[find_set(x)] = find_set(y)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    data = list(map(int, input().split()))

    for i in range(0, 2*M, 2):
        union(data[i], data[i+1])

    res = set()

    for i in p[1:]:
        res.add(find_set(i))

    print('#{} {}'.format(tc, len(res)))