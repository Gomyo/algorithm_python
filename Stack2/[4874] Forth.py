T = int(input())

for tc in range(1, T+1):
    data = list(map(str, input().split()))
    stack = []
    for i in data:
        if i in ['+', '*', '/', '-']:
            if len(stack) <= 1:
                print('#{} error'.format(tc))
                break
            if i == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif i == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a // b)
            else:
                stack.append(int(stack.pop()) * int(stack.pop()))
        elif i == '.':
            # 스택에 숫자가 여러 개 남아 있을 경우를 생각하지 못했다.
            # 1 1 + 2 . <- 이와 같은 input이 있다면?
            if len(stack) >= 2:
                print('#{} error'.format(tc))
            else:
                print('#{} {}'.format(tc, stack[-1]))
            break
        else:
            stack.append(i)
