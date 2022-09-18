"""
All imports
"""
from title import game_title


def display_menu():
    """
    Display game header and choice of menu options
    """
    game_options = True

    while game_options:
        print('\033[94m Press 1 \033[0m to start the game')
        print('\033[94m Press 2 \033[0m to view the rules')
        print('\033[94m Press 3 \033[0m to quit the game')
        option = input('\033[93m Press the number to continue\n\033[94m')
        if option == '1':
            game_options = False
        elif option == '2':
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


display_menu()
