"""
All imports
"""
import os   # credit to stackoverflow.com
import random
import operator
import gspread
from google.oauth2.service_account import Credentials
from title import GAME_TITLE
from gallows import hangman_img
from words import word

# code taken from love-sandwiches project.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPEd_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPEd_CREDS)
SHEET = GSPREAD_CLIENT.open('the_hangman')


high_score = SHEET.worksheet('score')
scores = high_score.get_all_records()
player_score = {}


def clear_terminal():
    """
    clear the terminal
    """
    # This line is credited to
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system("cls" if os.name == "nt" else "clear")


def update_highscores_sheet():
    """
    Add user name and score to google sheet
    """
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_results = [{'range': 'A1:ZZZ1', 'values': [keys]},
                      {'range': 'A2:ZZZ2', 'values': [values]}]
    high_score.batch_update(update_results)


def high_scores():
    """
    Get and sort data from google sheet.
    Return top 5 highscore items.
    """
    scores = high_score.get_all_records()
    clear_terminal()
    print(GAME_TITLE)
    print('\033[1m                  High Scores \033[93m\n\n')
    # This line is credited to
    # https://stackoverflow.com/questions/27447953/how-to-sort-this-list-by-the-highest-score
    ordered_scores = (dict(sorted(scores[0].items(),
                      key=operator.itemgetter(1), reverse=True)[:5]))
    for key, val in ordered_scores.items():
        print(f'\033[93m{key} : \033[0m{val}')
    print('\n')
    while True:
        back = input(
            '\033[93m Go back to main menu? (Press Y)\033[94m\n '
            ).upper()
        if back == 'Y':
            clear_terminal()
            print(GAME_TITLE)
            display_menu()
        else:
            # If users input is not valid:
            print('\033[93m Please try again')


def display_menu():
    """
    Display game header and choice of menu options
    """
    clear_terminal()
    print(GAME_TITLE)
    game_options = True

    while game_options:
        print('\033[94m Press 1 \033[0m to start the game')
        print('\033[94m Press 2 \033[0m to view the rules')
        print('\033[94m Press 3 \033[0m to view high scores')
        print('\033[94m Press 4 \033[0m to quit the game')
        option = input('\033[93m Press the number to continue \033[94m\n ')
        if option == '1':
            get_user_name()
            game_options = False
        elif option == '2':
            game_rules()
            game_options = False
        elif option == '3':
            high_scores()
            game_options = False
        elif option == '4':
            opt = input(
                '\033[93m Are you sure you want to quit?'
                '\033[94m (Y / N)\n '
                ).upper()
            while game_options:
                if opt == 'Y':
                    print(
                        '\033[93m You have successfully quit,'
                        'see you next time \n'
                        )
                    exit()
                elif opt == 'N':
                    print('\n')
                    print(GAME_TITLE)
                    break
                else:
                    # If users input is not valid:
                    print('\n')
                    print('\033[93m Invalid input please try again.\n\033[94m')
                    print('\n')
                    print('\n')
                    opt = input(
                        '\033[93m Press Y for Yes or N for No.. \033[94m\n '
                    ).upper()
        else:
            # If users input is not valid:
            print(
                '\033[93m Did not press 1, 2, 3 or 4...Please try again\n'
                )


def game_rules():
    """
    Display rules of the game and ask if user is ready to play.
    """
    clear_terminal()
    rules = True
    print(GAME_TITLE)
    print('')
    print('\033[1m                  Game Rules \033[93m\n\n')
    print(
        ' * To play hangman, all you need to do is to guess the word one '
        'at a time.\n * Type a letter of your choice and hit enter.\n * If '
        'your guess is correct, the letter will show within the hidden '
        'word.\n * If your guess is incorrect, a section of hangman will '
        'appear.\n * Keep guessing until you guess the correct word '
        'or you run out of tries.\n * If user guess the correct word, '
        'it will add 5 points to the final score.\n * If user accumulated '
        'enough points it will be able to add its name to the high scores'
        )

    print('\n')
    ready = input(
        '\033[93m Are you ready to start the game?\033[94m (Y / N)\n '
        ).upper()

    while rules:
        if ready == 'Y':
            get_user_name()
            rules = False
        elif ready == 'N':
            print(GAME_TITLE)
            display_menu()
            rules = False
        else:
            # If users input is not valid:
            print('\n')
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            ready = input(
                '\033[93m Press Y for Yes or N for No\033[94m\n '
                ).upper()


def get_user_name():
    """
    Display the user name with a welcome message and reset game score
    """
    global user
    clear_terminal()
    print(GAME_TITLE)
    user_name = True

    while user_name:
        # Strip takes away the spaces when writing the name
        user = input('\033[93m Please enter your name.\033[94m\n ').strip()
        if user.isalpha():
            print(f'\033[0m Welcome \033[94m{user}\033[0m, nice to meet you')
            player_score[user] = 0
            print('\n')
            input('\033[93m Press enter to continue')
            difficulty_level()
            user_name = False
        else:
            # If users input is not valid:
            print('\n')
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            print('\033[93m Name can only be letters.\033[94m\n')


