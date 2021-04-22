T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for x in range(V+1)]

    for i in range(E):
        s, e = list(map(int, input().split()))
        adj[s] = e
        adj[e] = s

    print(adj)