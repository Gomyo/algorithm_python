#이차원 배열에서의 BFS
arr = [[1,1,0,0,0,0],
       [0,1,1,1,1,0],
       [0,0,3,0,1,1],
       [0,0,0,0,1,0],
       [0,0,2,1,1,0],
       [0,0,0,0,0,0]]
N = 6
visited = [[0]*N for _ in range(N)]

def bfs(r,c):
    # 2차원 배열에서는 정점의 구분을 좌표로
    queue = []
    visited = [[0] * N for x in range(N)]
    # (r,c,d) d : 시작지점으로부터의 거리
    queue.append(r,c,0,'')
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    # 방문하는 정점을 dequeue -> front로
    # 갈 수 있는 경로가 있으면 enqueue
    visited[r][c] = 1

    # 도착지까지 거리 구하기
    # queue에 현재 좌표만 저장하는게 아니라 시작지점에서 얼마나 떨어졌는지 정보도 같이 저장
    while queue:
        # 현재까지의 거리 받아옴
        cr,cc,cd,path = queue.pop(0)
        path += str(r) + str(c)
        print((cr,cc,cd,path))

        if arr[cr][cc] == 2:
            return '도착'

        # 4방향 경로 탐색
        for dr,dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0 and not visited[nr][nc]:
                # queue에 추가
                # 방문했음을 표시
                # 다음 위치까지의 거리는 cd + 1
                queue.append((nr, nc, cd+1, path + str(nr) + str(nc)))
                path.append((nr,nc))
                visited[nr][nc] = 1

    return '도착 못함'

for i in range(N):
    for j in range(N):
        if arr[i][j] == 3:
            s = [i, j]
        elif arr[i][j] == 2:
            e = [i, j]

print(bfs(2,2))