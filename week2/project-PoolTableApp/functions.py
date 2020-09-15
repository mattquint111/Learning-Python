import datetime

#current date/time
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# function to find difference in date/times
def time_difference(start_time,end_time):
    start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M')
    ends = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M')
    diff = start - ends
    hours = int(diff.seconds // (60 * 60))
    mins = int((diff.seconds // 60) % 60)
    return f"HOURS = {hours}, MINS = {mins}"         

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
        self.start_time = ''
        self.end_time = ''
        self.time_played = ''
        self.last_user = ''
# empty list to hold table objects (1-12)     
tables = []
# function to create 12 table objects and append to tables array
def create_tables():
    for index in range(12):
        table = Table('Table ' + str(index+1))
        tables.append(table)

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
    NAME:------------------{table.name}
    STATUS:----------------{table.status}
    START DATE/TIME:-------{table.start_time}
    END DATE/TIME:---------{table.end_time}
    TOTAL TIME PLAYED:-----{table.time_played}
    LAST CHECKED OUT BY:---{table.last_user}
    """)

# check out a table and update information
def check_out(table_number, user):
    table = tables[table_number - 1]
    if table.status == "UNOCCUPIED":
        table.status = 'OCCUPIED'
        table.last_user = user
        table.start_time = dt
        print(f"{table.name} has been checked out at {table.start_time} by: {table.last_user}")
    else:
        print(f"{table.name} is already checked out, please choose another table")

#check in a table and update information
def check_in(table_number):
    table = tables[table_number - 1]
    if table.status == "OCCUPIED":
        table.status = "UNOCCUPIED"
        table.end_time = dt
        table.time_played = time_difference(table.start_time, table.end_time)
        print(f"{table.name} has been checked in by: {table.last_user}\n TOTAL PLAY TIME = {table.time_played}")
    else:
        print(f"{table.name} is not currently checked out, please choose a checked out table to check in.")

##############TESTING##############


    

