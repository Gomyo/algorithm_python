def bfs(v):
    global res
    visited = [False] * (V + 1)
    visited[v] = True
    queue = [(v, 0)]

    while queue:
        cv, cd = queue.pop(0) # queue인데 pop()했다 ㅋㅋ 근데도 8/10

        if cv == G:
            res = cd
            return

        for i in range(1, V+1):
            if adj[cv][i] and not visited[i]:
                queue.append((i, cd+1))
                visited[i] = True
    return

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for x in range(E)]
    S, G = map(int, input().split())
    adj = [[0] * (V + 1) for x in range(V + 1)]

    for i in range(E):
        # 양방향 연결
        a = edges[i][0]
        b = edges[i][1]
        adj[a][b] = 1
        adj[b][a] = 1

    res = 0
    bfs(S)

    print('#{} {}'.format(tc, res))

'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
'''