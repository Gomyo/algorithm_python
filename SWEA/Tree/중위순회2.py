import sys

sys.stdin = open('중위순회input.txt', 'r')
T = 10

def inorder(v):
    if v <= max_num and tree[v]:
        # 유효한 노드 번호
        inorder(left[v])
        print(tree[v], end="")
        inorder(right[v])


for tc in range(1, T+1):
    N = int(input())
    # 완전이진트리가 아닐 경우에는
    max_num = pow(2, N)
    tree = [0]*(max_num + 1)
    left = [0]*(max_num + 1)
    right = [0]*(max_num + 1)
    for i in range(1, N+1):
        data = list(input().split())
        number = int(data[0])
        tree[number] = data[1]
        if len(data) >= 3:
            left[number] = int(data[2])
        elif len(data) >= 4:
            right[number] = int(data[3])

    print('#{} '.format(tc), end=" ")
    inorder(1)
