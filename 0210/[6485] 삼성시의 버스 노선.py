'''
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    # res 최대값만큼 초기화
    bus_data = [0] * 5001

    # 노선 몇개 지나가는가
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            bus_data[j] += 1

    # 정류장의 수
    P = int(input())
    # 정류장. 이거 필요없는데 왜 받는거지?
    # 틀려보니까 알겠다. 정류장이 겹쳐서 나올 수가 있음.

    result = []
    for i in range(P):
        result.append(bus_data[int(input())])

    print(f'#{t}', *result)
'''

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    bus_route = []
    for i in range(N):
        a, b = map(int, input().split())
        bus_route.append([a,b])

    # 결과용으로 초기화
    res = [0] * 5001
    for a,b in bus_route:
        for i in range(a, b + 1):
            res[i] += 1

    # 정류장의 수
    # 정류장. 이거 필요없는데 왜 받는거지?
    P = int(input())
    result = []

    for i in range(P):
        result.append(res[int(input())])
    print(f'#{t}', *result)
    # 아래와 같이 print하는것도 가능
    '''
    print('#{}'.format(t), end=" ")
    for i in range(P):
        print(res[int(input())], end=" ")
    print()#\n 넣어주기
    '''

    # 아래처럼 출력하면 틀린다. 정수라 그런가...
    # for i in range(P):
    #     result += str(res[int(input())])
    # print(f'#{t} {" ".join(result)}')
