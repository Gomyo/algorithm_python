T = int(input())

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x,y):
    p[find_set(x)] = find_set(y)

for tc in range(1, T+1):
    V, E = map(int, input().split())
    p = list(range(V+1))

    for i in range(E):
        s, e = map(int, input().split())
        union(s,e)

    res = set()
    for i in p[1:]:
        res.add(find_set(i))
    print('#{} {}'.format(tc, len(res)))