#Реализация очереди через список

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
            print('Empty')
            return None
        res = self.head.val
        self.head = self.head.right
        return res
    
G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}

queue = Deque()
visited = []

#Реализация bfs

def bfs(G,queue,start,visited):
    queue.add(start)
    visited.append(start)
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if i not in visited:
                queue.add(i)
                visited.append(i)
                print(queue.head.val)
    
bfs(G,queue,3,visited)
print(visited)

#Кратчайший путь при помощи bfs

queue = Deque()
dist = [None]*len(G)

def bfs(G,queue,start,dist):
    queue.add(start)
    dist[start] = 0
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not dist[i]:
                queue.add(i)
                dist[i] = dist[current] + 1
                print(queue.head.val)
    
bfs(G,queue,3,dist)
print(dist)