class MyQueue:
    def __init__(self):
        #front : 현재 큐에 들어있는 요소 중 가장 앞요소
        #rear : 현재 큐에 들어있는 요소 중 가장 마지막 요소
        self.front = -1
        self.rear = -1
        #최대저장길이는 10으로 선언
        self.q = [None] * 10

    #enQueue(val) : Queue에 요소를 넣는 기능
        #Queue에 들어있는 마지막요소(rear)의 뒤에 새로운 요소를 넣음
    def enQueue(self,val):
        # 큐가 가득 찼으면 데이터를 넣지 않는다.
        if not self.isFull():
            self.rear += 1
            self.q[self.rear] = val

    #deQueue() : Queue의 front를 반환하고 삭제하는 기능
    def deQueue(self):
        # 비어있지 않으면 front를 1 증가 시키고 그 위치의 값을 반환
        if not self.isEmpty():
            self.front += 1
            # self.q.pop(self.front)
            return self.q[self.front]

    #isEmpty() : Queue가 비어있는지 확인하는 기능
        #Queue가 비어있으면 True, 아니면 False 를 반환
    def isEmpty(self):
        return self.front == self.rear

    #isFull() : Queue가 가득찼는지 확인하는 기능
        #가득차 있으면 True, 아니면 False를 반환
    def isFull(self):
        # 마지막 칸에 데이터가 들어가 있으면 True
        return self.rear == len(self.q) - 1

    #Qpeek() : Queue의 front를 반환
    # front가 가리키는 그 다음 칸.
    def Qpeek(self):
        if self.isEmpty():
            return None
        return self.q[self.front + 1]
myQ = MyQueue()
myQ.enQueue(1)
myQ.enQueue(2)
myQ.enQueue(3)
print(myQ.deQueue())
print(myQ.deQueue())
print(myQ.deQueue())