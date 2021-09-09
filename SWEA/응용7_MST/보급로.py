from collections import deque

def dijkstra(graph):
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    INF = 1e9
    adj = [[INF]*N for x in range(N)]

    adj[0][0] = 0
    Q = deque([(0,0,0)])
    while Q:
        cr, cc, cd = Q.popleft()

        # 방문체크. 최단거리가 정해져 있다면 그냥 PASS
        if cd > adj[cr][cc]:
            continue

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                cost = cd + graph[nr][nc]

                if adj[nr][nc] > cost:
                    adj[nr][nc] = cost
                    Q.append((nr,nc,cost))

    return adj[N-1][N-1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, list(input()))) for x in range(N)]
    print('#{} {}'.format(tc, dijkstra(data)))
