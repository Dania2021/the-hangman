"""
Hangman images
"""


def hangman_img(tries):
    """
    Displays Hang-Hangman visuals to show man been hung on letter not in word.
    """
    lives_left = [
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |      |
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |
        |
        |
        -
        ''',
        '''
        --------
        |      |
        |
        |
        |
        |
        -
        ''',
      ]
    return lives_left[tries]
