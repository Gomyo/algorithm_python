# 입력 받은 중위 표기식에서 토큰을 읽는다.
# 토큰이 피연산자이면 토큰을 출력한다.
# 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 push
# 그렇지 않다면 top의 연산자의 우선순위가 토큰의 우선순위보다 낮을 때까지 스택에서 pop한 후 토큰의 연산자를 push
# 만약 top에 연산자가 없으면 push
# 토큰이 오른쪽 괄호이면 스택 top에 왼쪽 괄호가 올 때까지 pop을 수행하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
# 중위 표기식에 더 읽을 것이 없다면 중지
# 스택에 남아 있는 연산자를 모두 pop하여 출력
# (6 + 5 * (2 – 8) / 2)
# (6+5*(2-8)/2)
# 6 5 2 8  - * 2 / +

in_come_pri = {  "(": 3 ,"*": 2 , "/": 2 , "+": 1 , "-": 1 }
in_stack_pri = { "*": 2 , "/": 2 , "+": 1 , "-": 1, "(": 0 }

ex_str = input()

def post_expression(ex_str):
    stack = []
    # 문자열에서 토큰 하나씩 읽어오기
    for i in range(len(ex_str)):
        token = ex_str[i]
        if token in ['(', '*', '/', '+', '-']:
            # token이 stack의 top보다 우선순위가 높으면 push
            # 낮으면 token보다 낮은애가 top에 있을때까지 pop하고 push
            if not stack or in_come_pri[token] > in_stack_pri[stack[-1]]:
                stack.append(token)
            else:
                # 토큰 우선순위가 낮음
                # 나보다 낮은애가 top에 있을때까지
                while stack and in_come_pri[token] <= in_stack_pri[stack[-1]]:
                    print(stack.pop(), end=" ")
                stack.append(token)
        elif token == ')':
            # stack의 top이 여는 괄호일 때까지
            while stack[-1] != '(':
                print(stack.pop(), end=" ")
        else: # 피연산자
            print(token, end=" ")
post_expression(ex_str)