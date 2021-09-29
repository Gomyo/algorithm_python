from sys import stdin

R, C = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for x in range(R)]
visited = [[0]*C for x in range(R)]

# 'left', 'bottom', 'right', 'up'
head = [(0,-1), (1,0), (0,1), (-1,0)]

# 바라보는 방향 init
idx_head = 3 - d

result = 0

stack = [(r, c)]
while stack:
    cr, cc = stack.pop()

    if not visited[cr][cc]:
        visited[cr][cc] = 1
        result += 1
    able = False
    # 방향전환으로 갈 수 있는 방향 찾기
    # 왼쪽부터 가야 하므로 방향부터 옮기고 찾기
    for i in range(4):
        idx_head = (idx_head+1)%4
        # 갈 수 있으면 전진 (스택에 추가)
        nr, nc = cr + head[idx_head][0], cc + head[idx_head][1]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and not arr[nr][nc]:
            stack.append((nr, nc))
            able = True
            break

    # for문을 빠져나왔다는건 다 돌았는데도 갈데가 없다는 것
    # 후진 가능하면 후진
    br, bc = cr - head[idx_head][0], cc - head[idx_head][1]
    if not able:
        if 0 <= br < R and 0 <= bc < C and not arr[br][bc]:
            stack.append((br, bc))
print(result)