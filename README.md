# The Hangman

The Hangman is a Python terminal game, which runs on a mock terminal on Heroku.

It is a word guessing game. User can enter its name and choose between 2 difficulty levels. Hangman game requires user to reveal the hidden word by guessing the individual letters. Player has 6 attempts per word, if the letter is in the word the letter is shown and another guess can be made. If the letter is wrong a visual of the traditional hangman man will start to appear, game continues until user either guess the correct word or lose all of its lives.

![Title image](/images/hangman-title-img.png)

Visit the deployed site [The Hangman](https://the-hangman22.herokuapp.com/)

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Goals](#user-goals)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
* Design
  * Flowchart
  * Colour
* Features
  * Welcome Screen
  * Start Game Screen
   * Username Screen
   * Difficulty Level Screen
   * Guessing Screen
     * Correct Answer Message
     * Incorrect Answer Message
     * Invalid Guess
     * Display of Hangman
     * Win Screen
     * Lose Screen
  * Rules Screen
  * High Scores Screen
  * Quit Game Screen
  * Extra Features
* Technologies Used
  * Laguages Used
  * Frameworks, Libraries & Programs Used
* Deployment & Local Development
  * How to Fork
  * How to Clone
  * Setting up google sheets API
  * Setting up Heroku
* Testing
  * Validator Tests
  * Lighthouse Test
  * Manual Testing
  * Bugs
* Credits

## User Experience (UX)

  ### User Goals
   * As a user I want to have fun.
   * As a user I want the game to be challenging.
   * Intuitive and responsive to user's interaction
   * Easily navigated around
   * High scores should be stored and accessible to other users to view it

  ### Project Goals
   * As the site owner I want the user to have a fun experience.
   * As the site owner I want the game to be functional with no bugs or errors.

  ### User Stories
  As a user I want to
   * See welcome page with menu option
   * Know how the game works
   * See list of 5 best players
   * See my score
   * be informed if my data input is not valid and why
   * see which letters I have already guessed
   * see the word being displayed for every correct guess
   * be informed how many lives I have left after a wrong guess
   * see a graphic visualising my lost lives
   * learn the word to be guessed after losing the game
   * see the full word displayed after completing the game successfully
   * know when the game is over (won or lost)
   * be able to restart the game or not when after it's finished
