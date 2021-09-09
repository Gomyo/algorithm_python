T = int(input())

for tc in range(1, T+1):
    stick = input()
    stack = 0
    res = 0
    stick = stick.replace('()', '*')

    for i in stick:
        if i == '(':
            stack += 1
        elif i == ')':
            stack -= 1
            res += 1 # 닫는 괄호일 경우, 쇠막대기의 끄트머리를 더해주어야 한다.
        elif i == '*':
            res += stack

    print(f'#{tc} {res}')
'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''



