#DSU - система непересекающхся множеств, используется в алгоритмах: Краскала и ?Борувка?
#Кратко: в каждом множестве есть представитель
#Также определены операции: поиска(выводит представителя множества, в котором находится наш элемент)
#Объединения множеств

class DSU:

    def __init__(self, G):
        self.parent = {i:i for i in G}

    def find(self, v):
        return self.parent[v]
    
    def union(self, v1, v2):
        u1 = self.find(v1)
        u2 = self.find(v2)
        if u1 == u2:
            return
        else:
            for i in self.parent:
                if self.parent[i] == u1:
                    self.parent[i] = u2
