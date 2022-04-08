_welcome_message = 'Добро пожаловать в числовую угадайку'
_bye_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
_play_again_message = 'Would you like to play again?'
_pay_message = 'Very good! Pay 1 USD :D'
_wrong_input_message = 'Wrong input'

_MIN = 1
_MAX = 100


def is_valid(st, min_val, max_val):
    if st.isnumeric():
        val = int(st)
        if min_val <= val <= max_val:
            return val
    return False


def get_guess():
    while True:
        val = is_valid(input('Type in your guess here:\n'), _MIN, _MAX)
        if val:
            return val
        print(f'А может быть все-таки введем целое число от {_MIN} до {_MAX}?')


def welcome():
    print(_welcome_message)


def bye():
    print(_bye_message)


def play_again():
    print(_play_again_message)
    if input('Press "Y" to play again!\n').lower() == 'y':
        print(_pay_message)
        s = input('Type your payment amount\n')
        try:
            if s.isnumeric() and int(s) > 1:
                print('here is your change', int(s) - 1)
            return True
        except Exception as error:
            print(_wrong_input_message)
    else:
        return False


def game(num_to_guess):
    while True:
        guess = get_guess()
        if num_to_guess == guess:
            print('Holly shoot, man! You did it! :)))')
            break

        elif guess < num_to_guess:
            print('Too low..')
        else:
            print("You're thinking too BIG, dude!")


def start():
    from random import randint
    welcome()
    while True:
        game(randint(_MIN, _MAX))
        if not play_again():
            break
    bye()


start()
