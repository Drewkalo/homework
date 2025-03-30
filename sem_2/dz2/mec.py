M = int(input())

G = {}

for i in range(M):
    v1,v2 = input().split()
    if v1 in G:
        G[v1].add(v2)
    else:
        G[v1] = {v2}
    if v2 in G:
        G[v2].add(v1)
    else:
        G[v2] = {v1}


def dfs(G,visited,matching,start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if  not matching[i] or dfs(G,visited,matching,matching[i]):
            matching[i] = start
            matching[start] = i
            return True            
    return False

def Kuhn(G):
    matching = {i:None for i in G}
    for i in G:
        visited = set()
        if not matching[i]:
            dfs(G,visited,matching,i)
    return matching

matching = Kuhn(G)

# создаём множество для реберного покрытия, в него будут входить паросочетание + ребра для непокрытых вершин
mec_edges = set()

# вершины в покрытии
match_verts = [i for i in matching if matching[i] is not None]
set_match = set(match_verts)

# множество всех вершин
all_verts = [i for i in G]
set_all_verts = set(G.keys())


# добавляем в покрытие ребра из паросочетание, причем игнорируем дублирующие ребра
for node in G:
    par = matching.get(node)
    if par is not None:
        mec_edges.add(tuple(sorted([node, par])))

# для каждой непокрытой вершины мы добавляем 1 ребро, инцидентное ей, и сразу же переходим к след. непокрытой вершине
unmatch_verts = set_all_verts - set_match

for vert in unmatch_verts:
    for neighbor in G[vert]:
        if matching.get(neighbor) is None:
            mec_edges.add(tuple(sorted([node, neighbor])))
            break


print(mec_edges)