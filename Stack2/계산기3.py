in_come_pri =   { "(": 3 , "*": 2 , "+": 1 }
in_stack_pri =  { "*": 2 , "+": 1 , "(": 0 }

T = 10

for tc in range(1, T+1):
    n = int(input())
    ex_str = input()
    res = []
    stack = []

    for i in range(n):
        token = ex_str[i]
        if token in ['(', '*', '+']:
            if not stack or in_come_pri[token] > in_stack_pri[stack[-1]]:
                stack.append(token)
            else:
                while stack and in_come_pri[token] <= in_stack_pri[stack[-1]]:
                    res.append(stack.pop())
                stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            stack.pop() # (를 빼줘야 한다.
        else:
            res.append(token)

    for i in range(len(stack)):
        res.append(stack.pop())

    for i in range(len(res)):
        if res[i] == '*': # mul
            stack.append(stack.pop() * stack.pop())
        elif res[i] == '+': # add
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(res[i]))

    print('#{} {}'.format(tc, stack[0]))

'''
1
3+(4+5)*6+7
'''