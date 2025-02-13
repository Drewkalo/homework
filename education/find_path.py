#Поиск кратчайшего пути между вершинами

from collections import deque

G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}

start = 0
end = 6

parents = [None]*len(G)
dist = [None]*len(G)
dist[start] = 0
queue = deque([start])

while queue:
    current = queue.popleft()
    for v in G[current]:
        if not dist[v]:
            dist[v] = dist[current] + 1
            parents[v] = current
            queue.append(v)

path = [end]
parent = parents[end]
while parent:
    path.append(parent)
    parent = parents[parent]
path.append(start)
print(path[::-1])

