class Node:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.node = None

    def balance(self):
        if self.node:
            left_height = self.node.left.height() if self.node.left else 0
            right_height = self.node.right.height() if self.node.right else 0
            return left_height - right_height
        else:
            return 0

    def height(self):
        if not self.node:
            return 0
        return self.node.height

    def fix_height(self):
        if self.node:
            self.node.height = 1 + max(self.node.left.height(), self.node.right.height())

    def rebalance(self):
        pass 

    def insert(self, val):
        if self.node is None:
            self.node = Node(val)
            self.node.left = AVL()
            self.node.right = AVL()
        else:
            if val < self.node.value:
                self.node.left.insert(val)
            elif val > self.node.value:
                self.node.right.insert(val)
        self.fix_height()
        return self.rebalance()
    
    def _leaves(self, node, leaves):
        if node:
            self._leaves(node.left.node, leaves)
            if not node.left.node and not node.right.node:
                leaves.append(node.value)
            self._leaves(node.right.node, leaves)

    def leaves(self):
        leaves = []
        self._leaves(self.node, leaves)
        return leaves

    def vivod(self):
        res = []
        self._vivod(self.node, res)
        return res

    def _vivod(self, node, res):
        if node:
            self._vivod(node.left.node, res)
            res.append(node.value)
            self._vivod(node.right.node, res)

    def vivod_invert(self):
        res = []
        self._vivod_invert(self.node, res)
        return res

    def _vivod_invert(self, node, res):
        if node:
            self._vivod_invert(node.right.node, res)
            res.append(node.value)
            self._vivod_invert(node.left.node, res)

res = AVL()
n = int(input())
for i in [int(c) for c in input().split()]:
    res.insert(i)
print(*res.leaves())




        

