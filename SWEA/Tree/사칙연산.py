import sys

sys.stdin = open('사칙연산input.txt', 'r')

def postorder(v):
    global res
    v = int(v)-1
    if len(data[v]) == 4:
        postorder(int(data[v][2]))
        postorder(int(data[v][3]))
        res.append(data[v][1])
    elif len(data[v]) == 3:
        postorder(int(data[v][2]))
        res.append(data[v][1])
    else:
        res.append(data[v][1])

def post_cal(ex):
    stack = []
    for i in ex:
        if i in ['+', '-', '/', '*']:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            else:
                stack.append(a/b)
        else:
            stack.append(float(i))
    return stack

for tc in range(1, 11):
    N = int(input())
    data = [list(input().split()) for x in range(N)]
    res = []
    postorder('1')
    ans = post_cal(res)[0]
    print('#{} {}'.format(tc, int(ans)))

'''
def operator(num1, num2, oper):
    if oper == '-':
        return num1 - num2
    elif oper == '+':
        return num1 + num2
    elif oper == '*':
        return num1 * num2
    else:
        return num1 / num2


for tc in range(1, 11):
    N = int(input())
    depth = len(bin(N)) - 2
    tree = [0] * (1 << depth)
    command = {}
    for _ in range(N):
        x = list(input().split())
        if len(x) == 4:
            command[x[0]] = x[1:]
        else:
            tree[int(x[0])] = int(x[1])
    for node in sorted(command.keys(), key=lambda x: int(x), reverse=True):
        child1, child2 = tree[int(command[node][1])], tree[int(command[node][2])]
        tree[int(node)] = operator(child1, child2, command[node][0])

    print('#{} {}'.format(tc, int(tree[1])))
'''