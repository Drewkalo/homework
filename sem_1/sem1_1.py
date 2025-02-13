visited = []
result = []

def topol_sort(G, visited, start, result):
    
    visited.append(start)
    for i in G[start]:
        
        if i not in visited:
            topol_sort(G, visited, i, result)
    result.append(start)

G = {"A":{"D", "E"},"D":{"F", "G"}, "F":{}, "G":{}, "B":{"D"}, "E":{}, "C":{"E", "H"}, "H":{}}

for i in G:
    if i not in visited:
        topol_sort(G, visited, i, result)
print(result[::-1])
