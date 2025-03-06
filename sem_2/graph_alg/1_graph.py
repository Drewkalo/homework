#Считывание графа

#считываем число вершин N и число ребер M
N,M = map(int,input().split())
#print(N,M)

#создаём заготовку под граф
graph = {i:set() for i in range(N)}

#считываем M рёбер
for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2) #для направленного графа
    graph[v2].add(v1) #для ненаправлненного графа