class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node

    def remove(self):
        if not self.head:
            return None
        res = self.head.val
        self.head = self.head.right
        return res
    
def bfs(graph, s, t, parent):
    visited = set()
    queue = Deque()
    queue.add(s)
    visited.add(s)
    parent.clear()
    parent[s] = -1
    while queue.head:
        node = queue.remove()
        for neighbor in graph[node]:
            if neighbor not in visited and graph[node][neighbor] > 0:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.add(neighbor)
                if neighbor == t:
                    return True
    return False

def edmonds_karp(graph, s, t):
    parent = {}
    max_flow = 0
    while bfs(graph, s, t, parent):
        path_flow = float('inf')
        current = t
        while current != s:
            u = parent[current]
            path_flow = min(path_flow, graph[u][current])
            current = u

        current = t
        while current != s:
            u = parent[current]
            graph[u][current] -= path_flow
            graph[current][u] += path_flow
            current = u
        max_flow += path_flow
    return max_flow

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    graph = {i:{} for i in range(n)}
    for i in range(n):
        temp = input()
        for j in range(n):
            if i != j:
                graph[i][j] = int(temp[j])

    min_cut = float('inf')
    for s in range(n):
        for t in range(s + 1, n):
            current_graph = {verticle: {neighbor: dist for neighbor, dist in dct.items()} for verticle, dct in graph.items()}
            flow = edmonds_karp(current_graph, s, t)
            if flow < min_cut:
                min_cut = flow
    res.append(min_cut)

print(*res, sep="\n")