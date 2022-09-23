"""
All imports
"""
import os
import random
from title import game_title


def clear_terminal():
    """
    clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    """
    Display game header and choice of menu options
    """
    clear_terminal()
    print(game_title)
    game_options = True

    while game_options:
        print('\033[94m Press 1 \033[0m to start the game')
        print('\033[94m Press 2 \033[0m to view the rules')
        print('\033[94m Press 3 \033[0m to quit the game')
        option = input('\033[93m Press the number to continue\n\033[94m')
        if option == '1':
            get_user_name()
            game_options = False
        elif option == '2':
            game_rules()
            game_options = False
        elif option == '3':
            opt = input(
                '\033[93m Are you sure you want to quit?'
                '\033[94m Yes or No\n'
                )
            while game_options:
                if opt == 'y' or opt == 'yes':
                    print(
                        '\033[93m You have successfully quit,'
                        'see you next time \n'
                        )
                    exit()
                elif opt == 'n' or opt == 'no':
                    print('\n')
                    print(game_title)
                    break
                else:
                    print('\n')
                    print('\033[93m Invalid input please try again.\n\033[94m')
                    print('\n')
                    print('\n')
                    opt = input(
                        '\033[93m Press y for Yes or n for No..\n\033[94m'
                        )
        else:
            print(
                '\033[93m Did not press 1, 2 or 3...Please try again\n'
                )


def game_rules():
    """
    Display rules of the game and ask if user is ready to play.
    """
    clear_terminal()
    rules = True
    print(game_title)
    print('')
    print('\033[1m                  Game Rules \033[93m\n\n')
    print(
        ' * To play hangman, all you need to do is to guess the word one '
        'at a time.\n * Type a letter of your choice and hit enter.\n * If '
        'your guess is correct, the letter will show within the hidden'
        'word.\n * If your guess is incorrect, a section of hangman will'
        'will appear.\n * Keep guessing until you guess the correct word'
        'or you run out of tries')

    print('\n')
    ready = input(
        '\033[93m Are you ready to start the game?\033[94m Yes or No\n'
       )

    while rules:
        if ready == 'y' or ready == 'yes':
            get_user_name()
            rules = False
        elif ready == 'n' or ready == 'no':
            print(game_title)
            display_menu()
            rules = False
        else:
            print('\n')
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            ready = input('\033[93mPress y for Yes or n for No\033[94m \n')


def get_user_name():
    """
    Display the user name with a welcome message
    """
    clear_terminal()
    print(game_title)
    user_name = True

    while user_name:
        user = input('\033[93m Please enter your name.\033[94m\n ')
        if user.isalpha():
            print(f'\033[0m Welcome \033[94m{user}\033[0m, nice to meet you')
            start_game()
            user_name = False
        else:
            print('\n')
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            print('\033[93m Name can only be letterrs.\033[94m\n')


word = ['APPLE', 'BANANA', 'ORANGE', 'GRAPES']


def start_game():
    """
    Starts the game by asking user for letter input
    """
    lives = 6
    guess_letter = []
    words = random.choice(word)
    words_letter = set(words)
    clear_terminal()
    print(game_title)
    while lives > 0 and len(words_letter) > 0:
        hidden_word = [
            letter if letter in guess_letter else "_" for letter in words
            ]
        print("\n")
        print(" ".join(hidden_word))
        print("\n")
        users_guess = input(
            "\033[93mPlease enter a letter: \033[94m\n"
            ).upper()
        print("\n")
        try:
            if len(users_guess) > 1:
                raise ValueError(
                    f'\033[93mYou can only guess 1 letter at a time '
                    f'\033[93m You guessed \033[94m{len(users_guess)} letter.'
                    )
            elif not users_guess.isalpha():
                raise ValueError(
                    f'\033[93mYou can only guess letter '
                    f'\033[93m You guessed \033[94m{users_guess},'
                    '\033[93mis not a letter.'
                )
            elif len(users_guess) == 1 and users_guess.isalpha():
                if users_guess in guess_letter:
                    raise ValueError(
                        f'\033[93mYou have already guessed'
                        f'\033[94m {users_guess}.'
                        )
                    print('\033[93mYou have these letters so far \033[94m')
                    print(' '.join(guess_letter))
                elif users_guess not in words:
                    clear_terminal()
                    print(game_title)
                    print(
                        f'\033[94m{users_guess} \033[1;31m is not in the word'
                        )
                    lives -= 1
                    print(f'\033[0mNumber of lives left: {lives} \n')
                    guess_letter.append(users_guess)
                    print('\033[93mYou have these letters so far \033[94m')
                    print(' '.join(sorted(guess_letter)))
                else:
                    clear_terminal()
                    print(game_title)
                    print(
                        f'\033[94m{users_guess} \033[1;32m is in the word, '
                        'Well done!!'
                        )
                    guess_letter.append(users_guess)
                    print('\033[93mYou have these letters so far \033[94m')
                    print(' '.join(sorted(guess_letter)))
                    if users_guess in words_letter:
                        words_letter.remove(users_guess)

        except ValueError as err:
            print(f'{err} \033[93m Please try again \033[94m')
            continue
   

display_menu()
