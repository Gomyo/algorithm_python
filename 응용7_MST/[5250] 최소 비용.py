from collections import deque

def dijkstra(graph):
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    INF = 0xfffffff

    adj = [[INF]*(N) for x in range(N)] # 연료 소비
    # U = {(0,0):1} # node 비용 확정된 곳 체크

    adj[0][0] = 0
    Q = deque([(0,0)])

    while Q:
        r, c = Q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N:
                fuel = 1

                if graph[nr][nc] > graph[r][c]:
                    fuel += graph[nr][nc] - graph[r][c] # 높이차만큼 연료 추가

                if adj[nr][nc] > adj[r][c] + fuel: # 노드 비용 업데이트될 경우 append
                    adj[nr][nc] = adj[r][c] + fuel

                    Q.append((nr,nc))

    return adj[N-1][N-1]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]
    print('#{} {}'.format(tc, dijkstra(data)))
