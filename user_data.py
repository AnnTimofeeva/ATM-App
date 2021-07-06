# create an empty list of users
import os
from datetime import date


#***********************************************************************************************************************
def clearscreen():
    os.system('cls')

#*************************************************************************************************************************
# create some example users (USERID:     PIN:    BALANCE:    OVERDRAFT:)
def load_user_data():
    return [
        {"USERID":1234,"PIN": 1100,"Balance": 670.00, "Overdraft":"No"},
        {"USERID":5678,"PIN": 3322,"Balance": 2494.00, "Overdraft":"Yes"},
        {"USERID":9012,"PIN": 5544,"Balance": 1039.00, "Overdraft":"No"},
        {"USERID":3456,"PIN": 7766,"Balance": 28.00, "Overdraft":"No"},
        {"USERID":7890,"PIN": 9988,"Balance": 14968.00, "Overdraft":"No"},
    ]
#*********************************************************************************************************************************
# create transactions history dictionary
def load_transactions():
    return[
        {"Date":"2021-05-11","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":760.00,"BALANCE_AFTER":720.00},
        {"Date":"2021-05-14","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":100.00,"BALANCE_BEFORE":720.00,"BALANCE_AFTER":620.00},
        {"Date":"2021-05-14","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":60.00,"BALANCE_BEFORE":1814.00,"BALANCE_AFTER":1754.00},
        {"Date":"2021-05-16","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":80.00,"BALANCE_BEFORE":620.00,"BALANCE_AFTER":540.00},
        {"Date":"2021-05-16","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":40.00,"BALANCE_BEFORE":318.00,"BALANCE_AFTER":278.00},
        {"Date":"2021-05-16","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":50.00,"BALANCE_BEFORE":1754.00,"BALANCE_AFTER":1704.00},
        {"Date":"2021-05-17","USERID": 5678,"TRANSACTION": "Lodgement", "AMOUNT":850.00,"BALANCE_BEFORE":1704.00,"BALANCE_AFTER":2554.00},
        {"Date":"2021-05-17","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":60.00,"BALANCE_BEFORE":12058.00,"BALANCE_AFTER":11998.00},
        {"Date":"2021-05-18","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":50.00,"BALANCE_BEFORE":540.00,"BALANCE_AFTER":490.00},
        {"Date":"2021-05-18","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":50.00,"BALANCE_BEFORE":2554.00,"BALANCE_AFTER":2504.00},
        {"Date":"2021-05-18","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":40.00,"BALANCE_BEFORE":1199.00,"BALANCE_AFTER":1159.00},
        {"Date":"2021-05-19","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":50.00,"BALANCE_BEFORE":11998.00,"BALANCE_AFTER":11948.00},
        {"Date":"2021-05-20","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":850.00,"BALANCE_BEFORE":11948.00,"BALANCE_AFTER":12798.00},
        {"Date":"2021-05-21","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":750.00,"BALANCE_BEFORE":12798.00,"BALANCE_AFTER":13548.00},
        {"Date":"2022-05-22","USERID": 1234,"TRANSACTION": "Lodgement", "AMOUNT":300.00,"BALANCE_BEFORE":490.00,"BALANCE_AFTER":790.00},
        {"Date":"2021-05-22","USERID": 3456,"TRANSACTION": "Lodgement", "AMOUNT":400.00,"BALANCE_BEFORE":278.00,"BALANCE_AFTER":678.00},
        {"Date":"2021-05-23","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":2504.00,"BALANCE_AFTER":2434.00},
        {"Date":"2021-05-23","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":13548.00,"BALANCE_AFTER":13478.00},
        {"Date":"2021-05-23","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":100,"BALANCE_BEFORE":1159.00,"BALANCE_AFTER":1059.00},
        {"Date":"2021-05-25","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":678.00,"BALANCE_AFTER":628.00},
        {"Date":"2021-05-26","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":790.00,"BALANCE_AFTER":730.00},
        {"Date":"2021-05-28","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":2434.00,"BALANCE_AFTER":2374.00},
        {"Date":"2021-05-28","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":13478.00,"BALANCE_AFTER":13418.00},
        {"Date":"2021-05-28","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":1059.00,"BALANCE_AFTER":1009.00},
        {"Date":"2021-05-30","USERID": 1234,"TRANSACTION": "PIN Change", "AMOUNT":0,"BALANCE_BEFORE":730.00,"BALANCE_AFTER":730.00},
        {"Date":"2021-06-01","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":2374.00,"BALANCE_AFTER":2324.00},
        {"Date":"2021-06-01","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":1009.00,"BALANCE_AFTER":959.00},
        {"Date":"2021-06-02","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":628.00,"BALANCE_AFTER":578.00},
        {"Date":"2021-06-03","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":80,"BALANCE_BEFORE":730.00,"BALANCE_AFTER":650.00},
        {"Date":"2021-06-03","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":200,"BALANCE_BEFORE":2324.00,"BALANCE_AFTER":2124.00},
        {"Date":"2021-06-03","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":959.00,"BALANCE_AFTER":919.00},
        {"Date":"2021-06-04","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":500,"BALANCE_BEFORE":13418.00,"BALANCE_AFTER":13918.00},
        {"Date":"2021-06-05","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":578.00,"BALANCE_AFTER":538.00},
        {"Date":"2021-06-05","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":200,"BALANCE_BEFORE":13918.00,"BALANCE_AFTER":13718.00},
        {"Date":"2021-06-08","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":650.00,"BALANCE_AFTER":600.00},
        {"Date":"2021-06-09","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":600.00,"BALANCE_AFTER":550.00},
        {"Date":"2021-06-09","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":13718.00,"BALANCE_AFTER":13668.00},
        {"Date":"2021-06-10","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":80,"BALANCE_BEFORE":498.00,"BALANCE_AFTER":418.00},
        {"Date":"2021-06-11","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":2124.00,"BALANCE_AFTER":2074.00}, 
        {"Date":"2021-06-11","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":80,"BALANCE_BEFORE":919.00,"BALANCE_AFTER":839.00},
        {"Date":"2021-06-12","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":418.00,"BALANCE_AFTER":358.00}, 
        {"Date":"2021-06-12","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":50,"BALANCE_BEFORE":2074.00,"BALANCE_AFTER":2024.00},  
        {"Date":"2021-06-12","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":1040,"BALANCE_BEFORE":13668.00,"BALANCE_AFTER":14698.00}, 
        {"Date":"2021-06-12","USERID": 9012,"TRANSACTION": "Lodgement", "AMOUNT":150,"BALANCE_BEFORE":839.00,"BALANCE_AFTER":989.00}, 
        {"Date":"2021-06-13","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":2024.00,"BALANCE_AFTER":1954.00},
        {"Date":"2021-06-13","USERID": 9012,"TRANSACTION": "Lodgement", "AMOUNT":270,"BALANCE_BEFORE":989.00,"BALANCE_AFTER":1259.00},
        {"Date":"2021-06-14","USERID": 1234,"TRANSACTION": "Lodgement", "AMOUNT":470,"BALANCE_BEFORE":550.00,"BALANCE_AFTER":1020.00}, 
        {"Date":"2021-06-14","USERID": 3456,"TRANSACTION": "Lodgement", "AMOUNT":50,"BALANCE_BEFORE":358.00,"BALANCE_AFTER":308.00}, 
        {"Date":"2021-06-14","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":14698.00,"BALANCE_AFTER":14628.00}, 
        {"Date":"2021-06-15","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":100,"BALANCE_BEFORE":1020.00,"BALANCE_AFTER":920.00}, 
        {"Date":"2021-06-15","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":308.00,"BALANCE_AFTER":268.00}, 
        {"Date":"2021-06-15","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":1954.00,"BALANCE_AFTER":1914.00}, 
        {"Date":"2021-06-15","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":14628.00,"BALANCE_AFTER":14588.00},
        {"Date":"2021-06-15","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":1259.00,"BALANCE_AFTER":1219.00},  
        {"Date":"2021-06-17","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":90,"BALANCE_BEFORE":920.00,"BALANCE_AFTER":830.00},  
        {"Date":"2021-06-18","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":1914.00,"BALANCE_AFTER":1874.00},
        {"Date":"2021-06-18","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":40,"BALANCE_BEFORE":14588.00,"BALANCE_AFTER":14548.00}, 
        {"Date":"2021-06-18","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":1219.00,"BALANCE_AFTER":1149.00},
        {"Date":"2021-06-20","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":70,"BALANCE_BEFORE":268.00,"BALANCE_AFTER":198.00},
        {"Date":"2021-06-21","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":20,"BALANCE_BEFORE":830.00,"BALANCE_AFTER":810.00},
        {"Date":"2021-06-21","USERID": 7890,"TRANSACTION": "Withdrawal", "AMOUNT":100,"BALANCE_BEFORE":14548.00,"BALANCE_AFTER":14448.00},
        {"Date":"2021-06-22","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":80,"BALANCE_BEFORE":810.00,"BALANCE_AFTER":730.00},  
        {"Date":"2021-06-22","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":100,"BALANCE_BEFORE":1874.00,"BALANCE_AFTER":1774.00}, 
        {"Date":"2021-06-22","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":100,"BALANCE_BEFORE":1149.00,"BALANCE_AFTER":1049.00}, 
        {"Date":"2021-06-24","USERID": 1234,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":730.00,"BALANCE_AFTER":670.00}, 
        {"Date":"2021-06-24","USERID": 3456,"TRANSACTION": "PIN Change", "AMOUNT":0,"BALANCE_BEFORE":198.00,"BALANCE_AFTER":198.00}, 
        {"Date":"2021-06-24","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":460,"BALANCE_BEFORE":14448.00,"BALANCE_AFTER":14908.00},
        {"Date":"2021-06-25","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":80,"BALANCE_BEFORE":198.00,"BALANCE_AFTER":118.00},  
        {"Date":"2021-06-25","USERID": 5678,"TRANSACTION": "Lodgement", "AMOUNT":780,"BALANCE_BEFORE":1774.00,"BALANCE_AFTER":2554.00},
        {"Date":"2021-06-25","USERID": 7890,"TRANSACTION": "Lodgement", "AMOUNT":60,"BALANCE_BEFORE":14908.00,"BALANCE_AFTER":14968.00}, 
        {"Date":"2021-06-25","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":180,"BALANCE_BEFORE":1049.00,"BALANCE_AFTER":1229.00},  
        {"Date":"2021-06-26","USERID": 3456,"TRANSACTION": "Withdrawal", "AMOUNT":90,"BALANCE_BEFORE":118.00,"BALANCE_AFTER":28.00}, 
        {"Date":"2021-06-28","USERID": 5678,"TRANSACTION": "Withdrawal", "AMOUNT":60,"BALANCE_BEFORE":2554.00,"BALANCE_AFTER":2494.00}, 
        {"Date":"2021-06-28","USERID": 9012,"TRANSACTION": "Withdrawal", "AMOUNT":190,"BALANCE_BEFORE":1229.00,"BALANCE_AFTER":1039.00}, 
    ]
#***************************************************************************************
#display updated users info (PIN, balance)     
def update_info(subject_to_be_updated):
    print(f"Your {subject_to_be_updated} has been updated, press return to continue")
    input()  

#******************************************************************************************
#updates user balance after lodgement and add transaction to the transaction history list
def lodge_money(user,sum,transactions):
    user ['Balance']+=sum
    update_info("balance")
    transactions.append({"Date": date.today(), "USERID": user['USERID'], "TRANSACTION": "Lodgement", "AMOUNT":sum, "BALANCE_BEFORE":user['Balance']-sum, "BALANCE_AFTER": user['Balance']}) 

#******************************************************************************************** 
#updates user balance after withdrawal and add transaction to the transaction history list
#checks overdraft availability if insufficient amount of money
def withdraw_money(user,sum,transactions):
    currentbalance=user ['Balance']
    newbalance=currentbalance-sum
    if newbalance<0 and user["Overdraft"]=="No" :
        print("Insufficient amount of money on your account. Withdrawal is cancelled")
        print("Press return to continue")
        input()   
        return
    else:    
        user ['Balance']-=sum        
        transactions.append({"Date": date.today(), "USERID": user['USERID'], "TRANSACTION": "Withdrawal", "AMOUNT":sum, "BALANCE_BEFORE":user['Balance']+sum, "BALANCE_AFTER": user['Balance']}) 
        update_info("balance")

#*************************************************************************************
#updates user PIN and add transaction to the transaction history list
def update_pin(user,new_pin,transactions):
    user['PIN']=new_pin 
    update_info("PIN")  
    transactions.append({"Date": date.today(), "USERID": user['USERID'], "TRANSACTION": "PIN Change", "AMOUNT":0, "BALANCE_BEFORE":user['Balance'], "BALANCE_AFTER": user['Balance']}) 

#*************************************************************************************
#prints brief blank statement form
def print_bank_statement(customer):
    clearscreen()
    print("=========================================== \n")
    print("Bank statement")
    print("=========================================== \n")
    print(f"Customer ID = {customer['USERID']}")
    print(f"Customer balance = {customer['Balance']}")
    print(f"Customer overdraft availability= {customer['Overdraft']}")
    print("=========================================== \n")
    

#*************************************************************************************
#prints detailed blank statement form
def print_n_last_transactions(n, user,transactions):
    count=0
    n_last_transactions=[]
    print("===========Last 10 transactions=============== \n")
    print(f"DATE".ljust(15),  "TRANSACTION".ljust(14), "AMOUNT (€)".ljust(15), "BALANCE (€)" )
    print(f"====".ljust(15),  "===========".ljust(14), "==========".ljust(15), "===========")
    print(f"{user['Balance']}".rjust(52))
    for line in reversed(transactions):
        if(line["USERID"] == user['USERID']):
            count+=1
            if count>n:
                break 
            else:
                n_last_transactions.append(line)
            
    for entry in reversed(n_last_transactions):
        result=entry['AMOUNT']
        if (entry['AMOUNT']==0):
            result="-"

        print(f"{str(entry['Date']).ljust(15)}  {str(entry['TRANSACTION']).ljust(15)}{str(result).ljust(15)}{str(entry['BALANCE_AFTER'])}")
                

