def solve(string):
                        #заводим список, для хранения чисел и промежуточных вычислений, разбиваем строку на список
  cache = []
  chrs = string.split()

  for chr in chrs:              #если символ это число, то отправляем с кеш
    if chr.isdigit():
      cache.append(int(chr))
      
    elif chr in "+-/*":         #если же символ это оператор, то достаём из кеша 2 последних числа и проводим вычисление
        try:
            num2 = cache.pop()
            num1 = cache.pop()
            if chr == "+":          #можно юзать eval
                res = num1 + num2   #также не забываем про возможные ошибки, поэтому юзаем try-except
            elif chr == "-":
                res = num1 - num2
            elif chr == "/":
                res = num1 / num2
            elif chr == "*":
                res = num1 * num2
            else:
               return "Error!"
            cache.append(res)
        except:
           return "Error!"
        
    else:
      return "Error!"

  if len(cache) != 1:
    return "Error!"

  return cache[0]                   #возврашаем ответ

formula = "2 3 - 12 10 - * 4 2 / +"

print(f"Ответ: {solve(formula)}")

