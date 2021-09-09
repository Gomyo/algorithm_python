T = int(input())

def cal(v):
    if v >= 2:
        tree[v//2] += tree[v]

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N,1,-1):
        cal(i)

    print("#{} {}".format(tc, tree[L]))