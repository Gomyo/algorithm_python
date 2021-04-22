#Dijkstra
#특정 정점에서 다른 나머지 정점까지 가는 최단거리를 구하는 알고리즘
#1. 각 정점까지 걸리는 시간을 최대로 설정(INF)
'''
6 10
1 2 3
1 3 4
2 4 5
3 2 1
3 4 4
3 5 5
4 5 3
4 6 4
5 1 3
5 6 5
'''
def dijkstra(start, adj, weight):
    #노드로 가는 비용이 확정된 노드들을 저장
    U = {start}
    #모든 노드들이 선택될때까지 아래를 반복
    #1. 현재 선택된 노드들을 통해서, 갈수있는 경로 중 최소 비용 경로를 선택
    #2. 새로운 노드가 선택되면 경로비용 업뎃
    while len(U) < V:
        min_w = 0xfffffff
        min_v = -1
        #weight 비용확인하면서 방문하지 않은 최소 비용 노드 탐색
        for i in range(1, V+1):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        #최소비용 노드를 찾았음
        U.add(min_v)
        for i in range(1, V+1):
            if i not in U: # 노드 비용 업데이트
                tmp = weight[min_v] + adj[min_v][i]
                if weight[i] > tmp:
                    weight[i] = tmp
    return weight

V, E = map(int,input().split())
INF = 0xfffffff
adj = [[INF]*(V+1) for _ in range(V+1)]
for i in range(E):
    s,e,w = map(int,input().split())
    adj[s][e] = w

#시작정점:1
start = 1
weight = adj[start][:] #인접행렬의 start행이 초기 weight
result = dijkstra(start, adj, weight)
print(result)