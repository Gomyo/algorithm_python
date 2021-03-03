#연습문제3
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V = 7
E = 8
adj  = [[0]*(V+1) for _ in range(V+1)]
#인접행렬 만들기
for i in range(0,E*2,2):
    a,b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1

#s : 시작 정점
def bfs(s):
    #bfs는 먼저 방문한 정점이 먼저 버려진다. >> Queue를 사용하면 된다.
    queue = list()
    #한 번 방문한 정점을 확인하기 위한 visited
    visited = [False] * (V+1)
    queue.append(s)
    visited[s] = True

    #1. 가장 먼저 방문한 정점을 방문 : queue에서 가장앞에 있는 정점을 방문
    #2. 해당 정점에서 방문할 수 있는 모든 경로를 저장 : queue에 순서대로 넣어줌
    #3. 1~2번을 queue가 빌때 까지 반복한다.
    while queue:
        front = queue.pop(0)    #queue에서 가장 앞에 있는 정점을 가져옴
        #front에서 갈 수 있는 경로를 탐색
        print(front, end=" ")
        print(adj[front])
        for i in range(1,V+1):
            # 인접행렬이 1이면 경로가 있는 것, 방문하지 않은 정점
            if adj[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
    print()
#s : 시작 정점
def bfs2(s):
    #bfs는 먼저 방문한 정점이 먼저 버려진다. >> Queue를 사용하면 된다.
    queue = list()
    #한 번 방문한 정점을 확인하기 위한 visited
    visited = [False] * (V+1)
    queue.append(s)
    visited[s] = True

    #1. 가장 먼저 방문한 정점을 방문 : queue에서 가장앞에 있는 정점을 방문
    #2. 해당 정점에서 방문할 수 있는 모든 경로를 저장 : queue에 순서대로 넣어줌
    #3. 1~2번을 queue가 빌때 까지 반복한다.
    while queue:
        front = queue.pop(0)    #queue에서 가장 앞에 있는 정점을 가져옴
        #front에서 갈 수 있는 경로를 탐색
        print(front, end=" ")
        print(adj[front])
        for i in adj[front]:
            # 인접행렬이 1이면 경로가 있는 것, 방문하지 않은 정점
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print()

bfs(5)
bfs2(5)