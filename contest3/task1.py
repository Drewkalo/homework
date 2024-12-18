def heapify(s, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and s[l] > s[smallest]:
        smallest = l
    if r < n and s[r] > s[smallest]:
        smallest = r
    if smallest != i:
        s[i], s[smallest] = s[smallest], s[i]
        heapify(s, n, smallest)

def find_k_small(s, k):
    for i in range(k // 2 - 1, -1, -1):
        heapify(s, k, i)

    for i in range(k, len(s)):
        if s[i] < s[0]:
            s[0] = s[i]
            heapify(s, k, 0)
    return s[:k]

n, k = map(int, input().split())
s = [int(i) for i in input().split()]

k_smallest = find_k_small(s, k)
print(*sorted(k_smallest))