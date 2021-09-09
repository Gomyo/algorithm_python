# def paper_recursion(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     # 종이를 붙이자면, 바로 전의 종이에 20 X 10 크기 한장을 붙이는 것과
#     # 전전 종이에 20 X 10 두장 or 20 X 20 한장을 붙이는 두가지 경우
#     # 따라서 아래의 결과
#     return (paper_recursion(n - 1) + paper_recursion(n - 2) * 2)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     print(f'#{tc} {dp(N//10)}')
# Using dp
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    dp = list()
    dp.append(1)
    dp.append(3)
    for i in range(2, N // 10):
        dp.append(dp[i - 1] + dp[i - 2]*2)
    print(dp[N//10-1])