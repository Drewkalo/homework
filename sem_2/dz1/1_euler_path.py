def is_eulerian(G):
    cnt_vert = 0
    start_path = None 
    for node in G:
        if len(G[node]) % 2 != 0:
            cnt_vert += 1
            if start_path is None:
                start_path = node
#в таком случае неважно, какая вершина
    if cnt_vert == 0:
        if G:
            start_path = G[0]
        return (True, start_path)
    elif cnt_vert == 2:
        return (True, start_path)
    else:
        return (False, None)


def dfs(G, visited, start, path):
    visited.append(start)
    while G[start]:
        neighbor = G[start].pop()
        try:
            G[neighbor].remove(start)
        except ValueError:
            pass
        dfs(G, visited, neighbor, path)


graph1 = {'A': ['B', 'C', 'D'],'B': ['A', 'C'],'C': ['A', 'B', 'D'],'D': ['A', 'C']}

visited = []
path = []

temp = is_eulerian(graph1)
if temp[0]:
    start_node = temp[1]

    dfs(graph1, visited, start_node, path)
    print(visited)
else:
    print("No path")
