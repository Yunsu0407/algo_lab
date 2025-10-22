class RedBlackNode:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color  # "red" 또는 "black"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = RedBlackNode(0)
        self.TNULL.color = "black"
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):
        node = RedBlackNode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"  # 새 노드는 항상 빨강으로 삽입됨

        y = None
        x = self.root

        # 이진 탐색 트리 규칙으로 삽입 위치 탐색
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # 루트라면 바로 색을 black으로 바꿔줌
        if node.parent is None:
            node.color = "black"
            return

        # 부모가 루트라면 바로 종료
        if node.parent.parent is None:
            return

        # 삽입 후 균형 유지
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # 삼촌 노드
                if u.color == "red":  # case 1: 삼촌이 red
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # case 2: 삼촌이 black, k가 왼쪽
                        k = k.parent
                        self.right_rotate(k)
                    # case 3: 삼촌이 black, k가 오른쪽
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # 삼촌 노드
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)

            if k == self.root:
                break
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self, node, res):
        if node != self.TNULL:
            self.inorder(node.left, res)
            res.append([node.key, node.color])
            self.inorder(node.right, res)

    def get_inorder(self):
        res = []
        self.inorder(self.root, res)
        return res

    def search_tree(self, key):
        return self.search_tree_helper(self.root, key)

    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)


# 테스트
rbt = RedBlackTree()
values = [55, 40, 65, 60, 75, 57]

for value in values:
    rbt.insert(value)

print("레드-블랙 트리의 중위 순회 결과:", rbt.get_inorder())

search_value = 65
found_node = rbt.search_tree(search_value)
if found_node != rbt.TNULL:
    print(f"값 {search_value}를 찾았습니다.")
else:
    print(f"값 {search_value}를 찾지 못했습니다.")
