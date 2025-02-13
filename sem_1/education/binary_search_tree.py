class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    #инициализация корня
    def __init__(self):
        self.root = None

    #вставка элемента
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    #поиск элемента в дереве
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    #удаление элемента
    def delete(self, key):
      self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            #нод с одним ребенком или без них
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #нод с двумя детьми
            node.key = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.key)
        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key



    # Метод для обхода дерева (например, инфиксный обход) - для проверки
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

bst = BinarySearchTree()
bst.insert(7)
bst.insert(6)
bst.insert(5)
bst.insert(7)
bst.insert(10)
bst.insert(11)
bst.insert(8)

print(bst.search(6)) #Найдем узел
print(bst.inorder_traversal()) # инфиксный(центрированный) обход (упорядоченный вывод)
bst.delete(8)
print(bst.inorder_traversal()) # инфиксный обход после удаления