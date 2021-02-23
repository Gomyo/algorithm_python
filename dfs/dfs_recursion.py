# 인접행렬(adjacency matrix)을 이용해서 그래프 표현이 가능
# 정점의 개수  : 7
# 간선의 개수 :  8
V = 7
E = 8
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 인접행렬은 인덱스의 번호를 정점의 번호와 매칭시켜서 사용
# 정점이 1번부터 시작이라면, 정점의 개수보다 1더큰 크기의 인접행렬을 사용
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 2개의 정점정보가 한 쌍이니까 2개씩 읽어옴
for i in range(0, E * 2, 2):
    s = edges[i]
    e = edges[i + 1]
    adj[s][e] = 1
    adj[e][s] = 1

visited = [False] * (V+1)
def dfs(v):
    # 현재 정점을 방문했음을 표시
    visited[v] = True
    print(v, end=' ')
    # 현재 정점에서 갈 수 있는 경로를 확인
    for i in range(1, V+1):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i)
dfs(1)