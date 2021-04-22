from collections import deque
def bfs(v):
    global voted, result
    Q = deque([v])
    res = set()

    while Q:
        front = Q.popleft()
        if not voted[front]:
            res.add(front)
            voted[front] = 1

        for i in adj[front]:
            if not voted[i]:
                Q.append(i)
    if len(res) >= 2:
        result -= len(res)-1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[] for x in range(N+1)]
    voted = [0]*(N+1)
    result = N

    for i in range(0, 2*M, 2):
        s, e = data[i], data[i+1]
        adj[s].append(e)
        adj[e].append(s)

    for i in range(1, N+1):
        bfs(i)

    print('#{} {}'.format(tc, result))