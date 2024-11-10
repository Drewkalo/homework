def revers(string):                                 #упр3 не аналогично упр1?

 sign = {"+": 1, "-": 1, "*": 2, "/": 2}            #словарь с приоритетами операций
 cache = []                                         #Заводим 2 списка. Один с хранением знаков операций, другой с выходной строкой
 out = []

 for chr in string.split():                         #проходим по каждому элементу строки и отправляем его либо в кеш, если это оператор, либо сразу в выход, если это число
  if chr.isdigit():
   out.append(chr)

  elif chr in sign:                                 #это условие вытаскивает из кеша оператор сразу в строку-выход, если chr имеет приоритет выше (get достаёт значение из словаря операторов по ключу, который мы указали, если такого ключа нет, то возвращает 0)
   while len(cache) != 0 and sign.get(cache[-1], 0) >= sign[chr]:
    out.append(cache.pop())
   cache.append(chr)

  elif chr == "(":                                  #работа со скобками
   cache.append(chr)

  elif chr == ")":                                  #это условие добавляет все операнды, после "(" в строку-выход, пока "(" не станет последней в кеше, после удаляем и её
   while len(cache) != 0 and cache[-1] != "(":
    out.append(cache.pop())
   cache.pop()

 while len(cache) != 0:                             #сбрасываем весь оставшийся кеш в строку выхода
  out.append(cache.pop())

 return " ".join(out)                               #собираем строку из списка



formula = "( 2 - 3 ) * ( 12 - 10 ) + 4 / 2"

print(f"Обратная польская нотация: {revers(formula)}") #прямую не придумал