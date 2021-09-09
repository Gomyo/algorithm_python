# 순열로 구할 수도 있지만, 터지지 않는 조합으로 구하는 방법
# 253ms로 가장 빨랐다
def comb(idx, cnt, selected):
    global res

    if cnt == 2: # 두번 짤랐음
        # 만약 여기서 0,1이 나온다면
        total_cnt = 0
        # 0번째 index (첫 번째 행)은 하얀색, 1번째 index (두 번째 행)은 파란색, 그 아래는 모두 빨간색이라는 의미다.
        # index로 들어와있기 때문에 계산하기 위해 구분선마다 + 1을 해 준다.
        first_line = selected[0] + 1 # 첫 번째 구분선
        second_line = selected[1] + 1 # 두 번째 구분선

        # 하얀색
        for i in range(first_line):
            for j in flag[i]:
                if j != 'W':
                    total_cnt += 1

        # 파란색
        for i in range(first_line, second_line):
            for j in flag[i]:
                if j != 'B':
                    total_cnt += 1

        # 빨간색
        for i in range(second_line, N):
            for j in flag[i]:
                if j != 'R':
                    total_cnt += 1

        if res > total_cnt:
            res = total_cnt

        return

    # 만약 idx가 마지막 행이라면, Red Color가 보장되지 않으므로 return
    # ex) 첫 번째 구분선의 idx가 2일 경우, idx+1을 하면 3이 되어 맨 아랫줄의 빨간 부분을 보장할 수 없으므로 바로 return
    if idx == N-1:
        return

    # 현재 idx를 cnt(구분선의 index) 로 지정한 뒤, 구분선을 한개 지정했음을 반영하기 위해 cnt + 1을 해 준 뒤 재귀를 들어간다.
    selected[cnt] = idx
    comb(idx+1, cnt+1, selected)
    # idx만 올리고, cnt를 올리지 않고 재귀를 들어간다.
    # 이렇게 하여, 만약 N이 4일 경우 [0,1] 을 첫 번째 구분선으로 지정할 수 있게 된다.
    comb(idx+1, cnt, selected)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
    flag = [list(input()) for x in range(N)]
    res = 2147483647
    selected = [None, None]

    # 앞은 idx, 뒤는 idx들의 중간합
    comb(0, 0, selected)

    print('#{} {}'.format(tc, res))

'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''