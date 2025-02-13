def price(s, l):
    if s == 1 or s == 0:
        return 0
    pr = min(price(s-1,l) + l[s-1], price(s-2,l) + l[s-2])
    return pr


l = [1,2,1,2,1]
print(price(5, l))