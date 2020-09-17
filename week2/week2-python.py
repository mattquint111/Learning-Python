# # CLasses & Objects

# # Create Class: table

# class Table:
    
#     def __init__(self, width, height, material):
#         self.width = width
#         self.height = height
#         self.material = material

# table1 = Table('100', '50', 'oak')
# table2 = Table('150', '65', 'steel')


# class BankAccount:

#     def __init__(self, account_num, routing_num, account_type, initial_balance):
#         self.account_num = account_num
#         self.routing_num = routing_num
#         self.type = account_type
#         self.initial_balance = initial_balance

#     def deposit(self, amount):
#         self.initial_balance += amount
#         print(f"Current balance: {self.initial_balance}")

#     def withdraw(self, amount):
#         self.initial_balance -= amount

#     def transfer(self, transfer_acc, transfer_amount):
#         transfer_acc.deposit(transfer_amount)
#         self.withdraw(transfer_amount)

# account_checking = BankAccount(12345, 54321, 'checking', 1_000)
# account_savings = BankAccount(45677, 67890, 'savings', 500)



# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.is_manager = False

# def upgrade_to_manager(emp):
#     emp.is_manager = True

# employee = Employee('John Doe')

#Exceptions

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
        
#     except ZeroDivisionError:
#         print('second number can not be zero')
#     else:
#         print(answer)

# def find_sum():
#     first_num = input("Enter a number: ")
#     second_num = input("Enter another number: ")
#     return int(first_num) + int(second_num)

# while True:
#     try:
#         soln = find_sum()
#     except ValueError:
#         print('You must enter two numbers')
#     else:
#         print(soln)

# with open('username.json', 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}")

# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}")

# greet_user()

# Inheritance 

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
    
#     def drive(self):
#         print('driving')

#     def fill_up(self):
#         print('filled up gas tank')
#         self.fuel_level = 100
#         print(f"fuel level is now {self.fuel_level}")
    
# class ElectricCar(Car):
#     def __init__(self, make, model, battery_size):
#         super().__init__(make,model)
#         self.battery_size = battery_size

# car = Car('Honda', 'S2000')
# print(car.make, car.model)

# tesla = ElectricCar('Tesla', 'Type-X', 100)
# print(tesla.make, tesla.model, tesla.battery_size)

# Exception Handling
# while True:
    
#     try:
#         first_number = int(input("Enter a number: "))
#         second_number = int(input("Enter a second number: "))
#         print(first_number / second_number)
#     except ValueError:
#         print("Enter a valid number")
#     except ZeroDivisionError:
#         print("Second number can't be zero")

# Reading from a file

# with open('emails.txt') as f:
#     email_list = f.read()

# email_list = email_list.split(', ')


# unique_email_list = []
# for email in email_list:
#     if email not in unique_email_list:
#         unique_email_list.append(email.strip())

# unique_emails_formatted = []
# for email in unique_email_list:
#     unique_emails_formatted.append(email.strip())

# duplicate_free_emails = ', '.join(unique_emails_formatted)

# with open('duplicate-free-email-list2.txt', 'w') as f:
#     f.write(duplicate_free_emails)

# JSON
# import json

# users = []

# while True:
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))

#     user = {"name": name, "age": age}
#     users.append(user)

#     with open("users.json", 'w') as file_object:
#         json.dump(users, file_object)

#     choice = input("Conitnue or 'q' to quit: ")
#     if choice == 'q':
#         break