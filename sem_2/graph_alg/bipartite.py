visited = []

G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}

#G = {0:{1,2},1:{0,3},2:{0,3},3:{1,2}}

colors = [None] * len(G)

is_bipatite = True

def dfs(G,visited,start,color = 1):
    visited.append(start)
    colors[start] = color
    for i in G[start]:
        if i in visited:
            if colors[i] == colors[start]:
                return False
        if i not in visited:
            return dfs(G,visited,i,color*-1)
    return True

print(dfs(G,visited,0))
        
