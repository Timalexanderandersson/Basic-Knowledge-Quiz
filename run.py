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
    display_questions()

def display_questions():
    """

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
                print("You got it Right")
                break
            else:
                print("Sorry, its wrong try again!")


display_questions()
#game_playing_text()

