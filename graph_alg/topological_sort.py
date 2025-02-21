#Топологическая сортировка

visited = set()
res = []

def topological(G,visited,start,res):
    visited.add(start)
    for i in G[start]:
        if i not in visited:
            topological(G,visited,i,res)
    res.append(start)

G = {'A':{'D','E'},'B':{'D'},'C':{'E','H'},'D':{'F','G'},'E':{'G'},'F':set(),'G':set(),'H':set()}

for i in G:
    if i not in visited:
        topological(G,visited,i,res)
print(res[::-1])