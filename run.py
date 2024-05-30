import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file"
]

CREDENT = Credentials.from_service_account_file('quizcreds.json')
CREDS_SCOPE = CREDENT.with_scopes(SCOPE)
GOOGLESPREAD = gspread.authorize(CREDS_SCOPE)
SHEET_HERE = GOOGLESPREAD.open("basic_questions")

questions = SHEET_HERE.worksheet('questions')

score_number = 0
 
def game_playing_text():
    """ 
    This function contains the intro text to the quiz game.
    """
    print('######################################################################')
    print(f'           Hello and welcome to the Basic Knowledge Quiz!\n\nHere we gonna test some of your knowledge about some basic questions\n\n                 You think you may know the answers?\n\n                        Lets find out then!')
    print('######################################################################')
    input('                        Press Enter To Play!')
    player_name()
       
def player_name():
    """
    This function let the user fill in a input for a name to play the game. 
    """
    name_user_here = ''
    
    while name_user_here == '':
        name_user_here = input('Enter in your name to start the game:').strip().lower()
        if name_user_here.isnumeric():
            print('You have to enter a name')
            name_user_here = input('Enter in your name to start the game:').strip().lower()
            

    print(f'Hey there {name_user_here} lets get started with the game!\n')
    display_questions(name_user_here)

def display_questions(name_user_here):
    """
    this function loops and shows the questions and respond to the answers 
    that the player are choosing.
    """
    global score_number
    
    question_col = questions.col_values(1)
    answer_col = questions.col_values(2)
    
    for question, answer_here in zip(question_col, answer_col):
        while True:
            print(question,"\n")
            user_answers = input('Answer Here: ').strip().lower()
            if user_answers == answer_here.strip().lower():
                score_number += 1
                print(f"You got it Right {name_user_here}!")
                break
            else:
                print(f"Sorry {name_user_here} , its wrong try again!")
                score_number -= 1
                
    quiz_over()

def quiz_over():
    """
    Function keep the result of the quiz and prints the ending text.
    """
    global score_number 
    print('\n*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#')
    print('                          Game over!')
    print("           Your score result is:",score_number,"out of 10 questions!")
    print('*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#')
        
      
game_playing_text()

