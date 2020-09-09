def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not a valid number, try again")
            continue
        else:
            return user_input
            break

number1 = input_number("Enter a number: ")
number2 = input_number("Enter a second number: ")
operator = input('Enter an operator (+,-,*,/,**,%): ')

def calculator():
    
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '%':
        return number1 % number2

print(calculator())