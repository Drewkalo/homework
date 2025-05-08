inp = [int(i) for i in input().split()]
price = [int(i) for i in input().split()]
tickets = [input().strip() for _ in range(inp[0])]

pref_mass = {}
for ticket in tickets:
    for i in range(1, inp[1] + 1):
        pref = ticket[:i]
        if pref in pref_mass:
            pref_mass[pref] += 1
        else:
            pref_mass[pref] = 1
#print(pref_mass)

best_ticket = ''
for i in range(inp[1]):
    min_count = float('inf')
    best_digit = 0
    for digit in range(inp[2]):
        curr = best_ticket + str(digit)
        count = pref_mass.get(curr, 0)
        if (count < min_count) or (count == min_count and digit < best_digit):
            min_count = count
            best_digit = digit

    best_ticket += str(best_digit)
#print(best_ticket)

fruits = 0
for i in range(1, inp[1] + 1):
    temp = pref_mass.get(best_ticket[:i], 0)
    #print(temp)
    if i < inp[1]:
        next = pref_mass.get(best_ticket[:i+1], 0)
    else:
        next = 0
    fruits += (temp - next) * price[i-1]

print(best_ticket, fruits, sep='\n')