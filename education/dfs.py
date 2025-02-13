#Реализация dfs

visited = []

def dfs(G,visited,start):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            dfs(G,visited,i)

G = {0:{1,2},1:{0,2,3},2:{0,1,4,5},3:{1,4},4:{2,3,5},5:{2,4,6},6:{5}}
dfs(G,visited,3)
print(visited)

#Подсчет компонент связности

visited = []

N = 0
for i in G:
    if i not in visited:
        N += 1
        dfs(G,visited,i)
    print(N)
