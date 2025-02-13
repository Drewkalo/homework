class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node  = Node(val)
        if not self.head:
            self.heaf = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node

    def remove(self):
        if not self.head:
            print("ПУсто")
            return None
        res = self.head.val
        self.head = self.head.right
        if self.head:
            self.head.ledt = None
            return res
        
G = {"A":{"D", "E"},"D":{"F", "G"}, "F":{}, "G":{}, "B":{"D"}, "E":{}, "C":{"E", "H"}, "H":{}}
queue = Deque()
start = 0
end = 6
dist = [None] * len(G)
parents  = [None] * len(G)
dist[start] = 0

def bfs(G, queue, start, dist, parents):
    queue.add(start)
    dist[start] = 0
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not dist[i]:
                dist[i] = dist[current] + 1
                parents[i] = current
                queue.add(i)

G = {"A":{"D", "E"},"D":{"F", "G"}, "F":{}, "G":{}, "B":{"D"}, "E":{}, "C":{"E", "H"}, "H":{}}

print(parents)