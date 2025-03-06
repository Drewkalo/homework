#Алгоритм аналогичен dfs, но на шагах мы красим вершинки в 2 цвета(1, -1),
#также проверяем, что цвет вершинки не совпадает с цветом соседей. Если совпал, то не двудольный
visited = []

G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}

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
        
