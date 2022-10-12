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
 * [Design](#design)
  * [Colour](#colour)
  * [Flowchart](#flowchart)
* [Features](#features)
  * [Welcome Screen](#welcome-screen)
  * [Username Screen](#username-screen)
   * [Difficulty Level Screen](#difficulty-level-screen)
   * [Guessing Screen](#guessing-screen)
     * [Correct Answer Message](#correct-answer-message)
     * [Incorrect Answer Message](#incorrect-answer-message)
     * [Display of Hangman](#display-of-hangman)
     * [Win Screen](#win-screen)
     * [Lose Screen](#lose-screen)
  * [Rules Screen](#rules-screen)
  * [High Scores Screen](#high-scores-screen)
  * [Quit Game Screen](#quit-game-screen)
* [Technologies Used](#technologies-used)
  * [Laguages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#framework-libraries--programs-used)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
    * [Setting up google sheets API](#setting-up-google-sheets-api)
    * [Setting up Heroku](#setting-up-heroku)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
  * [Validator Tests](#validator-tests)
  * [Lighthouse Test](#lighthouse-tests)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)
* Credits
* [Acknowledgements](#acknowledgements)

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


## Design

  * ### Colour
     I decided to add a color scheme to provide a better user experience. By showing incorrect guesses in red text and correct guesses in green text to make it clearer to the user.

     * General text, Blue ('\033[1;34m'), Yellow('\033[93m') and White('\033[0m'). 
     * Incorrect guesses, Red ('\033[1;31m').
     * Correct guesses, Green (\033[1;32m').
     * Bold('\033[1m') for game rules and high scores heading.

  * ### Flowchart
     I used [Lucidchart](https://lucid.app/documents#/dashboard) to help design the project and create the following flowchart.

     ![Flowchart image](/images/hangman_flowchart.png)


## Features

   I have used clear_terminal function to make it clearer for the user to read.

  * ### Welcome Screen

     This is the first page you see when the app loads. The welcome screen will display the name of the game and ask user to press one of the four options :

      1. Start the game
      2. How to play
      3. High Scores
      4. Quit game

      ![Welcome Screen Image](/images/welcome-screen-img.png)

  * ### Username Screen

      When user press 1 from the welcome screen then user is asked to input a Username so that the game can keep track of the score. If the User puts anything else other than letters, the game will display a text to the User, letting them know name can only be letters. It also display a welcome message to the user and reset the score.

       ![Username Screen Image](/images/welcome-msg-img.png)

  * ### Difficulty Level Screen

      The user is then asked to choose the level of difficulty. There are two options available:
       1. Easy
       2. Hard

       If the user selects easy then random word gets pick from words.py of length less than 5 and if the user selects hard then random word gets pick from words.py of length more than 4.

       ![Difficulty Level Image](/images/level-img.png)

  * ### Guessing Screen

       The Guessing screen displays the hangman title, the first stage of the hangman game. Underneath the hangman display, the user is asked to enter a letter.

       ![Game Start Image](/images/game-start-img.png)


    * #### Correct Answer Message

         When the user guess is valid and also correct, they are greeted with message praising them and stating that their guess is in the word. It also displays how many letters user has used so far and replace blank space with correct guess letter.

         ![Correct Answer Image](/images/correct-guess-img.png)

    * #### Incorrect Answer Message

         When the user guess is valid but is not in the word, they are greeted with message stating that their guess was not in the word, therefore being incorrect user will lose a life and will display the next stage of hangman. It also displays how many lives are left and how many letters user has used so far

         ![Incorrect Answer Image](/images/wrong-guess-img.png)


    * #### Display of Hangman
         
         The user will be able to see their progress of the hangman lives. With each incorrect letter or guess, the hangman image display and will go to the next stage of the display until the user gets the word or runs out of lives.

         ![Hangman stages Image](/images/life-stages.png)      
    
    * #### Win Screen

        If the user guesses all letter correctly it will take them to a screen that congratulates them and will ask the User to input a "Y" for Yes or "N" for No to either play again or exit the game, either options will store their username along with their score to a googlesheet document.

        ![Win Screen Image](/images/win-msg-img.png)

    * #### Lose Screen

        The lose screen is displayed when the user has finally used up all of their lives and lets them know that they have lost the game. When this screen shows, it displays the last stage of the hangman (a stick figure being 'hung'). It also greets the user to an unfortunate message letting the user know that user run out of lives, it also display what the word was and a encouraging text to persuade the User to play again. This screen also display username with the score.

         ![Lose Screen Image](/images/losing-msg-img.png)

  * ### Rules Screen

      The rules screen explains to the user how the game is played and then asks the user if they are ready for the game.

      ![Rules Screen Image](/images/rules-img.png)

  * ### High Scores Screen

       The Highscores screen will display the scores and the usernames of any of the users that have the top 5 scores and will continue to update through the googlesheet. This screen also has an option at the bottom of the screen to let the user know what to input to go back to the Welcome screen.

      ![High Scores Screen Image](/images/high-score-img.png) 

  * ### Quit Game Screen
        
      When the user press 3 from the welcome screen then user gets ask are you sure you want to quit. If the user selects 'Y' option then user exit the game and greets with a message that you have successfully quit and if user selects 'N' option then it will go to the welcome screen.

       ![Quit Screen Image](/images/quit-img.png) 


        
## Technologies Used

  * ### Languages Used

    Python

  * ### Framework, Libraries & Programs Used

    * [Lucidchart](https://lucid.app/documents#/dashboard) -Used to create flowchart

    * [Git](https://git-scm.com/) - Used for version control.
     
    * [Github](https://github.com/) - Used to save and store the files for website.

    * [GitPod](https://gitpod.io/workspaces) - IDE used to create the site.

    * [Google Sheets](https://docs.google.com/spreadsheets/u/0/) - To store information

    * [Gspread](https://docs.gspread.org/en/latest/) - To store information

    * [Random Library](https://docs.python.org/3/library/random.html) -Used to generate a random word

    * [Os Library](https://docs.python.org/3/library/os.html) - Used to clear the console

    * [Operator Library](https://docs.python.org/3/library/operator.html) - Used to sort a dictionary

    * [Heroku](https://id.heroku.com/login) - To deploy project

    * [Text to ASCII generator](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used to make heading logo

    * [Am I Responsive?](https://ui.dev/amiresponsive?)  Show of the mock terminal.

 
## Deployment & Local Development

  * ### Deployment
   
    * #### Setting up google sheets API

      To set up google sheets API you must;

      1. Head to https://console.cloud.google.com/ and sign in or create a free google account.

      2. From the google cloud platform dashboard click 'Select a new project'. Then select 'New project'.

      3. Create a name for your project under 'Project name' then click 'Create'.

      4. This should bring up a box with your project in. Underneath click 'SELECT PROJECT'.

      5. From the sidebar navigate to 'APIs and services', 'Library'.

      6. In the search bar search for google drive.

      7. Select 'Google drive API' and click 'ENABLE'.

      8. Click the 'CREATE CREDENTIALS' button located to the top right of the page.

      9. From the dropdown menu under 'Which API are you using?' select 'Google drive API'.

      10. Under 'What data will you be accessing' choose 'Application data'.

      11. Under 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions?' select 'No, i'm not using them' and click 'NEXT'.

      12. Enter a Service Account Name. You can name it whatever you like. I would suggest naming it the same as what you named your project. Then click 'CREATE AND CONTINUE'.

      13. In the 'Role' dropdown menu select 'Basic', 'Editor', then click 'Continue'.

      14. The next page can be left blank so just click 'DONE'.

      15. Under 'Service Accounts' find the account you just created and click it.

      16. Navigate to the 'KEYS' tab and click 'ADD KEY', 'Create new key'. Select 'JSON' and click 'CREATE'.

      17. This will download a json file to your machine. This normally downloads into your 'downloads' folder but if you're unsure you can right click the file once it's downloaded and click 'show in folder' to locate it.

      18. Next we will have to link the Google Sheets API. To do this navigate back to the library by clicking on the burger icon in the top left hand corner and selecting 'APIs and services', 'Library' from the dropdown menu.

      19. In the search bar search for 'Google Sheets' and select 'Google Sheets API' and click 'ENABLE'.

      20. Now, using a programme like Gitpod open or create a repository.

      21. Drag and drop the json file that you downloaded earlier into your workspace. Rename this file to 'creds.json'.

      22. Open the file and copy the email address under 'client_email' without the quotation marks.

      23. Open up the google sheet you want to use and click the 'Share' button.

      24. Paste in the client email. Make sure 'Editor' is selected, untick 'Notify people' and then click 'Share'.

      25. To protect sensitive information be sure to add your creds.json file to your .gitignore file inside your editor.

      26. In order to use our google sheets API you need to install two additional dependencies into your project. To do this, inside your python workspace on the first line input 'import gspread' and on the line beneath input 'from google.oauth2.service_account import Credentials'.

      27. Underneath the two imports copy and paste this code, inserting the name of your google spreadsheet where it says 'google_sheet_name_here'.

       SCOPE = [ "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive" ]
 
       CREDS = Credentials.from_service_account_file('creds.json') SCOPED_CREDS = CREDS.with_scopes(SCOPE) GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) SHEET = GSPREAD_CLIENT.open('google_sheet_name_here')

      28. Your APIs will now be linked to your project.


    * #### Setting up heroku

      To setup heroku you must

       1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip3 freeze > requirements.txt' then save and push the changes.
       2. Go to Heroku.com and sign in or create a free account.
       3. From the heroku dashboard click the 'Create new app' button.
       4. Name the app something unique and choose what region you are in then click 'Create app'.
       5. Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
       6. If your project does not use a creds.json file then skip this step. Otherwise, in the field for KEY enter the value CREDS in all capitals. In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
       7. In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
       8. Scroll down to the Buildpacks section and click 'Add buildpack'.
       9. Click Python then save changes.
       10. Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
       11. Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
       12. Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
       13. From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
       14. Enter the repository name as it is in GitHub and click 'search'.
       15. Click the 'connect' button next to the repository to link it to heroku.
       16. To deploy, scroll down and click the 'Deploy Branch' button.
       17. Heroku will notify you that the app was successfully deployed with a button to view the app.
       18. If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.


  * ### Local Development

    * #### How to Fork
     
      To fork the The-Hangman repository:

      1. Log in (or sign up) to Github.
      2. Go to the repository for this project, [The-Hangman repository](https://github.com/Dania2021/the-hangman).
      3. Click the Fork button in the top right corner.

   
    * #### How to Clone

      To clone the The-Hangman repository:

      1. Log in (or sign up) to GitHub.
      2. Go to the repository for this project, [The-Hangman repository](https://github.com/Dania2021/the-hangman).
      3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
      4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
      5. Type git clone into the command line and then paste the URL copied from GitHub.
      6. Press enter and the local repository clone will be created.

## Testing

  Bugs and errors encountered during coding of project were solved through contiuned testing throught the development. Using print statements and through git terminal python run.py

   * Checked that when I get a score, it would update automatically in the googlesheets file.

   * Adding over 50 player names to google sheet file to ensure still sorting and displaying correctly.

   * Checked for all scenarios with invalid guesses (numbers, special characters, double characters, spaces).


  ### Validator Tests

  Since the PEP8 website is not properly working at the moment, I added the PEP8 validator into my Gitpod workspace directly, following the Code Institue instructions for installation.
        
  * run.py -  No errors and warnings were returned when passing through PEP8 validator(in Gitpod workspace) 

  * words.py -  No errors and warnings were returned when passing through PEP8 validator(in Gitpod workspace) 

  * title.py -  No errors and warnings were returned when passing through PEP8 validator(in Gitpod workspace)

  * gallows.py -  No errors and warnings were returned when passing through PEP8 validator(in Gitpod workspace)
       
  ### Lighthouse Tests

  I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

  ![Lighthouse Test of Hangman Image](/images/hangman-lighthouse-test.png)

  ### Manual Testing

  1. The user is asked to Press the number on the welcome screen
      
       * First, I tested what would happen if the user typed anything other than 1, 2, 3 or 4: Error message shows, results were as expected.

       ![Welcome Screen invalid input Image](/images/welcome-invalid.png)


       * Next I tested what would happen if the user typed 1: go to the Username Screen, results were as expected.

       * Then I tested what would happen if the user typed 2: go the Rules Screen, results were as expected.

       * Then I tested what would happen if the user typed 3: go to the High Scores Screen, results were as expected.

       * Last I tested what would happen if the user typed 4: Quit the game, results were as expected.

  2. After reading the rules the user is asked if they are ready to start the game, Y for yes and N for no.   

       * I tested what would happen if the user typed anything other than Y or N: Error message shows, results were as expected.

       ![Rules invalid input Image](/images/rules-invalid.png)


       * Next I tested what would happen if the user typed Y: go to the Username Screen, results were as expected.

       * Last I tested what would happen if the user typed N: go to the Welcome Screen.

  3. After viewing the high scores the user is asked go back to the main menu, press Y for yes.

       * I tested what would happen if the user typed anything other than Y: Error message shows, results were as expected.

       ![Back to main menu invalid input Image](/images/high-score-invalid.png)


       * Next I tested what would happen if the user typed Y: go back to the Welcome Screen.

  4. When user go the Username Screen, user is asked to enter your name .

       * I tested what would happen if the user typed anything other than letter: Error message shows, results were as expected. 

       ![Invalid username Image](/images/username-invalid.png)
 

       * Next I tested what would if the user typed letters: display a welcome message with username and ask user to press enter to continue, results were as expected

  5. When the user press enter from the Username Screen then after that user go to the Difficulty Level Screen and user is asked to choose your difficulty level, 1 for Easy and 2 for Hard.

       * First, I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.

       ![Invalid Difficulty Level Image](/images/level-invalid.png)


       * Next I tested what would happen if the user typed 1: Start the game go to the Guessing Screen and guess the word with length of less than 5.

       * Last I tested what would happen if the user typed 2: Start the game go to the Guessing Screen and guess the word with length of more than 4.

  6. Once the user go to the Guessing Screen, user is asked to enter a letter.

       * First I tested what would happen if the user typed anything other than letter: Error message shows, results were as expected.

       ![Invalid guess Image](/images/guess-invalid.png)

       
       * Next I tested what would happen if the user typed more than 1 letter: Error message shows, results were as expected.

       ![Invalid length of guess letter Image](/images/guess-invalid-letter.png)


       * Next I tested what would happen if the user typed a valid but an incorrect guess: message shows, being incorrect user will lose a life and will display the next stage of hangman image and displays how many letters used so far, results were as expected.

       * Then I tested what would happen if the user typed valid and correct guess: message shows, and displays how many letters used so far, results were as expected.

       * Last I tested what would happen if the user typed a letter they had already guessed: You have already guessed that letter message shows, results were as expected.

       ![Guess Letter repeated Answer Image](/images/guess-invalid-repeat.png)


  7. When  user go to either Win Sreen or Lose Screen then the user is asked if they want to play again, Y for yes N for no.

       * First I tested what would happen if the user typed anything other than Y or N: Error message shows, results were as expected.

       ![Play again invalid input Image](/images/play-again-invalid.png)


       * Next I tested what would happen if the user typed Y: go the Difficulty Level Screen, results were as expected.

       * Last I tested what would happen if the user typed N: go the Welcome Screen, results were as expected.

  8. When the user go to the Quit Game Screen, user is asked that are they sure to quit, Y for yes and N for no.

       * First I tested what would happen if the user typed anything other than Y or N: Error message shows, results were as expected.

       ![Quit Screen invalid input Image](/images/quit-invalid.png)


       * Next I tested what would happen if the user typed Y: message displays, results were as expected.

       * Last I tested what would happen if the user typed N: go back to the Welcome Sreen, results were as expected.

  ### Bugs

   #### Resolved

   * At Username Screen when user typed its name with spaces before or after, then invalid error message is showing that is not letting the user to continue the game. To solve this issue I used strip method of the input to remove unnecessary whitespaces.

   #### Unresolved     
    
  The Hangman game is working perfectly fine on my gitpod workspace but after deployment I see an issue that when user guess the correct letter, it is not displaying the remaining blank spaces. As suggested by my mentor and tutor try to change the colour of blank spaces but issue remains the same. No issues are showing on my gitpod workspaces

  ![Game no issue Image](/images/hangman-no-issue.png)

  ![Game issue Image](/images/hangman-issue.png)

## Acknowledgements

The Hangman game was created as my third portfolio project. I would like to thank my mentor Marcel Mulders for his helpful feedback and encouragement throughout the development process. I would also like to thank tutor of code institute for their support. I'd like to thank fellow Code Institute students in May 2022 class at code institute.

Dania Khanam




