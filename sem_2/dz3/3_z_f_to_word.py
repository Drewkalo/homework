zf = [0,0,1,0,3,0,1]

def convert_zf_to_word(zf):
    if len(zf) == 0:
        return ''
    word = [''] * len(zf)
    word[0] = 'A'
    left_border,right_border = 0,0
    curr_letter = 66

    # пробегаемся по всем элементам z-массива
    for i in range(1, len(zf)):
    # если за границей самого крайнего совпадения префиксов
        if i > right_border:
            if zf[i] == 0:                  # случай уникальной буквы, тривиально обновляем
                word[i] = chr(curr_letter)
                curr_letter += 1
                left_border, right_border = i, i
            else:                           # случай ненулевого значения, смотрим, что нужно скопировать [i: i + zf[i] - 1]
                for j in range(zf[i]):
                    if i + j >= len(zf):    # проверка выхода за границу слова
                        break
                    word[i+j] += word[j]    
                                            # обновляем границы
                left_border, right_border = i, i + zf[i] - 1

    # если находимся внутри крайней совпавшей подстроки          
        else:
            pos = i - left_border       # позиция внутри префикса
            if zf[pos] < right_border - i + 1:  # если совпадающих меньше, чем правая граница начального префикса, значит нужно скопировать символ
                word[i] = word[pos]
            else:                       # иначе обновляем за границей, копируя символы и обновляя границы
                for j in range(right_border - i + 1, zf[pos]):
                    if i + j >= len(zf):
                        break
                    word[i+j] = word[j]
                left_border, right_border = i, i + zf[pos] - 1

    return ''.join(word)

print(convert_zf_to_word(zf))