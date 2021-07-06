from user_data import load_user_data 
from user_data import load_transactions 
from user_menu import login_menu
# Main program
# load all nesessary user data and transactions history from user_data.py and pass them to login menu to
#deal with login procedure and user menu functionality
userdata = load_user_data()
transactions = load_transactions()

login_menu(userdata,transactions)


