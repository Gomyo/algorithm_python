import sys

sys.stdin = open('중위순회input.txt', 'r')
T = 10

def inorder(v):
    global res
    v = int(v)
    if len(data[v]) == 2:
        res += data[v][1]
        return

    if len(data[v]) == 4:
        inorder(data[v][2])
        res += data[v][1]
        inorder(data[v][3])

    elif len(data[v]) == 3:
        inorder(data[v][2])
        res += data[v][1]


for tc in range(1, T+1):
    N = int(input())
    datas = [list(input().split()) for x in range(N)]
    data = [0] * (N+1)
    for i in range(1, N+1):
        data[i] = datas[i-1]
    res = ''
    inorder(1)
    print('#{} {}'.format(tc, res))
