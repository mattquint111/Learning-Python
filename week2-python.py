# CLasses & Objects

# Create Class: table

class Table:
    
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

table1 = Table('100', '50', 'oak')
table2 = Table('150', '65', 'steel')


class BankAccount:

    def __init__(self, account_num, routing_num, account_type, initial_balance):
        self.account_num = account_num
        self.routing_num = routing_num
        self.type = account_type
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount
        print(f"Current balance: {self.initial_balance}")

    def withdraw(self, amount):
        self.initial_balance -= amount

    def transfer(self, transfer_acc, transfer_amount):
        transfer_acc.deposit(transfer_amount)
        self.withdraw(transfer_amount)

account_checking = BankAccount(12345, 54321, 'checking', 1_000)
account_savings = BankAccount(45677, 67890, 'savings', 500)



class Employee:
    def __init__(self, name):
        self.name = name
        self.is_manager = False

def upgrade_to_manager(emp):
    emp.is_manager = True

employee = Employee('John Doe')

print(employee.name)
print(employee.is_manager)
upgrade_to_manager(employee)
print(employee.is_manager)