n, m = map(int, input().split())

graph = {i:set() for i in range(1, n+1)}
count_in = {i:0 for i in range(1, n+1)}
count_out = {i:0 for i in range(1, n+1)}

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    count_in[v2] += 1
    count_out[v1] += 1

def cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        
        if node in visited:
            return False
        
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        stack.remove(node)
        return False

    for node in graph:
        if dfs(node) == True:
            return True
    return False

if cycle(graph):
    print(-1)

else:
    if list(count_out.values()).count(0) != 1:
        print("NO")
    else:
        print("YES")