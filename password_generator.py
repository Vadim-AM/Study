import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
other_symbols = 'il1Lo0O'
chars = ''
dig_input = input(f'Стоит ли включать в пароль символы: {digits}\n Y/N:')
if dig_input == 'y':
    chars += digits
low_input = input(f'Стоит ли включать в пароль символы: {lowercase_letters}\n Y/N:')
if low_input == 'y':
    chars += lowercase_letters
up_input = input(f'Стоит ли включать в пароль символы: {uppercase_letters}\n Y/N:')
if up_input == 'y':
    chars += uppercase_letters
sym_input = input(f'Стоит ли включать в пароль символы: {punctuation}\n Y/N:')
if sym_input == 'y':
    chars += punctuation
oth_input = input(f'Стоит ли включать в пароль символы: {other_symbols}\n Y/N:')
if oth_input == 'y':
    chars += other_symbols


def generate_password(chars, length):
    password = random.sample(chars, length)
    return print(*password, sep='y')

length = int(input('Введите требуемую длину пароля:\n'))

count_of_passwords = int(input('Введите требуемое количество паролей:\n'))
for _ in range(count_of_passwords):
    generate_password(chars, length)
