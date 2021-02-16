T = int(input())

for tc in range(1, T+1):
    stack = []
    data = input()
    res = 1

    for i in data:
        if i == '(':
            stack.append(1)
        elif i == '{':
            stack.append(2)
        # Runtime Error maybe occurred because of pop?
        # 스택이 비어있는지 먼저 체크하고 -1에 접근해야 함.
        # index Error가 뜨니까!!
        elif i == ')':
            if stack[-1] == 1:
                stack.pop()
            else:
                res = 0
        elif i == '}':
            if stack[-1] == 2:
                stack.pop()
            else:
                res = 0
    if stack:
        res = 0

    print(f'#{tc} {res}')