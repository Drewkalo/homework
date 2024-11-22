num = int(input())
ptx = []
for i in range(num):
    x, y = map(int, input().split())
    ptx.append((x, y))

if num == 0:
    print(1)
else:
    x_dots = {}
    for x, y in ptx:
        if x in x_dots:
            x_dots[x].append(y)
        else:
            x_dots[x] = [y]

symm = False
for x in x_dots:
    symm_x = None
    for temp_symm_x in x_dots:
        if temp_symm_x != x and len(x_dots[x]) == len(x_dots[temp_symm_x]):
            symm_dot = True
            for y in x_dots[x]:
                if y not in x_dots[temp_symm_x]:
                    symm_dot = False
                    break
            if symm_dot == True:
                symm_x = temp_symm_x
                break


    if symm_x is not None:
        symm = True
        break

for i in x_dots:
    for 
if symm == True:
    print(1)
else:
    if len(x_dots) != 1:
        print(0)
    else:
        print(1)
