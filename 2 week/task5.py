c = [j for j in input() if j != ' ']
print(c[-1:] + c[:-1])                  #c[-1] + c[:-1] приводит к ошибке, потому что мы конкатенируем строку и список (":" роляет xDD)