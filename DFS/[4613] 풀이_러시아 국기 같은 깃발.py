# def perm(idx, sub_sum):
#     global res
#     # 유망성 검사
#     if sub_sum > N:
#         return
#
#     if idx == 3:
#         if sub_sum == N:
#             cnt = 0
#
#             st = sel[0]
#             st2 = st + sel[1]
#
#             # 흰색 칠하기
#             for i in flag[:st]:
#                 for j in i:
#                     if j != 'W':
#                         cnt += 1
#
#             # 파란색 칠하기
#             for i in flag[st:st2]:
#                 for j in i:
#                     if j != 'B':
#                         cnt += 1
#
#             # 빨간색 칠하기
#             for i in flag[st2:]:
#                 for j in i:
#                     if j != 'R':
#                         cnt += 1
#
#             if res > cnt:
#                 res = cnt
#         return
#
#     # 중복순열 살짝응용
#     # N이 4라면 맨 위, 맨 아래는 고정되어야 하므로 N-1까지 두어야 한다.
#     for i in range(1, N-1):
#         sel[idx] = i
#         perm(idx+1, sub_sum+i)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
#     flag = [list(input()) for x in range(N)]
#     res = 214748364
#     sel = [0] * 3
#
#     # 앞은 idx, 뒤는 중간합
#     perm(0, 0)
#
#     print('#{} {}'.format(tc, res))
#
# #############################################################################################
# # 누적합 풀이
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
#     flag = [input() for x in range(N)]
#
#     res = 214748364
#
#     W = [0] * N
#     B = [0] * N
#     R = [0] * N
#
#     # 나와 다른 색깔의 개수를 카운트
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 W[i] += 1
#             if flag[i][j] != 'B':
#                 B[i] += 1
#             if flag[i][j] != 'R':
#                 R[i] += 1
#
#     # 누적합
#     for i in range(1, N):
#         W[i] += W[i-1]
#         B[i] += B[i-1]
#         R[i] += R[i-1]
#
#     # 각각의 색별로 한 줄 이상씩은 확보해야 하니까
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             w_cnt = W[i]
#             b_cnt = B[j] - B[i] # i층 까지는 흰색을 칠해 두었으니까
#             r_cnt = R[N-1] - R[j]
#
#             if ans > w_cnt + b_cnt + r_cnt:
#                 ans = w_cnt + b_cnt + r_cnt


###########################################################################
# 조합 풀이

# 고를 수 있는 idx의 개수는 전체 길이 N-2개이다.
# 세 영역으로 구분하기 위해서는 두 개의 구분선이 필요하다
# 구분선의 값을 2개 선택해 주면 된다.
# 전체 행에서 첫, 마지막 줄을 제외하고 2개 선택하는 거니까, 전체 집합에서 요소를 N-2개 선택하는 조합이다.
# idx : 자르려고 하는 행의 번호
# cnt : 자른 행의 개수
# 자른 행을 저장하는 배열
def comb(selected, idx, cnt):
    global res

    if cnt == 2:
        # 모든 선택이 끝났음
        # 흰색 영역
        w_cnt = 0
        a = selected[0]+1
        b = selected[1]+1
        for i in range(a):
            for j in range(M):
                if flag[i][j] != 'W':
                    w_cnt += 1
            pass
        b_cnt = 0
        # 파란색 영역
        for i in range(a,b):
            for j in range(M):
                if flag[i][j] != 'B':
                    b_cnt += 1
        r_cnt = 0
        for i in range(b,N):
            for j in range(M):
                if flag[i][j] != 'R':
                    r_cnt += 1
        tmp = w_cnt + b_cnt + r_cnt

        if res > tmp:
            res = tmp
        return
    if idx == N-1: # 마지막 줄은 구분선이 될 수 없으므로
        return
    # 각 행을 자를지 말지 결정
    # idx 행을 자르기
    selected[cnt] = idx # cnt번째 자른 행을 저장한다.
    comb(selected, idx+1, cnt+1)
    # idx 행을 자르지 않기
    comb(selected, idx+1, cnt)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열 , 최대 50행 50열
    flag = [input() for x in range(N)]
    # selected의 값은 구분선으로 사용하려는 행 번호
    selected = [-1] * 2
    res = 9999

    comb(selected, 0, 0)
    print('#{} {}'.format(tc, res))