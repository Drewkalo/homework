def prime(n, pr_di = []):
    if n == 1:                          #Проверка на тривиальный случай
        return pr_di
    
    for i in range(2,n):
        if n % i == 0:
            pr_di.append(i)             #Добавляем простой множитель в список
            return prime(n//i, pr_di)   #Возвращаем значение функции
        
    pr_di.append(n)                     #Добавляем в список, если число само простое 
    return pr_di

print(prime(17))