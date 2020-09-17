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
        tables_status()
    # user chooses 2. CHOOSE TABLE
    elif  user_choice == 2:
        # choose number of table to view
        table_choice = pick_table()
        #print out all data for specific table
        table_info(table_choice)
    # user chooses 3. CHECK-OUT TABLE
    elif user_choice == 3:
        table_choice = pick_table()
        check_out(table_choice)
    # user chooses 4. CHECK-In TABLE
    elif user_choice == 4:
        table_choice = pick_table()
        #check_in(table_choice)
        check_in(table_choice)