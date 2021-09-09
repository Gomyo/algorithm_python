data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7   #노드(정점)의 개수
#인접리스트
adj=[[] for _ in range(N+1)]

for i in range(0,len(data),2):
    #무향 그래프 이므로 양쪽에 모두 추가
    s = data[i]
    e = data[i+1]
    adj[s].append(e)
    adj[e].append(s)

def dfs(v, visited):
    visited[v] = 1
    result = [v]

    for i in adj[v]:
        if not visited[i]:
            result += dfs(i, visited)

    return result

res = dfs(1, [0]*(N+1))
print(res)