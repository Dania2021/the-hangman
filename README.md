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
* Features
  * [Welcome Screen](#welcome-screen)
  * [Username Screen](#username-screen)
   * [Difficulty Level Screen](#difficulty-level-screen)
   * [Guessing Screen](#guessing-screen)
     * [Correct Answer Message](#correct-answer-message)
     * [Incorrect Answer Message](#incorrect-answer-message)
     * Invalid Guess
     * Display of Hangman
     * [Win Screen](#win-screen)
     * [Lose Screen](#lose-screen)
  * Rules Screen
  * High Scores Screen
  * Quit Game Screen
  * Extra Features
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

    * #### Win Screen

        If the user guesses all letter correctly it will take them to a screen that congratulates them and will ask the User to input a "Y" for Yes or "N" for No to either play again or exit the game, either options will store their username along with their score to a googlesheet document.

        ![Win Screen Image](/images/win-msg-img.png)

    * #### Lose Screen

        The lose screen is displayed when the user has finally used up all of their lives and lets them know that they have lost the game. When this screen shows, it displays the last stage of the hangman (a stick figure being 'hung'). It also greets the user to an unfortunate message letting the user know that user run out of lives, it also display what the word was and a encouraging text to persuade the User to play again. This screen also display username with the score.

         ![Lose Screen Image](/images/losing-msg-img.png)
        
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

     
     

