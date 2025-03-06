import math

def can_more_rich(graph):
    def bellman_ford(G, start):
        d = {i: float('inf') for i in G}
        parents = {i: None for i in G}
        #в логарифмическом представлении 1 рубль = 0
        d[start] = 0
        for i in range(len(G) - 1):
            for node1 in G:
                for node2 in G[node1]: 
                    if d[node2] > d[node1] + G[node1][node2]:
                        d[node2] = d[node1] + G[node1][node2]
                        parents[node2] = node1

        #проверка на отрицательные циклы
        for node1 in G:
            for node2  in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    return True

        return False
    
    #в представлении весов-курсов как логарифмов, произведение переходит в сумму, что позволит нам просто суммировать веса
    #юзаем отрицательные логарифмы, потому что беллман-форд ищет МИНИМАЛЬНЫЙ путь, а так мы его "обманем"
    for currency1 in graph:
        for currency2 in graph[currency1]:
            graph[currency1][currency2] = -math.log(graph[currency1][currency2])

    #проверяем наличие отрицательного цикла хотя бы в одной вершине
    for start_currency in graph:
        if bellman_ford(graph, start_currency):
            return True

    return False

M = int(input())
G = {}

for i in range(M):
    v1, v2, w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2: w}

if can_more_rich(G):
    print("Да")
else:
    print("Нет")
