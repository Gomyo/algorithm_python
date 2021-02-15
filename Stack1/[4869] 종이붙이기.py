def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    # 종이를 붙이자면, 바로 전의 종이에 20 X 10 크기 한장을 붙이는 것과
    # 전전 종이에 20 X 10 두장 or 20 X 20 한장을 붙이는 두가지 경우
    # 따라서 아래의 결과
    return (dp(n - 1) + dp(n - 2) * 2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {dp(N//10)}')
