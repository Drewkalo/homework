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
            left_height = self.node.left.height()
            right_height = self.node.right.height()
        else:
            left_height=0
            right_height=0
        return left_height - right_height
    def height(self):
        if not self.node:
            return 0
        return self.node.height
    def fix_height(self):
        self.node.height = 1 + max(self.node.left.height(),self.node.right.height())
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
            else:
                self.node.right.insert(val)
        self.fix_height()
        self.rebalance()
    def small_left_rotate(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
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
res.insert(1)
res.insert(105)
res.insert(37)
res.insert(89)
res.insert(33)
res.insert(11)
res.insert(69)
res.insert(22)
res.insert(57)
print(*res.vivod())
print(*res.vivod_invert())




        

