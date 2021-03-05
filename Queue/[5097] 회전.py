T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(M):
        arr.append(arr.pop(0))
    # 혹은, 아래와 같이 풀어도 된다.
    M %= N
    print(arr[M])
    print('#{} {}'.format(tc, arr[0]))