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

data = questions.get_all_values()

#print(data)

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
            name_user_here = ''

    print(f'Hey there {name_user_here} lets get started with the game!')

def display_questions():
    print('hello')
    
display_questions()

game_playing_text()

