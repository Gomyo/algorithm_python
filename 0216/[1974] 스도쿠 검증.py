def sudoku(arr, r, c):
    res = 1
    # 정방형 범위
    num = set()
    for i in range(3):
        for j in range(3):
            num.add(arr[r + i][c + j])
    if len(num) != 9:
        res = 0
    # 행
    num = set(arr[r])
    if len(num) != 9:
        res = 0
    # 열
    num = set()
    for i in range(9):
        num.add(arr[i][c])
    if len(num) != 9:
        res = 0

    return res

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for x in range(9)]
    res = 1

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            tmp = sudoku(arr, r, c)
            if tmp == 0:
                res = 0

    print(f'#{tc} {res}')