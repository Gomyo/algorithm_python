T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    res = [0] * (N+1)
    for i in range(1, Q+1):
        l, r = list(map(int, input().split()))
        for idx in range(l, r+1):
            res[idx] = i
    # 왜 출력을 꼭 이렇게 unpacking으로 해야만 통과하는거야 ㅡㅡ
    print('#{}'.format(tc), *res[1:])