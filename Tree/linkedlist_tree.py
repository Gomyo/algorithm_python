# 노드로 구성된 이진트리
class MyTree:
    def __init__(self):
        # 트리니까... 루트가 항상 있어야 함
        self.root = None
    # 데이터 추가
    def insert(self, parent, child):
        # is 자체가 None 비교하기 위해 나온 연산자라서
        if self.root == None:
            self.root = Node(parent)
            self.root.left = Node(child)
        else:
            # parent의 노드를 찾아서 왼쪽이나 오른쪽에 child 추가
            # parent 노드를 찾기 위해서 검색하는 연산 등이 필요
            p_node = self.find_node(parent)
            if p_node.left is None:
                p_node.left = Node(child)
            else:
                p_node.right = Node(child)
        
    def find_node(self, val):
        # val 값을 가지는 노드를 반환하는 함수
        pass

class Node:
    # 값, 왼쪽자식, 오른쪽자식
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

my_tree = MyTree()
my_tree.insert(1,2)