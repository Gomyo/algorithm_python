def dfs(node):
    global res # 전역으로 결과 변수 사용
    visited[node] = True # 이 노드를 방문했다고 체크
    for i in graph[node]:
        if G in graph[i]: # 만약 goal node가 i와 이어져 있다면
            res = 1
            return
        dfs(i) # 이어져 있지 않다면 i에 대해 재귀적으로 DFS 실행. for문으로 실행되므로 가지치듯이 주루룩 내려간다.

def dfs2(node):
    visited[node] = 1
    if node == G:
        return 1

    for i in graph[node]:
        if not visited[i]:
            dfs2(i)

    return 0

T = int(input())

for tc in range(1, T+1):
    # V : Number of nodes
    # E : Number of edges
    V, E = map(int, input().split())
    visited = [False] * (V+1) # 아직 방문하지 않았다는 의미로 False로 초기화해준다.
    graph = [[] for x in range(V+1)] # Init graph
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    res = 0

    # S = Start node
    # G = Goal node
    S, G = map(int, input().split())

    # DFS
    res = dfs2(S)
    print('#{} {}'.format(tc, res))