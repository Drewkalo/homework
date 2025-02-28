#Реализация очереди через список

#вспомогательный класс для хранения данных: значение, ссылку на правого и левого соседа
class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

#создаём очередь, у которой есть голова и хвост. Добавляем в хвост, достаём из головы (FIFO)
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,val):
        node = Node(val)
        #если очередь пуста
        if not self.head:
            self.head = node
            self.tail = node
        #иначе добавляем значение справа старого хвоста, а после переставляем хвост на наше новое значение
        else:
            self.tail.right = node
            self.tail = node

    def remove(self):
        #если нет головы, то нечего и доставать
        if not self.head:
            print('Empty')
            return None
        #иначе записываем значение в res, а после переставляем голову на соседа справа
        res = self.head.val
        self.head = self.head.right
        return res
    
G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}

queue = Deque()
visited = []

#Реализация bfs
#стартуем с вершинки, закидываем её в очередь и добавляем в visited
#пока очередь не пуста, достаем вершинку из очереди(головы), смотрим её соседей, если они не в visited, то добавляем их в очередь и visited, 
def bfs(G,queue,start,visited):
    queue.add(start)
    visited.append(start)
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if i not in visited:
                queue.add(i)
                visited.append(i)
    
bfs(G,queue,3,visited)
print(visited)

#Кратчайший путь при помощи bfs

queue = Deque()
dist = [None]*len(G)

def bfs_way(G,queue,start,dist):
    queue.add(start)
    dist[start] = 0
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if not dist[i]:
                queue.add(i)
                dist[i] = dist[current] + 1
    
bfs_way(G,queue,3,dist)
print(dist)