class Node:
    def __init__(self, val = None):
        self.val = val
        self.right = None
        self.left = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, val):
        node = Node(val)
        if  not self.head:
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
        if self.head is None:  # Если очередь стала пустой
            self.tail = None
        return res

G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}
queue = Deque()
dist = [-2 for i in range(len(G))] # -1 означает, что вершина не посещена
visited = [False for i in range(len(G))]


def bfs_way(G, queue, start, dist, visited): #Убрали visited, тк используем dist
    queue.add(start)
    dist[start] = 0
    visited[start] = True
    while queue.head:
        current = queue.remove()
        for neighbor in G[current]:
            if not visited[neighbor]:
                queue.add(neighbor)
                dist[neighbor] = dist[current] + 1
                visited[neighbor] = True


bfs_way(G, queue, 3, dist, visited)
print(dist)
