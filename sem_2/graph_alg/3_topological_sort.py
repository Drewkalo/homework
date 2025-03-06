#Топологическая сортировка

visited = set()
res = []

#это слово в слово dfs, но когда мы доходим до листа, то записываем его в res
def topological(G,visited,start,res):
    visited.add(start)
    for i in G[start]:
        if i not in visited:
            topological(G,visited,i,res)
    res.append(start)

G = {'A':{'D','E'},'B':{'D'},'C':{'E','H'},'D':{'F','G'},'E':{'G'},'F':set(),'G':set(),'H':set()}

#повторяем topological для каждой вершины, если она не была посещена, чтобы точно пройти все вершинки.
for i in G:
    if i not in visited:
        topological(G,visited,i,res)
print(res[::-1])