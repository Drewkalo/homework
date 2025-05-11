class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = -1
        self.end = -1

class SuffixTree:
    def __init__(self, s):
        self.root = SuffixTreeNode()
        self.string = s + "$"
        self.build_tree()

    def build_tree(self):
        n = len(self.string)
        for i in range(n):
            self._add_suffix(i, n)

    def _add_suffix(self, suffix_start, n):
        node = self.root
        i = suffix_start
        while i < n:
            current_char = self.string[i]
            if current_char not in node.children:
                new_node = SuffixTreeNode()
                new_node.start = i
                new_node.end = n - 1
                node.children[current_char] = new_node
                return
            else:
                child = node.children[current_char]
                edge_start = child.start
                edge_end = child.end
                k = 0
                while (edge_start + k <= edge_end and 
                       i + k < n and 
                       self.string[edge_start + k] == self.string[i + k]):
                    k += 1
                if k == 0:
                    return
                if k > (edge_end - edge_start + 1):
                    node = child
                    i += (edge_end - edge_start + 1)
                    continue
                mid_node = SuffixTreeNode()
                mid_node.start = edge_start
                mid_node.end = edge_start + k - 1
                child.start = edge_start + k
                mid_node.children[self.string[child.start]] = child
                new_leaf = SuffixTreeNode()
                new_leaf.start = i + k
                new_leaf.end = n - 1
                mid_node.children[self.string[i + k]] = new_leaf
                node.children[current_char] = mid_node
                return

    def count_unique(self):
        def dfs(node):
            total = 0
            for child in node.children.values():
                if child.end == len(self.string) - 1:
                    edge_length = child.end - child.start
                else:
                    edge_length = child.end - child.start + 1
                total += edge_length + dfs(child)
            return total
        return dfs(self.root)

s = input()
st = SuffixTree(s)
print(st.count_unique()) 