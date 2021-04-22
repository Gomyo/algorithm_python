T = int(input())

def dfs(node, cnt):
    global result
    visited[node] = 1
    if cnt > result:
        result = cnt

    for i in range(1, V+1):
        if adj[node][i] and not visited[i]:
            dfs(i, cnt+1)
    # 다른 경로를 통해서 노드를 재방문할 수 있도록 해 주어야 한다.
    visited[node] = 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for x in range(V+1)]
    result = 0

    for i in range(E):
        s, e = list(map(int, input().split()))
        adj[s][e] = 1
        adj[e][s] = 1

    visited = [0]*(V+1)

    for i in range(1, V+1):
        dfs(i, 1)

    print('#{} {}'.format(tc, result))

'''
반례
1
6 6
1 2
2 3
2 5
3 4
3 6
5 6
'''