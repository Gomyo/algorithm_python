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

from collections import deque

result = []

def bfs(s):
    global result
    visited = [0]*(N+1)
    queue = deque([s])
    visited[s] = 1

    while queue:
        front = queue.popleft()
        result.append(front)
        for i in adj[front]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
bfs(1)
print(result)
