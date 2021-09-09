arr = [1,2,3]
N = 3
sel = [0] * N
check = [0] * N

# check 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        # i번째 원소를 활용을 했군. 그럼 쓰면 안되지.
        if check & (1<<i): continue
        sel[idx] = arr[i]
        perm(idx+1, check | (1<<i)) # 원상복구가 필요없다
perm(0, 0)
