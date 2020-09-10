# Assignment 1 - Factorial
number = int(input("Enter a number: "))

def factorial():
    soln = 1

    for i in range(1, number+1):
        soln *= i

    return soln

print(factorial())
