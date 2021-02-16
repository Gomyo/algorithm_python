def play(ladders, start):
    row = 0
    col = start
    while row < 99: # 사다리 게임 맨 밑에 도달하기 전까지
        # 왼쪽 or 오른쪽으로 빠지면 그쪽으로 쭉 가줘야 한다
        # 단축평가 개념을 활용, 인덱스 에러가 나지 않게 계속 체크해준다.
        if col < 99 and ladders[row][col + 1]:
            while col < 99 and ladders[row][col + 1]:
                col += 1
        elif col > 0 and ladders[row][col - 1]:
            while col > 0 and ladders[row][col - 1]:
                col -= 1
        # 아래로 내려갈 수 있으면 무조건 내려가는 동작을 왼쪽, 오른쪽 끝까지 간 뒤에 해야 한다.
        row += 1
    if ladders[row][col] == 2:
        return 1
    else:
        return 0

# 100 X 100 size of 2D Array
T = 10

for tc in range(1, T+1):
    n = int(input()) # test case's number
    ladders = [list(map(int, input().split())) for x in range(100)]

    # Using for loop,
    # start = index,
    # play(ladders, start) function,
    # start and end is pair. So I just check when it goes on 99th row
    for start in range(100):
        if ladders[0][start]:
            res = play(ladders, start)
            if res:
                print('#{} {}'.format(tc, start))
                break

'''output
#1 67
#2 45
#3 39
#4 24
#5 91
#6 93
#7 90
#8 4
#9 99
#10 35
'''