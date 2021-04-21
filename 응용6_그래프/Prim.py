# 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
# 1) 임의의 정점을 하나 선택해서 시작
# 2) 선택한 정점과 인접하는 정점들 중의 최소 배용의 간선이 존재하는 정점을 선택
# 3) 모든 정점이 선택될 때까지 1,2 과정을 반복

# 서로소인 2개의 집합(2 disjoint-set)의 정보 유지

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 6 25
2 4 46
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int, input().split())
INF = 0xfffffff

# 간선의 가중치를 저장하는 인접행렬
adj = [[INF]*(V) for x in range(V)]

for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w

# Prim 알고리즘을 통한 mst 가중치 얻어오기
def prim(start):
    # 1.임의의 노드 설정
    # 2.그 노드로부터 최소 가중치의 노드를 선택
    # 3.방문 여부 체크하면서 반복

    # 가중치를 저장하는 배열, 초기값은 최대값
    weight = [INF]*V
    weight[start] = 0

    # 어떤 노드를 선택했는지 표시하는 배열
    visited = [0] * V # 0이면 아직 선택되지 않은 노드

    # 최소 신장 트리의 가중치를 저장하는 변수
    result = 0
    # 어떤 노드가 어디에 연결되었는지 저장하는 배열
    st = [-1]*V

    # 가중치 선택
    for _ in range(V):
        # 현재까지 선택된 노드들에서 갈 수 있는 모든 경로를 탐색
        # 그 중에서 가중치가 제일 작은 경로를 선택
        min_w = 0xfffffff
        min_v = 0
        for v in range(V):
            # 방문하지 않았고 가중치가 최소인 경우
            if not visited[v] and weight[v] < min_w:
                min_w = weight[v]
                min_v = v

        visited[min_v] = 1
        result += min_w

        # 선택한 정점으로부터 갈 수 있는 경로를 살펴보고
        # 해당 노드를 선택하기 위한 가중치가 작아지면, 수정
        # 최단 가중치로 업데이트
        for v in range(V):
            # 현재의 정점(min_v)와 연결되어 있으며, 방문하지 않은 노드일 경우
            if adj[min_v][v] < weight[v] and not visited[v]:
                weight[v] = adj[min_v][v] # 도착 노드의 값을 간선의 값으로 채워넣음
                st[v] = min_v # 어느 노드에서 뻗어온 간선인지 저장(최소값으로 접근하려면 어떤 노드를 거쳐야 하는가)
    print(st)
    return result

print(prim(0))