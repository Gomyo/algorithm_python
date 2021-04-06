T = int(input())

def preorder(v):
    global res
    if v <= E+2 and tree[v]:
        res += 1
        preorder(left[v])
        preorder(right[v])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    tree = [x for x in range(E+2)]

    for i in range(0, E*2, 2):
        parent = data[i]
        child = data[i+1]

        if left[parent]:
            right[parent] = child
        else:
            left[parent] = child
    res = 0
    preorder(N)
    print('#{} {}'.format(tc, res))