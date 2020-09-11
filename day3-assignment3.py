# Is Prime

number = int(input("Enter a number: "))

def is_prime():
    # If a number is not proved to not be prime then by default number == prime
    soln = f"{number} IS PRIME"
    
    # test to see if number is not prime
    if number <= 1:
        soln = f"{number} IS NOT PRIME"
    else:
        for i in range(2, number):
            if number % i == 0:
                soln = f"{number} IS NOT PRIME"         
    return soln

print(is_prime())






