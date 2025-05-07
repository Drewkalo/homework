alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Deque_Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,val):
        node = Deque_Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node
    def remove(self):
        if not self.head:
            print('Empty')
            return None
        res = self.head.val
        self.head = self.head.right
        return res

class Node:
    def __init__(self):
        self.children = {}
        self.to = {}
        self.sufflink = None
        self.compressed_sufflink = None
        self.output = None

class Aho_corasick:
    def __init__(self):
        self.root = Node()
    def add(self,s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                new_v = Node()
                v.children[c] = new_v
                v = new_v
        v.output = s
    
    def build(self):
        queue = Deque()
        self.root.sufflink = self.root
        self.root.compressed_sufflink = self.root
        for char in alphabet:
            if char in self.root.children:
                 self.root.to[char] = self.root.children[char]
            else:
                self.root.to[char] = self.root
        for i in self.root.children:
            cur = self.root.children[i]
            cur.sufflink = self.root
            cur.compressed_sufflink = self.root
            queue.add(cur)
        while queue.head:
            current = queue.remove()
            for char in alphabet:
                if char in current.children:
                    current.to[char] = current.children[char]
                else:
                    current.to[char] = current.sufflink.to[char]
            for i in current.children:
                current_child = current.children[i]
                current_child.sufflink = current.sufflink.to[i]
                queue.add(current_child)
                if current_child.sufflink.output:
                    current_child.compressed_sufflink = current_child.sufflink
                else:
                    current_child.compressed_sufflink = current_child.sufflink.compressed_sufflink
    def find(self,text,words):
        for word in words:
            self.add(word)
        self.build()

        cur_node = self.root
        result = {}

        for i, char in enumerate(text):
            cur_node = cur_node.to[char]
            temp = cur_node
            while temp != self.root:
                if temp.output:
                    if temp.output in result:
                        result[temp.output].add(i)
                    else:
                        result[temp.output] = {i}
                temp = temp.compressed_sufflink
        return result
    
    def find_min(self,L,words):
        for word in words:
            self.add(word)
        self.build()
        def dfs(start,word,L):
            if len(word) == L:
                return word
            for i in alphabet:
                if not start.to[i].output and not start.to[i].compressed_sufflink.output:
                    if dfs(start.to[i],word+i,L):
                        return dfs(start.to[i],word+i,L)
            return False
        return dfs(self.root,'',L)

    def find_mask(self,mask,text):
        res = []
        number = 0
        words = set()
        positions = {}
        cur = ''
        for i in range(len(mask)):
            if mask[i] != '?':
                cur += mask[i]
            else:
                if cur:
                    words.add(cur)
                    number += 1
                    if cur in positions:
                        positions[cur].add(i-1)
                    else:
                        positions[cur] = {i-1}
                    cur = ''
        if cur:
            words.add(cur)
            number += 1
            if cur in positions:
                positions[cur].add(i)
            else:
                positions[cur] = {i}

        c = [0]*len(text)

        for word in words:
            self.add(word)
        self.build()
        cur_node = self.root
        for i, char in enumerate(text):
            cur_node = cur_node.to[char]
            temp = cur_node
            while temp != self.root:
                if temp.output:
                    for j in positions[temp.output]:
                        if i - j >= 0:
                            c[i-j] += 1
                temp = temp.compressed_sufflink

        for i in range(len(c)):
            if c[i] == number:
                res.append(i)
        return res






