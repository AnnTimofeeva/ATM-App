import os
import user_data 

def clearscreen():
    os.system('cls')

#*************************************************************************************
#validates user input (numeric value)
def validate_user_input(user_input):
    isnumeric = user_input.isnumeric()
    status = isnumeric
    if status==False:
         print("Sorry, invalid input. Please enter your data in digital format")
         print("Press return to continue...")
         input()
    return status


#******************************************************************************************
#validates PIN input when user logs in or tries to change PIN
def validate_pin_input(pin_input):
    is_numeric = pin_input.isnumeric()
    pin_length=len(pin_input)
    status = (is_numeric) and (pin_length==4)
    if status==False:
         print("Sorry, invalid PIN. Please enter correct amount in digital format (4 digits)")
         print("Press return to continue...")
         input()
    return status


#********************************************************************************
#keeps asking user to input valid menu option from 1-5
def user_menu(user,transactions):

    selection = "0"

    while(selection != "5"):
        clearscreen()
        selection = show_user_menu(user,transactions)

        if(selection not in ["1", "2", "3", "4", "5"]):
            clearscreen()
            print(f"Invalid menu option [{selection}]. Press return to try again.")
            input()


#**************************************************************************************         
# What user can do in this App:
# Change their PIN number
# Withdraw money from their account
# Lodge money into their account
# View a statement showing:
#      - The customer's USERID
#      - Their current balance
#      - Whether or not the user is registered for an overdraft facility
#      - [Optional] The user's last 10 transactions 
#                   (PIN Change/Withdrawal/Lodgement)
# User main menu system
def show_user_menu(user,transactions):

    print(f"Welcome user {user['USERID']}!")
    print(f"Your current balance is = {user['Balance']}\n")
    print("Menu options:")
    print("1. Change your PIN")
    print("2. Withdraw money from your account")
    print("3. Lodge money into your account")
    print("4. View a bank statement")        
    print("5. Exit\n")

    selection = input("Please choose an option (1-5): ")

    if(selection == "1"):
        #clearscreen()
        print("Change your PIN")
        print("=================\n")        
        print(f"Current PIN = {user['PIN']}")
        new_pin= input("New PIN: ")
        if validate_pin_input(new_pin):
            user_data.update_pin(user,int(new_pin),transactions)
    elif(selection == "2"):
        print("Withdraw money from your account\n")
        sum_withdraw= input("Enter the amount to withdraw from your account: ")
        if (validate_user_input(sum_withdraw)):
            user_data.withdraw_money(user,int(sum_withdraw),transactions)
    elif(selection == "3"):
        print("Lodge money into your account\n")
        sum_lodge= input("Enter the amount to lodge into your account: ")
        if (validate_user_input(sum_lodge)):
            user_data.lodge_money(user,int(sum_lodge),transactions)
    elif(selection == "4"):
        print("View a bank statement\n")
        user_data.print_bank_statement(user)
        user_data.print_n_last_transactions(10,user,transactions)
        print("Press return to continue...")
        input()

    return selection

#*********************************************************************************************
# Login menu method  - checks user login credentials and directs to the user menu if they are valid   

def login(userdata,transactions):
    print("User login\n")
    user_id_input = input("Enter your USER ID: ")
    if (validate_user_input(user_id_input)):
        user_id=int(user_id_input)

        pin_input = input("Enter your PIN: ")
        if (validate_pin_input(pin_input)):
            pin = int(pin_input)
            logged_in_user = None
            for user in userdata:
                if(user["USERID"] == user_id):
                
                    if(user["PIN"] == pin):
                        logged_in_user = user
                        break

            if(logged_in_user is not None):
                user_menu(logged_in_user,transactions)
            else:
                print("Invalid username or password. Press return to continue...")
                input()
     
#**************************************************************************************************
# prompts user to the first menu (login or exit)
def show_login_menu(userdata,transactions):
    print("Welcome to Banking ATM app. If you experience any issues, please contact us by phone 087-335-0000")
    print("Choose your menu options:")
    print("1. Login (You will need your 4 digits USER ID and your PIN number")
    print("2. Exit\n")

    selection = input("Please choose an option (1-2): ")

    if(selection == "1"):
        login(userdata,transactions)

    return selection

#********************************************************************************************************
# keeps showing login menu to the user until valid option is chosen    

def login_menu(userdata,transactions):

    selection = "0"

    while(selection != "2"):
        clearscreen()
        selection = show_login_menu(userdata,transactions)

        # if invalid menu option selected
        if(selection not in ["1", "2"]):
            clearscreen()
            print(f"Invalid menu option [{selection}]. Press return to try again.")
            input()

    print("Thank you for using Banking ATM App. Goodbye!")