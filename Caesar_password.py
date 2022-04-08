direction = input('Шифровать(введите "0")\nили дешифрировать(введите"1")?:\n')
if direction == '1':
    direction = -1
else:
    direction = 1
text_lang = input('Введите язык:\neng/rus: ')
eng_lower_alphabet = [chr(i) for i in range(97, 123)] * 2
eng_upper_alphabet = [chr(i) for i in range(65, 91)] * 2
rus_lower_alphabet = [chr(i) for i in range(1072, 1104)] * 2
rus_upper_alphabet = [chr(i) for i in range(1040, 1072)] * 2
shifting = (int(input('Введите сдвиг:\n')) * direction)
text = input('Введите текст:\n').split(' ')
output_text = []


def symbol_shift_eng(shift):
    for i in text:
        if i in eng_upper_alphabet:
            output_text.append(eng_upper_alphabet[eng_upper_alphabet.index(i) + shift])
        elif i in eng_lower_alphabet:
            output_text.append(eng_lower_alphabet[eng_lower_alphabet.index(i) + shift])
        else:
            output_text.append(i)
    return print(*output_text, sep='')


def symbol_shift_rus(shift):
    for i in text:
        if i in rus_upper_alphabet:
            output_text.append(rus_upper_alphabet[rus_upper_alphabet.index(i) + shift])
        elif i in rus_lower_alphabet:
            output_text.append(rus_lower_alphabet[rus_lower_alphabet.index(i) + shift])
        else:
            output_text.append(i)
    return print(*output_text, sep='')


def symbol_shift(lang):
    if lang == 'rus':
        return symbol_shift_rus(shifting)
    if lang == 'eng':
        return symbol_shift_eng(shifting)


symbol_shift_eng(shifting)
