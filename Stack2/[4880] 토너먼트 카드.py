#
# 이 모든 뻘짓을 할 필요 없이
# idx만 사용해서 인덱싱으로 풀면 된다.
#
def rcp(l, r):
    l_val = l[1]
    r_val = r[1]
    # 축약
    if (l_val == '1' and r_val == '2') or (l_val == '2' and r_val == '3') or (l_val == '3' and r_val == '1'):
        return r
    else:
        return l

    # if l_val == '1': # 가위
    #     if r_val == '2':
    #         return r
    #     else:
    #         return l
    # elif l_val == '2': # 바위
    #     if r_val == '3':
    #         return r
    #     else:
    #         return l
    # else: # 보
    #     if r_val == '1':
    #         return r
    #     else:
    #         return l

def tournament(arr):
    if len(arr) <= 1:
        return arr[0] # 여기서 1차원 배열로 리턴해줘야 함
    # 재귀
    pivot = (len(arr)+1)//2 # 1 fail! 여기서 조건을 맞추어줘야 함. (i+j)//2 i가 1이었다...;; 문제 설명이 빈약쓰

    left, right = arr[:pivot], arr[pivot:] # 2차원 배열로 나뉘어지고 있음

    return rcp(tournament(left), tournament(right))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    # index, value 형태로 recursion
    data = []
    for i in range(N):
        data.append([i+1,cards[i]])

    print('#{} {}'.format(tc, tournament(data)[0]))

'''
1
6
2 1 1 2 3 3

3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''