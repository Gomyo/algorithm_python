T = int(input())

for t in range(1, T+1):
    purple = [[0 for x in range(11)] for y in range(11)]
    res = 0

    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 좌표로 볼 때, 모눈종이의 정 중앙을 좌표라고 생각하면 보다 풀기 편하다.
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                purple[x][y] += color
                if purple[x][y] == 3:
                    # It's PURPLE!!
                    res += 1
    print(f'#{t} {res}')

'''input
1
2
2 2 4 4 1
3 3 6 6 2
1
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''
