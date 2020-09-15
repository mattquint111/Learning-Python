from datetime import datetime

start_time = datetime.now()
input("Wait...")
end_time = datetime.now()

# is of type timedelta = end_time - start_time
time_played = end_time - start_time
print(time_played)

pool_tables = []

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = 
        self.start_time = None
        self.end_time = None
        self.time_played = None

    def check_out(self):
        self.is_occupied = True
        self.start_time = datetime.now()

    def check_in(self):
        # time difference in minutes
        self.time_played = (self.end_time - self.start_time) / 3_600
        self.is_occupied = False
#create 12 pool tables
for index in range(1,13):
    #initialize a pool table object
    table = PoolTable(index)
    pool_tables.append(table)

# ask for user input for table to play on
user_input = int(input("Enter pool table number: "))
pool_table = pool_tables[user_input - 1]
pool_table.check_out()