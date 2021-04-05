class MyBinaryTree:
    # 최대 높이를 받아서 노드의 총 개수 지정
    def __init__(self, H):
        self.tree = [-1]*(pow(2, H+1))

    # Add data
    def insert(self, parent, child):
        # 만약에 tree 안에 parent가 없으면
        # parent는 root, child는 왼쪽자식
        if parent not in self.tree:
            self.tree[1] = parent
            self.tree[2] = child
        else: # 부모가 tree에 있으면
            # child를 tree에 추가해야하는데
            # child의 index를 알아야 함 > 부모의 인덱스를 확인
            p_idx = self.tree.index(parent)
            if self.tree[p_idx*2] == -1:
                self.tree[p_idx*2] = child
            else:
                self.tree[p_idx*2+1] = child
    def print_tree(self):
        print(self.tree)

    # preorder
    # v : 현재노드의 인덱스
    # 전위순회
    def preorder(self, v):
        # 좌 우 서브트리를 순회하기 전에, 현재노드에서 작업을 먼저 수행
        if v > pow(2, H+1)-1 or self.tree[v] == -1:
            return
        print(self.tree[v], end=" ")
        self.preorder(v*2)
        self.preorder(v*2+1)

    # inorder
    def inorder(self, v):
        if v > pow(2, H + 1) - 1 or self.tree[v] == -1:
            return
        self.inorder(v * 2)
        print(self.tree[v], end=" ")
        self.inorder(v * 2 + 1)

    # postorder
    def postorder(self,v ):
        if v > pow(2, H + 1) - 1 or self.tree[v] == -1:
            return
        self.postorder(v * 2)
        self.postorder(v * 2 + 1)
        print(self.tree[v], end=" ")
    pass

data = list(map(int, '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))
H = 4
my_tree = MyBinaryTree(H)
for i in range(0, len(data), 2):
    my_tree.insert(data[i], data[i+1])

# my_tree.print_tree()

my_tree.preorder(1)
print()
my_tree.inorder(1)
print()
my_tree.postorder(1)
print()