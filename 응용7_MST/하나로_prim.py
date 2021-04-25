import sys
sys.stdin = open('하나로input.txt')

def prim(start):
    result = 0

    weight = [INF]*N
    weight[start] = 0

    visited = [0]*N

    for _ in range(N):
        min_w = INF
        min_v = -1
        for i in range(N):
            if not visited[i] and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        result += min_w
        visited[min_v] = 1

        # 새로 찾은 섬 기준, 최단 가중치 업데이트
        for i in range(N):
            # weight[i] = min(adj[min_v][i], weight[i])
            if adj[min_v][i] < weight[i] and not visited[i]:
                weight[i] = adj[min_v][i]

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    INF = float("inf") # 실수 값을 return해야 하는 문제의 경우 infinity 값을 float inf로 설정해야 한다.
    adj = [[INF]*N for x in range(N)]

    for i in range(N-1):
        for j in range(i+1, N):
            w = ((x_list[j] - x_list[i])**2 + (y_list[j]-y_list[i])**2)*E # 실수값을 미리 계산해 넣음으로 시간 단축
            adj[i][j] = w
            adj[j][i] = w
    prim(0)

    print('#{} {}'.format(tc, round(prim(0))))
