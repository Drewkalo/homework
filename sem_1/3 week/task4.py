def paint_triangle(st, char):
    if st % 2 == 0:                         #для четного кол-ва
        i = 1
        for i in range(1,st//2 + 1):
            print(char * i)
        for i in range(st//2, 0, -1):
            print(char * i)
    else:
        for i in range(1,int(st/2 + 2)):
            print(char * i)
        for i in range(int(st/2), 0, -1):
            print(char * i)
            
paint_triangle(99, "{}")