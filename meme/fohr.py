import unittest

def factor(n, pr_di = []):
    if n == 1:                          #Проверка на тривиальный случай
        return pr_di
    
    for i in range(2,n):
        if n % i == 0:
            pr_di.append(i)             #Добавляем простой множитель в список
            return factor(n//i, pr_di)   #Возвращаем значение функции
        
    pr_di.append(n)                     #Добавляем в список, если число само простое 
    return pr_di

class TestOrdinaryNumber(unittest.TestCase):
    def test_factor(self):
        self.assertEqual(factor(1), [1])
        self.assertEqual(factor(2), [2])
        self.assertEqual(factor(4), [2,2])
        self.assertEqual(factor(0), [])

unittest.main()