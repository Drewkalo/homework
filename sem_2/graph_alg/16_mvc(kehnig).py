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



def dfs(G,visited,start,color = 1):
    visited[start] = color
    for i in G[start]:
        if i not in visited:
            dfs(G,visited,i,color*-1)


def kuhn_dfs(G,visited,matching,start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if not matching[i] or kuhn_dfs(G,visited,matching,matching[i]):
            matching[i] = start
            matching[start] = i
            return True            
    return False

def Kuhn(G,half):
    matching = {i:None for i in G}
    for i in half:
        visited = set()
        if not matching[i]:
            kuhn_dfs(G,visited,matching,i)
    return matching

def MVC(G):
    visited = {}
    for i in G:
        if i not in visited:
            dfs(G,visited,i)
    L,R = set(),set()
    for i in visited:
        if visited[i] == 1:
            L.add(i)
        else:
            R.add(i)
    if len(L) > len(R):
        L,R = R,L

    matchings = Kuhn(G,L)

    LR = {i:set() for i in G}

    for v1 in L:
        for v2 in G[v1]:
            if matchings[v1] == v2:
                LR[v2] = {v1}
            else:
                if v2 in LR:
                    LR[v1].add(v2)
                else:
                    LR[v1] = {v2}
    visited = {}
    for v in L:
        if matchings[v] is None:
            dfs(LR,visited,v)
    
    mvc = []

    for v in L:
        if v not in visited:
            mvc.append(v)
    
    for v in R:
        if v in visited:
            mvc.append(v)
    return mvc


print(MVC(G))
