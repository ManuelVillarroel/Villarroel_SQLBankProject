import mysql.connector

"""
connection = mysql.connector.connect(
    user = 'bankRegister',
    database = 'AccountTest',
    password = 'bankingTime'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM Bank_accounts")
cursor.execute(testQuery)

cursor.close()
cursor.connection()
"""

"""
testQuery = (f"SELECT ID FROM Bank_accounts WHERE name = \"{userName}\" and password = \"{password}\"")
    cursor.execute(testQuery)
    for item in cursor:
        userID = item
        break
    print(f"Your ID is \"{userID[0]}\"")
"""


connection = mysql.connector.connect(
    user = 'bankRegister',
    database = 'Account_Shema',
    password = 'bankingTime'
)

cursor = connection.cursor()

print("+----------------------------------------------+")
print("| Welcome to your own personal banking system. |")
print("|        Do you already have an account?       |")
print("|     or would you like to create a new one?   |")
print("+----------------------------------------------+\n")
print("1. Login")
print("2. Create an account")
print("3. exit")

print()

def Login():
    print("\n+------------------------------------------+")
    print("|                                          |")
    print("|                   Login                  |")
    print("|                                          |")
    print("+------------------------------------------+\n")
    print("1. [Insert ID]")
    print("2. Back\n")
    while(True):
        try:
            playerInput = input("please insert ID: ")
            testQuery = (f"SELECT ID, password FROM Bank_accounts")
            cursor.execute(testQuery)

            if playerInput.strip().upper().__contains__("BACK"):
                return 
            
            playerInputNumber = int(playerInput)
            accountexists = False
            accountInfo = tuple()

            for item in cursor:
                if playerInputNumber == int(item[0]):
                    accountexists = True
                    accountInfo = item
                    break

            print()
            if accountexists:
                while True:
                    checkPassword = input("Please enter Password: ")
                    if checkPassword == accountInfo[1]:
                        ManagingAccount(int(accountInfo[0]))
                        return
                    else:
                        print("INVALID PASSWORD TRY AGAIN")
            else:
                print(f"INVALID ID PLEASE TRY AGAIN")
        except ValueError:
                print(f"INVALID ID PLEASE TRY AGAIN")
    return
def CreateAccount():
    print("\n+---------------------------------------+")
    print("|                                       |")
    print("|   Welcome! We're glad to have you!    |")
    print("|                                       |")
    print("+---------------------------------------+\n")
    userName = input("Please provide a username: ")
    print()
    while True:
        password = input("Please provide a Password: ")
        confirm = input("Confirm Password: ")
        if password == confirm:
            break
        else:
            print(" !!Passwords don't match!!")
    print()
    while True:
        money = input("Please insert a starting deposit: ")
        try:
            money = float(money)
            break
        except ValueError:
            print(" !!Not a digit value!!")
    testQuery = (f"INSERT INTO Bank_accounts (password, name, Balance) VALUES (\"{password}\", \"{userName}\", {money});")
    cursor.execute(testQuery)
    print("\n!Account Created!")
    testQuery = (f"SELECT ID FROM Bank_accounts WHERE name = \"{userName}\" and password = \"{password}\"")
    cursor.execute(testQuery)
    for item in cursor:
        userID = item
        break
    print(f"Your ID is \"{userID[0]}\"")
    ManagingAccount(userID[0])
    return

def ManagingAccount(accountID):
    testQuery = (f"SELECT ID, name FROM Bank_accounts;")
    cursor.execute(testQuery)
    for item in cursor:
        if int(item[0]) == accountID:
            accountName = item[1]
            break
    print("\n+----------------------------------+")
    print("|                                  |")
    print(f"|     Welcome {accountName}!       |")
    print("|                                  |")
    print("+----------------------------------+\n")
    while True:
        try:
            print("1. Check Balance")
            print("2. Exit Account")
            userinput = input("What would you like to do: ")

            if userinput.strip().upper().__contains__("BALANCE"):
                CheckBalance(accountID)
            elif userinput.strip().upper().__contains__("EXIT"):
                return
            
            userinputnumber = int(userinput)

            if userinputnumber == 1:
                CheckBalance(accountID)
            elif userinputnumber == 2:
                return
            else:
                print(" !!Invalid, Not an option!!")
        except ValueError:
                print(" !!Invalid, Not an option!!")
    return

def CheckBalance(accountID):
    testQuery = (f"SELECT Balance FROM Bank_accounts WHERE ID = {accountID}")
    cursor.execute(testQuery)
    for item in cursor:
        balance = item[0]
        break
    print(f"\nYour balance is ${balance}!\n")
    return

while True:
    playerInput = input("Please input the number you would like to access: ")
    try:
        if playerInput.strip().upper().__contains__("LOGIN"):
            Login()
        elif playerInput.strip().upper().__contains__("CREATE"):
            CreateAccount()
        elif playerInput.strip().upper().__contains__("EXIT"):
            break

        playernumber = int(playerInput)
        
        if playernumber == 1:
            Login()
        elif playernumber == 2:
            CreateAccount()
        elif playernumber == 3:
            break
        else:
            print(f"[{playerInput.strip()}] is not a number or an option")

        print("\n+----------------------------------------------+")
        print("| Welcome to your own personal banking system. |")
        print("|        Do you already have an account?       |")
        print("|     or would you like to create a new one?   |")
        print("+----------------------------------------------+\n")
        print("1. Login")
        print("2. Create an account")
        print("3. Exit")
    except ValueError:
        print(f"[{playerInput.strip()}] is not a number or an option")
        print("\n+----------------------------------------------+")
        print("| Welcome to your own personal banking system. |")
        print("|        Do you already have an account?       |")
        print("|     or would you like to create a new one?   |")
        print("+----------------------------------------------+\n")
        print("1. Login")
        print("2. Create an account")
        print("3. Exit")


cursor.close()
connection.close()