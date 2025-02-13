with open("C:/Users/Эльмира/Documents/GitHub/homework/2 week/input.txt", 'r') as f:
    a = f.readlines()
    pr = 0
    print(a)

for i in range(len(a)):     #Знаки разделители: ! ? . ... ?!
    c_dot = a[i].count(".")
    c_vop = a[i].count("?")
    c_vos = a[i].count('!')
    c_mndot = a[i].count('...')
    c_vosp = a[i].count('?!')
                            #Считаем кол-во предложений (формула добыта опытным путём xDD)
    pr += ((c_dot - c_mndot*3) + (c_vop - c_vosp) + (c_vos - c_vosp) + c_mndot + c_vosp)

print(pr)