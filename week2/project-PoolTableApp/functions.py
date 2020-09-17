import datetime     

# App Function Module
def welcome_msg():
    print("""
    -------------------------------------
    ***** POOL TABLE MANAGEMENT APP *****
    1. VIEW ALL TABLES STATUS
    2. VIEW TABLE INFO
    3. CHECK-OUT TABLE
    4. CHECK-IN TABLE
    5. QUIT
    -------------------------------------
    """)

# create class: Table for each table object in list tables
class Table:
    def __init__(self, name):
        self.name = name
        self.status = 'UNOCCUPIED'
        self.date_start = ''
        self.start_time = ''
        self.end_time = ''
        self.start_counter = ''
        self.end_counter = ''
        self.price_start = ''
        self.price_end = ''
        self.price_counter = ''
        self.time_played = ''
        self.last_user = ''
# empty list to hold table objects (1-12)     
tables = []
# function to create 12 table objects and append to tables array
def create_tables():
    for index in range(12):
        table = Table('Table ' + str(index+1))
        tables.append(table)

def calc_cost(price_counter):
    if price_counter == 0:
        total = 30
    else:
        total = 30 + (30 * price_counter)
    
    return total

# print the status of all tables
def tables_status():
    for table in tables:
        print(f"NAME: {table.name} - STATUS: {table.status}")

# table choice function to pick number of particular table
def pick_table():
    return int(input("Enter number of table to choose: "))
#choose a particular table and see all information
def table_info(table_choice):
    table = tables[table_choice - 1]
    print(f"""
    NAME:------------------ {table.name}
    STATUS:---------------- {table.status}
    START TIME:------------ {table.start_time}
    END TIME:-------------- {table.end_time}
    TOTAL TIME PLAYED:----- {table.time_played}
    LAST CHECKED OUT BY:--- {table.last_user}
    """)

# check out a table and update information
def check_out(table_number, user):
    table = tables[table_number - 1]
    if table.status == "UNOCCUPIED":
        table.status = 'OCCUPIED'
        table.last_user = user
        table.date_start = datetime.datetime.now().strftime("%Y/%m/%d")
        table.start_counter = datetime.datetime.now()
        table.price_start = int(datetime.datetime.now().strftime("%H"))
        table.start_time = datetime.datetime.now().strftime("%H:%M")
        table.date_start = datetime.datetime.now().strftime("%Y/%m/%d")
        print(f"{table.name} has been checked out at {table.start_time} by: {table.last_user}")
        
    else:
        print(f"{table.name} is already checked out, please choose another table")

#check in a table and update information
def check_in(table_number):
    table = tables[table_number - 1]
    if table.status == "OCCUPIED":
        table.status = "UNOCCUPIED"
        table.end_counter = datetime.datetime.now()
        table.price_end = int(datetime.datetime.now().strftime("%H"))
        table.end_time = datetime.datetime.now().strftime("%H:%M")
        table.time_played = table.end_counter- table.start_counter
        table.price_counter = table.price_end - table.price_start
        print(f"{table.name} has been checked in by: {table.last_user}\nTOTAL PLAY TIME = {table.time_played}")
        total_price = calc_cost(table.price_counter)
        print(f"TOTAL PRICE = ${total_price}")
        # write table data to txt file when table is checked back in
        with open('table_data.txt', 'a') as f:
            f.write(f"DATE:{table.date_start}, NAME:{table.name}, USER:{table.last_user}, START_TIME:{table.start_time}, END_TIME:{table.end_time}, TOTAL_TIME_PLAYED:{table.time_played}, TOTAL_COST:{total_price}\n")

    else:
        print(f"{table.name} is not currently checked out, please choose a checked out table to check in.")

# function to calculate price for table with $30/hr



    