def difficulty_level():
    """
    Gets level value from user and creates word list accordingly
    """
    clear_terminal()
    print(GAME_TITLE)
    choose = True
    while choose:
        choose_level = input(
            '\033[93m What difficulty level you want to choose:\n\n'
            ' 1. Easy\n 2. Hard\n \033[94m\n '
        )
        if choose_level == '1':
            easy_words = [easy for easy in word if len(easy) < 5]
            words = random.choice(easy_words)
            start_game(words)
            choose = False
        elif choose_level == '2':
            hard_words = [hard for hard in word if len(hard) > 4]
            words = random.choice(hard_words)
            start_game(words)
            choose = False
        else:
            # If users input is not valid:
            print('\n')
            print('\033[93m Invalid input please try again.\033[94m')
            print('\n')
            print('\n')
            print(
                '\033[93m Press 1 for Easy Game and Press 2 for Hard Game.'
                '\033[94m\n'
            )


def start_game(words):
    """
    Starts the game by asking user for letter input
    If user guess the correct word then 5 points are added to the score
    Ask user to continue upon game end and validate for user input.
    Add user score in high scores if enough points accumulated.
    """
    lives = 6
    guess_letter = []
    words_letter = set(words)
    clear_terminal()
    print(GAME_TITLE)
    while lives > 0 and len(words_letter) > 0:
        hidden_word = [
            letter if letter in guess_letter else
            '_' for letter in words
            ]
        print(hangman_img(lives))
        print('\n ')
        print(' '.join(hidden_word))
        print('\n')
        # User ask to enter a letter
        users_guess = input(
            '\033[93m Please enter a letter: \033[94m\n '
            ).upper()
        print('\n')
        if len(users_guess) > 1:
            # If the user guess two letter
            print(
                f'\033[93m You can only guess 1 letter at a time '
                f'\033[93m You guessed \033[94m{len(users_guess)}'
                f' letter.\033[94m'
                )
        elif not users_guess.isalpha():
            # If the user guess is not a letter
            print(
                f'\033[93m You can only guess letter '
                f'\033[93m You guessed \033[94m{users_guess}, '
                '\033[93mis not a letter.\033[94m'
                )
        # If users guess is valid input:
        elif len(users_guess) == 1 and users_guess.isalpha():
            if users_guess in guess_letter:
                # If the user has already guessed this letter:
                print(
                    f'\033[93m You have already guessed'
                    f'\033[94m {users_guess}.'
                    )
                print('\033[93m You have these letters so far \033[94m ')
                print(' '.join(guess_letter))
            elif users_guess not in words:
                # If the user guess is not in the word:
                clear_terminal()
                print(GAME_TITLE)
                print(
                    f'\033[94m{users_guess} \033[1;31m is not in the word'
                    )
                lives -= 1
                print(f'\033[0mNumber of lives left: {lives} \n')
                guess_letter.append(users_guess)
                print('\033[93mYou have these letters so far \033[94m ')
                print(' '.join(sorted(guess_letter)))
            else:
                # If the user guess a correct letter:
                clear_terminal()
                print(
                    f'\033[94m{users_guess} \033[1;32mis in the word, '
                    'Well done!!'
                    )
                guess_letter.append(users_guess)
                print('\033[93mYou have these letters so far \033[94m ')
                print(' '.join(sorted(guess_letter)))
                if users_guess in words_letter:
                    words_letter.remove(users_guess)
        else:
            # If users input is not valid:
            print('\033[93m Please try again \033[94m')

    if lives != 0:
        # If the user wins and gets the whole word:
        clear_terminal()
        print(GAME_TITLE)
        print('\033[93m Congratulations! You WON')
        print(f' You guessed the word \033[94m{words} \033[93mcorrectly \n')
        while True:
            play_again_after_win = input(
                '\033[93m Would you like to play again? ( Y / N ) \033[94m\n '
            ).upper()
            if play_again_after_win == 'Y':
                player_score[user] += 5
                difficulty_level()
            elif play_again_after_win == 'N':
                player_score[user] += 5
                if user not in scores[0].keys():
                    scores[0][user] = player_score[user]
                    print(
                        f'{user} your final score is'
                        f'\033[94m {player_score[user]}'
                        )
                    update_highscores_sheet()
                    display_menu()
                elif player_score[user] > scores[0][user]:
                    scores[0][user] = player_score[user]
                    update_highscores_sheet()
                    display_menu()
                else:
                    display_menu()
            else:
                # If users input is not valid:
                print('\033[93m Invalid input please try again.\033[94m')
                print('\n')
                print('\n')
                print("\033[93m Please choose Y for Yes and N for No:")
    else:
        # If the user runs out of lives:
        clear_terminal()
        print(GAME_TITLE)
        print(hangman_img(lives))
        print(
            f'\033[93m You are out of lives \n'
            f' The word you have to guess was \033[94m{words}'
        )
        print(
            f' {user} your final score is'
            f'\033[94m {player_score[user]}'
        )
        if user not in scores[0].keys():
            scores[0][user] = player_score[user]
            update_highscores_sheet()
        elif player_score[user] > scores[0][user]:
            scores[0][user] = player_score[user]
            update_highscores_sheet()
        else:
            display_menu()
        while True:
            play_again_after_lose = input(
                '\033[93m Would you like to play again? ( Y / N ) \033[94m\n '
                    ).upper()
            if play_again_after_lose == 'Y':
                difficulty_level()
            elif play_again_after_lose == 'N':
                display_menu()
            else:
                # If users input is not valid:
                print('\033[93m Invalid input please try again.\033[94m')
                print('\n')
                print('\n')
                print("\033[93m Please choose Y for Yes and N for No:")


if __name__ == '__main__':
    display_menu()
