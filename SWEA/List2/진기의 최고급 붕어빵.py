T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명의 사람, M초마다 K개의 붕어빵 생산
    customer = list(map(int, input().split()))
    res = 'Possible'
    bbang = 0
    for i in range(11112): # 11111초 이내에 다 도착하니까. 이렇게 하면 손님을 정렬할 필요가 없다.
        if i and i%M == 0: # i가 0이 아니고 M초마다 생산된 붕어빵이면
            bbang += K
        if i in customer:
            if bbang:
                bbang -= 1
            else:
                res = 'Impossible'

    print('#{} {}'.format(tc, res))