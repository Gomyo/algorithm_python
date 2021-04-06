class Tree:
    def __init__(self, N):
        self.tree=[0] * (N+1)
        self.N = N
        self.cnt = 1
        self.insert(1)

    def insert(self, num):
        if num <= N:
            self.insert(num * 2)
            self.tree[num] = self.cnt
            self.cnt += 1
            self.insert(num * 2 + 1)

    def print_result(self):
        return '{} {}'.format(self.tree[1], self.tree[N//2])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = Tree(N)
    print('#{} {}'.format(tc, tree.print_result()))