class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self, data):
        self.heap.append(data)
        self.refactor(len(self.heap)-1) # 인덱스니까

    def refactor(self, idx):
        if idx >= 2:
            if self.heap[idx] < self.heap[idx//2]:
                self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
                self.refactor(idx//2)

    def sum_result(self):
        last_idx = (len(self.heap) - 1)//2
        my_sum = 0
        while last_idx >= 1:
            my_sum += self.heap[last_idx]
            last_idx //= 2
        return my_sum

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = Heap()
    for i in map(int, input().split()):
        heap.insert(i)
    print('#{} {}'.format(tc, heap.sum_result()))