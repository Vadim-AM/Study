import random


def head(wins, loses):
    word_list = ['python', 'java', 'swift', 'javascript']
    chosen_word = list(random.choice(word_list))
    start_word = list('-' * len(chosen_word))
    repeat_check = []
    body(start_word, chosen_word, repeat_check, wins, loses, attempts=8)


def menu(wins, loses):
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    player_action = input()
    match player_action:
        case 'play':
            head(wins, loses)
        case 'results':
            print(f'You won: {wins} times\n', f'You lost: {loses} times')
            menu(wins, loses)
        case 'exit':
            return None
        case _:
            menu(wins, loses)


def letter_replace(start_w, chosen_w, let_r):
    for i, j in enumerate(chosen_w):
        if j == let_r:
            start_w[i] = let_r


def body(start_word, chosen_word, repeat_check, wins, loses, attempts):
    while attempts != 0 and start_word != chosen_word:
        print(''.join(start_word))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            if letter in repeat_check:
                print('Please, input a single letter.')
            elif letter not in repeat_check:
                repeat_check.append(letter)
                print('Please, input a single letter.')
        elif not letter.islower():
            print('Please, enter a lowercase letter from the English alphabet.')
        elif letter not in chosen_word:
            if letter in repeat_check:
                print("You've already guessed this letter.")
            elif letter not in repeat_check:
                repeat_check.append(letter)
                attempts -= 1
                print("That letter doesn't appear in the word.")
        elif letter in chosen_word:
            if letter in repeat_check:
                print("You've already guessed this letter.")
            elif letter not in repeat_check:
                repeat_check.append(letter)
                letter_replace(start_word, chosen_word, letter)
                if chosen_word == start_word:
                    wins += 1
                    return print(f'You guessed the word {"".join(chosen_word)}!\n', 'You survived!'), menu(wins, loses)
    if attempts == 0:
        loses += 1
        return print('You lost!'), menu(wins, loses)


print('H A N G M A N')
menu(wins=0, loses=0)
