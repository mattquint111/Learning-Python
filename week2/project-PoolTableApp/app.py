from functions import *
#create array of 12 table objects with default status = UNOCCUPIED
create_tables()
# flag to run table app until user quits
active = True
while active == True:
    welcome_msg()
    user_choice = int(input("Enter number of option: "))
    # user chooses 5. QUIT
    if user_choice == 5:
        active = False
    # user chooses 1. VIEW ALL TABLES
    elif  user_choice == 1:
        for table in tables:
            print(f"NAME: {table.name} - STATUS: {table.status}")
    # user chooses 2. CHOOSE TABLE
    elif  user_choice == 2:
        table_choice = int(input("Enter number of table to choose: "))
        #print out all data for specific table