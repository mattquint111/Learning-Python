# def calculator(first_number, operand, second_number):
#     soln = None

#     if operand == '+':
#         soln = first_number + second_number
#     elif operand == '-':
#         soln = first_number - second_number
#     elif operand == '*':
#         soln = first_number * second_number
#     elif operand == '/':
#         soln = first_number / second_number
    
#     return soln


input1 = int(input("Enter first number: "))
input2 = input("Enter an operand (+,-,*,/): ")
input3 = int(input("Enter second number: "))

def add():
    print(input1 + input3)

def subtract():
    print(input1 - input3)

def multiply():
    print(input1 * input3)

def divide():
    print(input1 / input3)

def calculator():
    if input2 == '+':
        return add()
    elif input2 == '-':
        return subtract()
    elif input2 == '*':
        return multiply()
    elif input2 == '/':
        return divide()
calculator()

