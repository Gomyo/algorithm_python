# 10분컷
def row_sum_max(arr):
    res = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if tmp > res:
            res = tmp
    return res

def col_sum_max(arr):
    res = 0
    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += arr[i][j]
        if tmp > res:
            res = tmp
    return res

def diagonal_sum(arr, direction):
    res = 0
    if direction == 'left':
        for i in range(100):
           res += arr[i][i]
        return res
    elif direction == 'right':
        for i in range(99, -1, -1):
            res += arr[99-i][i]
        return res

def ft_sum(arr):
    res = 0
    for i in arr:
        if res < i:
            res = i
    return res

T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for x in range(100)]

    row_sum = row_sum_max(arr)
    col_sum = col_sum_max(arr)
    left_diagonal_sum = diagonal_sum(arr, 'left')
    right_diagonal_sum = diagonal_sum(arr, 'right')

    print(f'#{tc} {ft_sum([row_sum, col_sum, left_diagonal_sum, right_diagonal_sum])}')
