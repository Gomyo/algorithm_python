T = int(input())

arr = [[0 for x in range(T)] for y in range(T)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
direction = 0
cnt = 1
go = T
r, c = 0, 0

for i in range(2*T-1):
    if direction%4 == 0:
        for j in range(go):
            arr[r][c] = cnt
            cnt += 1
            c += dc[direction%4]
        c -= 1 # 다음 칸으로 이동해 있어야 하므로 (1, 4) 값 변환
        r += 1 # 1 올려줌
        go -= 1
        direction += 1
    elif direction%4 == 1:
        for j in range(go):
            arr[r][c] = cnt
            cnt += 1
            r += dr[direction%4]
        r -= 1 # 아래쪽으로 가다가 왼쪽으로 가야하므로 둘다 줄인다
        c -= 1
        direction += 1
    elif direction%4 == 2:
        for j in range(go):
            arr[r][c] = cnt
            cnt += 1
            c += dc[direction%4]
        c += 1 # 왼쪽으로 가다가 위쪽으로 가야하므로 c 하나 더해주고
        r -= 1
        go -= 1
        direction += 1
    elif direction%4 == 3:
        for j in range(go):
            arr[r][c] = cnt
            cnt += 1
            r += dr[direction%4]
        r += 1
        c += 1
        direction += 1

for i in arr:
    for j in i:
        print('%3d' %j, end=" ")
    print()



