T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 바로 출력하지 않고 N*N 배열에 넣어서 출력
    arr = [[0]*n for x in range(n)]

    # 좌상우하 대각선으로 반틈 잘라서 아래쪽만 출력하면 된다
    for i in range(n):
        for j in range(i+1):
            if i == 0 or j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()
