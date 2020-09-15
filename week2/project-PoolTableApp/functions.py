# App Function Module
def welcome_msg():
    print("""
    -------------------------------------
    ***** POOL TABLE MANAGEMENT APP *****
    1. VIEW ALL TABLES
    2. CHOOSE TABLE
    3. ASSIGN TABLE
    4. CLOSE OUT TABLE
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
        
tables = []

def create_tables():
    for index in range(12):
        table = Table('Table ' + str(index+1))
        tables.append(table)

table_1 = Table('Table 1')
