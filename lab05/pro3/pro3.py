class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.value:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)
        else:
            return

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None  # 못 찾음
        if key == node.value:
            return node  # 찾은 노드 반환
        elif key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            # 자식이 없는 경우
            if node.left is None and node.right is None:
                return None

            # 자식이 하나인 경우
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 자식이 두 개인 경우 → 오른쪽 서브트리에서 최소값 찾기
            min_node = self._min_value_node(node.right)
            node.value = min_node.value
            node.right = self._delete(node.right, min_node.value)

        return node

    # 오른쪽 서브트리에서 최소값 찾는 함수
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 중위 순회를 이용한 나무 탐색
    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, values):
        if node:
            self._inorder(node.left, values)
            values.append(node.value)
            self._inorder(node.right, values)
        return values


def main():
    # 아래는 예시 코드 입니다.
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("이진 탐색 트리의 중위 순회 결과:", bst.inorder())

    print("값 40을 탐색:", "발견" if bst.search(40) else "발견되지 않음")
    print("값 25를 탐색:", "발견" if bst.search(25) else "발견되지 않음")

    bst.delete(20)
    print("값 20을 삭제한 후 중위 순회 결과:", bst.inorder())

    bst.delete(30)
    print("값 30을 삭제한 후 중위 순회 결과:", bst.inorder())

    bst.delete(50)
    print("값 50을 삭제한 후 중위 순회 결과:", bst.inorder())


if __name__ == "__main__":
    main()
