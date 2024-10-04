
def even(n):
    if n < 2 and n != 1:
        return False
    if n == 2 or n == 1:
        return True
    else:
        return even(n/2)


print(even(60))