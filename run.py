"""
All imports
"""
import os
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
            print('Hello')
            rules = False
        elif ready == 'n' or ready == 'no':
            print(game_title)
            display_menu()
            rules = False
        else:
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            ready = input('\033[93mPress y for Yes or n for No\033[94m \n')


display_menu()
