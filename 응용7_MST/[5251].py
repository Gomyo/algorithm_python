def dijkstra(start):
    INF = 0xfffffff
    adj = {x: [] for x in range(V+1)}
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e,w))

    weight = [INF]*(V+1)
    selected = [0] * (V+1)

    U = 0
    weight[0] = 0

    while U < V:
        min_w = INF
        min_v = -1
        for i in range(V+1):
            if not selected[i] and weight[i] < min_w:
                min_w = weight[i]
                min_v = i
        U += 1
        selected[min_v] = 1

        for e, w in adj[min_v]:
            tmp = weight[min_v] + w
            if weight[e] > tmp:
                weight[e] = tmp
    return weight[V]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    print('#{} {}'.format(tc, dijkstra(0)))