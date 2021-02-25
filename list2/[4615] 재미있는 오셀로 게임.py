from pprint import pprint
T = int(input())
# 12시부터 시계방향으로 8방향
delta = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 0: init 1: black 2: white
    othello = [[0] * (N+1) for x in range(N+1)]
    # 정가운데 배치
    n = N//2
    othello[n][n], othello[n+1][n+1], othello[n+1][n], othello[n][n+1] = 2,2,1,1
    for _ in range(M):
        x,y,c = map(int, input().split())
        othello[x][y] = c

        for i in range(8): # 8방향
            dx, dy = x + delta[i][0], y + delta[i][1] # 돌은 놓았으니 한번 움직인다.
            stack = []
            while True:
                if dx > N or dy > N or dx < 1 or dy < 1: # 보드 범위를 벗어났을 때도 비워줘야됨 아ㅋㅋㅋㅋ
                    stack = []
                    break
                if othello[dx][dy] == 0: # 빈칸을 만났을 때는 스택을 비워줘야 한다.
                    stack = []
                    break
                if othello[dx][dy] == c: # 자기 색이 나오거나
                    break
                # 위 경우를 제외하고는 뒤집어준다.
                else:
                    stack.append((dx,dy))
                dx, dy = dx+delta[i][0], dy+delta[i][1]

            for a, b in stack: # 여기서 x, y를 쓰면 기본 좌표가 바뀌어버린다.
                if c == 1:
                    othello[a][b] = 1
                else:
                    othello[a][b] = 2
            print()
            pprint(othello)
    b, w = 0, 0

    for x in range(1, N+1):
        for y in range(1, N+1):
            if othello[x][y] == 1:
                b += 1
            elif othello[x][y] == 2:
                w += 1

    print('#{} {} {}'.format(tc, b, w))
