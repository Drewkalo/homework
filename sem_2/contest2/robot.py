class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node

    def remove(self):
        if not self.head:
            return None
        res = self.head.val
        self.head = self.head.right
        return res
    
def bfs(i, j, x, y, sheme):
    visited = set()
    visited.add((i, j))
    dist = [[float("inf")] * y for _ in range(x)]
    dist[i][j] = 0
    queue = Deque()
    queue.add((i, j))
    neighbors = [(0, -1), (-1, 0), (0, 1), (1,0)]

    while queue.head:
        u, v = queue.remove()
        for du, dv in neighbors:
            new_u, new_v = u + du, v + dv
            if 0 <= new_u <= x-1 and 0 <= new_v <= y-1:
                if sheme[new_u][new_v] != 'X' and (new_u, new_v) not in visited:
                    dist[new_u][new_v] = dist[u][v] + 1
                    queue.add((new_u, new_v))
                    visited.add((new_u, new_v))
    return dist

def Kuhn(G):
    matching = {i:None for i in G}
    for i in G:
        visited = set()
        if not matching[i]:
            dfs(G,visited,matching,i)
    return matching

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


t = int(input())
res = []
for _ in range(t):
    x,y = map(int, input().split())
    sheme = []
    goals = set()
    robot = []
    for i in range(x):
        temp = input()
        sheme.append(temp)
        for j in range(y):
            if temp[j] == 'T':
                goals.add((i,j))
            if temp[j] == 'R':
                robot.append((i,j))
    #print('goals:', goals)
    #print('robot:', robot)
    if len(robot) > len(goals):
        res.append(-1)
    #print('sheme:',sheme)

    matrix = []
    flag = True
    for (i, j) in robot:
        dist = bfs(i, j, x, y, sheme)
        all_goal_dist = []
        for (x_goal, y_goal) in goals:
            if x_goal < x and y_goal < y:
                d = dist[x_goal][y_goal]
            else:
                d = float('inf')
            all_goal_dist.append(d)
        matrix.append(all_goal_dist)

        if min(all_goal_dist) == float('inf'):
            flag = False
            break

    if flag == False:
        res.append(-1)
        continue
    #print('matrix:',matrix)

    value = -1
    low_time = 0
    high_time = 0
    visited = set()
    for part in matrix:
        curr_max = max([v for v in part if v != float('inf')])
        high_time = max(high_time, curr_max)

    #print(high_time)

    while low_time <= high_time:
        mid_time = (low_time + high_time) // 2

        graph = {}
        for i in range(len(robot)):
            for j in range(len(robot), len(robot) + len(goals)):
                if matrix[i][j - len(robot)] <= mid_time:

                    if i not in graph:
                        graph[str(i)] = set()
                        graph[str(i)].add(str(j))
                    else:
                        graph[str(i)].add(str(j))
                        
                    if j not in graph:
                        graph[str(j)] = set()
                        graph[str(j)].add(str(i))
                    else:
                        graph[str(j)].add(str(i))
      
        
        #print(Kuhn(graph))
        #print(len([i for i in Kuhn(graph).values() if i is not None]))
        if len([i for i in Kuhn(graph).values() if i is not None])//2 == len(robot):
            value = mid_time
            high_time = mid_time - 1
        else:
            low_time = mid_time + 1

    res.append(value)

print(*res, sep='\n')
    