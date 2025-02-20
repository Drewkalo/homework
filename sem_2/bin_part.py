''' ЖПТ вариант
def is_bipartite(G):
    visited = {}
    
    def dfs(node, color):
        visited[node] = color
        for neighbor in G[node]:
            if neighbor not in visited:
                if not dfs(neighbor, 1 - color):
                    return False
            elif visited[neighbor] == color:
                return False
        return True

    for node in G:
        if node not in visited:
            if not dfs(node, 0):
                return False
    return True
G = {0: {1}, 1: {0, 3}, 3: {1, 4}, 4: {3, 5}, 5: {4, 6}, 6: {5}}
#G = {0: {1, 2}, 1: {0, 2, 3}, 2: {0, 1, 4, 5}, 3: {1, 4}, 4: {2, 3, 5}, 5: {2, 4, 6}, 6: {5}}
if is_bipartite(G):
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
'''

#Реализация dfs_bin
G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}
colors = {i:None for i in G}

def dfs_bin(G,colors,start,color):
    colors[start] = color
    for i in G[start]:
        if colors[i]:
            if colors[start] == colors[i]:
                return False
            else:
                return dfs_bin(G,colors,i, color*-1)

dfs_bin(G,colors,3,1)
