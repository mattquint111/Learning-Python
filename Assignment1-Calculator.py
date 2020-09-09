def calculator(first_number, operand, second_number):
    soln = None

    if operand == '+':
        soln = first_number + second_number
    elif operand == '-':
        soln = first_number - second_number
    elif operand == '*':
        soln = first_number * second_number
    elif operand == '/':
        soln = first_number / second_number
    
    return soln