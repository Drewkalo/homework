class Node:
    def __init__(self):
        self.children = {}
        self.output = None
        self.count = 0 

def generate_numbers(n, base):
    result = []
    def backtrack(curr):
        if len(curr) == n:
            result.append(''.join(curr))
            return
        for digit in range(base):
            curr.append(str(digit))
            backtrack(curr)    
            curr.pop()
    backtrack([])
    return result

class Trie:
    def __init__(self):
        self.root = Node()

    def build(self, base, length):
        self.build_recursive(self.root, base, length, 0, [])        # +

    def build_recursive(self, node, base, length, curr_depth, digits): # +
        if curr_depth == length:
            num_str = ''.join(digits)
            node.output = num_str
            return
        for digit in range(base):
            str_digit = str(digit)
            if str_digit not in node.children:
                new_v = Node()
                new_depth = curr_depth + 1
                node.children[str_digit] = new_v
            else:
                new_v = node.children[str_digit]
            self.build_recursive(new_v, base, length, new_depth, digits + [str_digit])

    def find_word(self, word):
        v = self.root
        for letter in word:

            if letter in v.children:
                v = v.children[letter]
            else:
                return False
        if v.output != word:
            return False
        else:
            return True

    def add(self,s):                # +
        v = self.root
        for c in s:
            v.children[c].count += 1
            v = v.children[c]
        v.output = s

    def solve(self, prices, word): # +
        v = self.root
        result = 0
        pos = 0
        for char in word:
            result += prices[pos] * v.children[char].count
            v = v.children[char]
            pos += 1
        return (result, v.output)


inp = [int(i) for i in input().split()]
price = [int(i) for i in input().split()]
fixed_price = [price[i] - price[i-1] for i in range(1, inp[1])]

fixed_price = price[0:1] + fixed_price


tickets = Trie()
tickets.build(inp[2], inp[1])
for _ in range(inp[0]):
    tickets.add(input().strip())
# print(tickets.words)

best = (float('inf'), '')
cont = generate_numbers(inp[1], inp[2])
for num in cont:
    temp1, temp2 = tickets.solve(fixed_price, num)
    if temp1 < best[0]:
        best = (temp1, temp2)
    if temp1 == 0:
        best = (temp1, temp2)
        break

print(best[1])
print(best[0])