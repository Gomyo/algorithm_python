# # 5/10
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     cheese = list(map(int, input().split()))
#     data = []
#
#     for a,b in zip(cheese, range(M)):
#         data.append([a,b+1])
#
#     queue = data[:N] # 어디까지 세어 두었는지
#     cnt = 0
#     while len(queue) > 1:
#         if queue[0][0] >= 2:
#             queue[0][0] //= 2
#             queue.append(queue.pop(0))
#         else: # queue가 하나 빠지게 될 경우
#             queue.pop(0) # pop
#             if N+cnt < M: # 아직 피자가 남았다면 대기열의 피자 추가
#             # 인덱싱 했었으니까 N부터 시작해서 M보다 작을때까지 반복하면 됨
#                 N += cnt
#                 cnt += 1
#                 queue.append(data[N])
#     print('#{} {}'.format(tc, queue[0][1]))

# # 3/10
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     cheese = list(map(int, input().split()))
#     data = []
#
#     for a,b in zip(cheese, range(M)):
#         data.append([a,b+1])
#
#     queue = data[:N] # 어디까지 세어 두었는지
#     stack = data[N:] # 남은 피자
#
#     while len(queue) > 1:
#         queue[0][0] //= 2
#
#         if queue[0][0] >= 1:
#             queue.append(queue.pop(0))
#         else: # queue가 하나 빠지게 될 경우
#             queue.pop(0) # pop
#             if stack:
#                 queue.append(stack.pop())
#     print('#{} {}'.format(tc, queue[0][1]))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    data = []

    for a,b in zip(cheese, range(M)):
        data.append([a,b+1])

    queue = data[:N] # 어디까지 세어 두었는지
    cnt = 0
    while len(queue) > 1:
        if queue[0][0] >= 2:
            queue[0][0] //= 2
            queue.append(queue.pop(0))
        else: # queue가 하나 빠지게 될 경우
            queue.pop(0) # pop
            if N+cnt < M: # 아직 피자가 남았다면 대기열의 피자 추가
            # 인덱싱 했었으니까 N부터 시작해서 M보다 작을때까지 반복하면 됨
                cnt += 1 # 이 부분에서 실수했다!!
                queue.append(data[N+cnt-1])
    print('#{} {}'.format(tc, queue[0][1]))

'''
1
3 5
7 2 6 5 3
'''