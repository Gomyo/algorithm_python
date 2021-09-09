data = list(map(int, '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))
H = 4
tree = [-1]*(pow(2, H+1))
tree[1] = 1
for i in range(0, len(data), 2):
    parent = data[i]
    child = data[i+1]

    p_idx = tree.index(parent)
    if tree[p_idx*2] == -1: #왼쪽 자식이 없음
        tree[p_idx*2] = child
    else:
        tree[p_idx*2+1] = child
# print(tree)

def pre_order(v):
    if v > pow(2, H+1)-1 or tree[v] == -1:
        return
    print(tree[v], end=' ')
    pre_order(v*2)
    pre_order(v*2+1)

pre_order(1)