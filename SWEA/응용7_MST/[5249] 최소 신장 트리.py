def prim(start):
    weight = [INF]*V
    weight[start] = 0
    visited = [0]*V
    st = [-1]*V
    result = 0

    for _ in range(V):
        min_w = 0xfffffff
        min_v = 0

        for v in range(V):
            if not visited[v] and weight[v] < min_w:
                min_w = weight[v]
                min_v = v

        visited[min_v] = 1
        result += min_w

        for v in range(V):
            if adj[min_v][v] < weight[v] and not visited[v]:
                weight[v] = adj[min_v][v]
                st[v] = min_v

    return result

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    V = V+1
    INF = 0xfffffff
    adj = [[INF]*(V) for x in range(V)]

    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
        adj[e][s] = w

    print('#{} {}'.format(tc, prim(0)))
