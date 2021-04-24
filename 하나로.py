import heapq

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x,y):
    a = find_set(x)
    b = find_set(y)

    if a > b:
        p[a] = b
    else:
        p[b] = a

def kruscal(data):
    result = 0

    while data:
        d, a, b = heapq.heappop(data)
        if find_set(a) == find_set(b): continue
        result += d
        union(a,b)

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    data = list()
    p = list(range(N)) # 서로소 집합
    E = float(input())

    for i in range(N):
        for j in range(i+1, N):
            distance = ((x[i] - x[j])**2 + (y[i] - y[j])**2)*E
            heapq.heappush(data, (distance, i, j))

    res = int(kruscal(data) + 0.5)
    print('#{} {}'.format(tc, res))
