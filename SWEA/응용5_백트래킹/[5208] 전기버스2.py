t = int(input())

def backtrack(idx, cnt):
    global res
    if cnt > res: return

    if idx >= N-1:
        if res > cnt:
            res = cnt
        return

    charge = bus_stop[idx]
    # for i in range(idx+1, charge+idx+1): # 정류장 별로 갈수있는 한계까지 for문으로 반복시켜준다.
    for i in range(charge+idx, idx, -1): # 위의 코드로는 안되는 이유는 뭘까? 가장 멀리 있는 경우부터 탐색하는 것이 실행시간 면에서 유의미한 차이가 있는 것일까?
        backtrack(i, cnt+1)

for tc in range(1, t+1):
    data = list(map(int, input().split()))
    N = data[0]
    bus_stop = data[1:]

    res = 2147483647
    backtrack(0,-1)

    print('#{} {}'.format(tc, res))