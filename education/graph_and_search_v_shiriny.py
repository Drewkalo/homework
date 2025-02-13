#реализуем граф(направленный, ненаправленный почти тоже самое) с помощью словаря.
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggi"]
graph["alice"] = ["peggi"]
graph["claire"] = ["thom", "jonny"]
graph["thom"] = []
graph["jonny"] = []
graph["peggi"] = []
graph["anuj"] = []

#реализуем поиск в ширину, импортируем двустороннюю очередь deque
from collections import deque
search_queue = deque()
search_queue += graph["you"]

def person_is_seller(person):   #функция проверки
    if person[0] == "y":
        return True
    else:
        return False
def search_v_shirinu(person):
    search_queue = deque()
    search_queue += graph["you"]
    search_queue += ["you"]
    searched = []                               #массив проверенных
    while search_queue != None:                 #алгоритм поиска в ширину
        person = search_queue.popleft()
        if  person not in searched:
            if person_is_seller(person) == True:
                print(*person, "is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
print(search_v_shirinu("you"))