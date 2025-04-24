prefix = [0, 0, 1, 0, 0, 1]

def prefix_to_word(prefix):
    if len(prefix) == 0:
        return ''
    
    word = [''] * len(prefix)
    word[0] = 'A'
    # пробегаемся по всем значениям массива
    for i in range(1, len(prefix)):
        # если значение не 0, то буквы i и i - prefix[i] -1 совпадают
        if prefix[i] != 0:
            word[i] = word[prefix[i] - 1]
        # иначе смотрим, какие буквы могут дополнить до префикса, запоминаем их
        else:
            used_letters = set()
            used_letters.add('A')

            k = prefix[i-1]
            while k>0:
                used_letters.add(word[k])
                k = prefix[k-1]
        # выбор буквы от A до Z, которая не использовалась
            for letter in range(65, 123):
                if chr(letter) not in used_letters:
                    word[i] = chr(letter)
                    break

    return ''.join(word)
print(prefix_to_word(prefix))