t = int(input())
res = []
for i in range(t):
    G = {}
    rows, cols, cuts = map(int, input().split()) 
    numbers = range(0,rows)
    letters = range(rows, rows + cols)
    for i in letters:
        for j in numbers:
            if i in G:
                G[i].add(j)
            else:
                G[i] = {j}
            if j in G:
                G[j].add(i)
            else:
                G[j] = {i}

    temp = [int(i) for i in input().split()]
    broken_cell = [(temp[i], temp[i+1] + rows) for i in range(0, len(temp)-1, 2)]

    for i in range(cuts):
        l = broken_cell[i][0]
        k = broken_cell[i][1]
        G[l].remove(k)
        G[k].remove(l)

    def dfs(G,visited,matching,start):
        if start in visited:
            return False
        visited.add(start)
        for i in G[start]:
            if not matching[i] or dfs(G,visited,matching,matching[i]):
                matching[i] = start
                matching[start] = i
                return True            
        return False

    def broken_chess(G):
        matching = {i:None for i in G}
        lm = 0
        for i in letters:
            visited = set()
            if not matching[i]:
                lm += dfs(G,visited,matching,i)
        res.append(lm)
    broken_chess(G)

print(*res, sep="\n")