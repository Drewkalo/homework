class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if not self.head:
            print('Empty')
            return
        else:
            result = self.head.val
            self.head = self.head.next
            return result



N,M = map(int,input().split())

graph = {i:set() for i in range(N)}

reversed_graph = {i:set() for i in range(N)}

for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)
    reversed_graph[v2].add(v1)

visited = []

stack = Stack()

def dfs(G,visited,start, stack = None, list = None):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            dfs(G,visited,i,stack,list)
    if stack:
        stack.push(start)
    if list is not None:
        list.append(start)

        
for i in graph:
    if i not in visited:
        dfs(graph,visited,i, stack = stack)


visited = []

result = []

while stack.head:
    current = stack.pop()
    if current not in visited:
        list = []
        dfs(reversed_graph, visited, current, list = list)
        result.append(list)

print(result)