def ft_prior(c):
    if c == '*':
        return 2
    elif c == '+':
        return 1
    else:
        return 0
T = 10

for tc in range(1, T+1):
    n = int(input())
    cal = input()
    res = []
    stack = []

    # Stacking
    for c in cal:
        if ft_prior(c) == 2 or ft_prior(c) == 1: # mul or add
            if not stack or ft_prior(c) < ft_prior(c):
                stack.append(c)
            else:
                while stack and ft_prior(c) <= ft_prior(stack[-1]):
                    res.append(stack.pop())
                stack.append(c)
        else:
            res.append(c) # digit

    # for c in stack: # 여기서 에러남. 스택을 완전하게 비우지 않았음.
    for i in range(len(stack)):
        res.append(stack.pop())

    for i in range(len(res)):
        if ft_prior(res[i]) == 2: # mul
            stack.append(stack.pop() * stack.pop())
        elif ft_prior(res[i]) == 1: # add
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(res[i]))

    print('#{} {}'.format(tc, stack[0]))

# # 다른사람
# T = 10
#
# for tc in range(1, T + 1):
#     N = int(input())
#     stack = []
#     pri = {'*': 2, '+': 1}
#
#     str1 = input()
#     new = []
#
#     for i in range(N):
#         token = str1[i]
#         if token == '*' or token == '+':
#             if not stack or pri[stack[-1]] < pri[token]:
#                 stack.append(token)
#             else:
#                 while stack and pri[token] <= pri[stack[-1]]:
#                     new += [stack.pop()]
#                 stack.append(token)
#         else:
#             new += [token]
#     else:
#         c = len(stack)
#         for j in range(c):
#             new += [stack.pop()]
#
#     for i in range(len(new)):
#         if new[i] == '*':
#             stack.append(int(stack.pop()) * int(stack.pop()))
#         elif new[i] == '+':
#             stack.append(int(stack.pop()) + int(stack.pop()))
#         else:
#             stack.append(new[i])
#     print('#{} {}'.format(tc, stack[-1]))