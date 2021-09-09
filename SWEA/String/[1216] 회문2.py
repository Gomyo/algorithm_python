# def data_refactor(data, N):
#     res = []
#     for j in range(N):
#         tmp = []
#         for i in range(N):
#             tmp.append(data[i][j])
#         res.append(tmp)
#     return res
#
# T = 10
#
# for tc in range(1, T+1):
#     n = int(input())
#     data = [list(input()) for x in range(100)]
#     data_col = data_refactor(data, 100)
#     # data_col = list(zip(*data))
#     res = 0
#
#     for r in range(100):
#         for c in range(100):
#             for k in range(c+1, 100):
#                 # index니까 k+1까지 인덱싱 해줘야 한다.
#                 tmp = data[r][c:k+1]
#                 if tmp == tmp[::-1]:
#                     if res < len(tmp):
#                         res = len(tmp)
#                 tmp = data_col[r][c:k+1]
#                 if tmp == tmp[::-1]:
#                     if res < len(tmp):
#                         res = len(tmp)
#
#     print('#{} {}'.format(tc, res))

# 다른사람 코드
def palindrome(M,N):
    global arry
    # M : 100 ~ 1
    # N : 100

    # 행 순회
    for i in range(N):
        # 0번 ~ 100번 반복
        for j in range(N - M + 1):
            # M // 2까지 반복. 회문이니까!
            for k in range(M // 2):
                # M : 100일 때
                # arry[0][0 + 0], arry[0][0 + 100 - 1 - 0]
                # arry[0][0 + 1], arry[0][0 + 100 - 1 - 1]
                # arry[0][0 + 2], arry[0][0 + 100 - 1 - 2]
                # arry[0][0 + 3], arry[0][0 + 100 - 1 - 3]
                # ...
                # arry[0][0 + 50], arry[0][0 + 100 - 1 - 50] 이러면 전체가 회문이라는 것이니까 return M = 50이 되는거고.
                # 계속 같았을 경우에만 else로 빠지는 것이다. 중간에 달라지면 break. else에 넣어 놔야 중간에 달라졌을 경우 M을 리턴하지 않는다.
                if arry[i][j + k] != arry[i][j + M - 1 - k]:
                    break
            else:
                return M
    # 열 순회
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(M // 2):
                if arry[i + k][j] != arry[i + M - 1 - k][j]:
                    break
            else:
                return M
    return 1
T = 10
for tc in range(1,T+1):
    text_number = int(input())
    arry = []
    N = 100
    # input
    for i in range(N):
        arry += [str(input())]
    # 100부터 하나씩 줄여나가면서 res 가져온다
    for i in range(N,1,-1):
        res = palindrome(i,N)
        # 만약 res가 1이 아니라면 ( 조사한 부분에 palindrome이 있다면 ) break
        if res != 1:
            break
    print('#{} {}'.format(tc, res))
