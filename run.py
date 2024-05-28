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

def game_playing():
    print('######################################################################')
    print(f'           Hello and welcome to the Basic Knowledge Quiz!\n\nHere we gonna test some of your knowledge about some basic questions\n\n                 You think you may know the answers?\n\n                        Lets find out then!')
    print('######################################################################')
game_playing()

