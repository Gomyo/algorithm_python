# top 변수를 이용한 stack 구현하기
# 임의로 저장가능한 크기를 지정해두고 구현할거임
class Stack:
    # 기능 : push, pop
    # 데이터 : 실제값이 저장되는 리스트
    #     가장 마지막에 들어온 데이터의 위치 : top 변수
    def __init__(self):
        self.s = [0] * 100  # 데이터 저장 리스트
        self.top = -1  # 가장 나중에 들어온 데이터의 위치를 저장할 변수

    # 데이터를 현재의 마지막 요소 뒤에 넣어주기
    def push(self, val):
        # 데이터를 받아오면,
        # top을 1 증가 시키고
        self.top += 1
        # 해당 위치에 데이터 넣기
        self.s[self.top] = val

    # 마지막 요소를 반환하고 지움
    def pop(self):
        # stack안에 요소가 있을 때 반환
        # 없으면, 데이터가 없음이라는 데이터를 반환
        result = None
        # if 데이터가 있으면, 마지막 데이터를 반환
        if self.top > -1:
            result = self.s[self.top]
            self.top -= 1
        return result


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())


#########################################
# 여러분들이 작성할 조건
# 데이터 추가(push)시 list의 append() 함수 활용
# 데이터 삭제(pop) pop() 함수 사용 X
#    (마지막 요소를 어떻게 지우지???)

class Stack2:
    def __init__(self):
        self.top = -1
        self.s = list()

    def push(self, value):
        self.s.append(value)
        self.top += 1

    def pop(self):
        result = None
        if self.top > -1:
            result = self.s[self.top]
            self.s = self.s[:self.top]
            self.top -= 1
        return result

my_stack = Stack2()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())