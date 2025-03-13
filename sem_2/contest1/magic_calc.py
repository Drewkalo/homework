class Node:
    def __init__(self, val = None, step = None):
        self.val = (val, step)
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val, step):
        node = Node(val, step)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.right = node
            self.tail = node

    def remove(self):
        
        if not self.head:
            print('Empty')
            return None

        res = self.head.val
        self.head = self.head.right
        return res

def sum_symb(val):
    res = 0
    while val > 0:
        res += val % 10
        val //= 10
    return res

n, m = map(int, input().split())

deque = Deque()
deque.add(n, 0)
visited = set()
visited.add(n)

while deque:
    current, step = deque.remove()
    if current == m:
        print(step)
        break

    next = current - 2
    if next <= 9999 and next >= 1 and next not in visited:
        visited.add(next)
        deque.add(next, step+1)
    
    next = current * 3
    if next <= 9999 and next >= 1 and next not in visited:
        visited.add(next)
        deque.add(next, step+1)

    next = current + sum_symb(current)
    if next <= 9999 and next >= 1 and next not in visited:
        visited.add(next)
        deque.add(next, step+1)

