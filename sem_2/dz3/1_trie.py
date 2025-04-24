alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Node:
    def __init__(self):
        self.children = {}
        self.parent = None
        self.output = None

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self,s):
        v = self.root
        for c in s:
            if c in v.children:
                v = v.children[c]
            else:
                new_v = Node()
                new_v.parent = v
                v.children[c] = new_v
                v = new_v
        v.output = s
    
    def find_word(self, word):
        v = self.root
        for letter in word:
            # если буква в дереве, то спускаемся в неё
            if letter in v.children:
                v = v.children[letter]
            # если в какой-то момент не сможем, то слова нет
            else:
                return False
            # проверка, что вершина, в котором заканчивается слово, является терминальной
        if v.output != word:
            return False
        else:
            return True
        
    def del_word(self, word):
        # проверка, есть ли слово в боре
        v = self.root
        for letter in word:
            if letter not in v.children:
                return
            v = v.children[letter]

        if v.output != word:
            return
        # если есть, то снимаем метку
        v.output = None
        # поднимаемся вверх, если это не корень, у него нет детей и она не терминальная
        while v != self.root and not v.children and v.output is None:
            # родитель
            parent = v.parent
            # ищем текущую вершину в родителе и удаляем
            for letter, node in parent.children.items():
                if node is v:
                    del parent.children[letter]
                    break
            # поднялись к родителю
            v = parent

        