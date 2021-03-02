T = 10

def dfs(v):
    stack = []
    visited = [False] * V
    stack.append(v)
    visited[v] = True

    while stack:
        top = stack[-1]
        if adj[top][99]: # top node와 99가 이어져 있을 경우
            return 1
        for i in range(V):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = True
                break
        else:
            stack.pop()
    return 0

def dfs2(v):
    for i in range(2):
        pass

for _ in range(1, T+1):
    V = 100
    tc, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adj = [[-1] * V for x in range(V)]

    for i in range(0, E*2, 2):
        s = edges[i]
        e = edges[i + 1]
        adj[s][e] = 1 # 일방통행 edge

    dfs2_edges = []

    res = dfs(0)
    print('#{} {}'.format(tc, res))

'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
'''