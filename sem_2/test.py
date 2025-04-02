def bfs(graph, s, t, parent):
    visited = set()
    queue = [s]
    visited.add(s)
    parent.clear()
    parent[s] = -1
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                if v == t:
                    return True
    return False
