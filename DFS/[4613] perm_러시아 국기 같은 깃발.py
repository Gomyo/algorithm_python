def perm(idx, cur_sum):
    global res

    # 중간합이 주어진 N보다 커진다면 break해 주어야 한다.
    # 여기를 체크해 주지 않으면, 아래에서 경계선을 설정해 주는 부분에서 index error가 발생할 수 있다.
    # 전체 행의 길이보다 index의 중간합이 커졌다 == 경계선이 주어진 데이터의 범위를 넘어간다
    if N < cur_sum:
        return
    if idx == 3: # selected 배열이 꽉 찼으므로 탐색을 끝내야 한다
        # 효율화) 그런데 그냥 중간합이 N과 같은 경우에만 아래의 색깔 탐색을 수행하도록 하면 더 효율적이다.
        if cur_sum == N:
            # print(selected) # 경계선의 위치 체크
            a = selected[0] # 첫번째 경계선
            b = a + selected[1] # 두번째 경계선

            cnt = 0

            # 하얀색으로 색칠하는 부분
            # 여기서 flag[i] : 문자열 ex) WWBWB
            for i in range(a):
                for j in flag[i]:
                    if j != 'W':
                        cnt += 1
            # 파란색 부분
            for i in range(a, b):
                for j in flag[i]:
                    if j != 'B':
                        cnt += 1

            # 빨간색 부분
            for i in range(b, N):
                for j in flag[i]:
                    if j != 'R':
                        cnt += 1

            if cnt < res:
                res = cnt
        return

    # 중복 순열 DFS
    for i in range(1, N-1):
        selected[idx] = i
        perm(idx+1, cur_sum+i) # 인덱스 + 1로 재귀에 들어간다

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
    flag = [list(input()) for x in range(N)]
    res = 2147483647
    selected = [0] * 3

    # 앞은 idx, 뒤는 idx들의 중간합
    perm(0, 0)

    print('#{} {}'.format(tc, res))