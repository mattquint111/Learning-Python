# Is Prime

number = int(input("Enter a number: "))



def is_prime():
    # declare an empty solution variable to return
    soln = f"{number} IS PRIME"
    

    if number <= 1:
        soln = f"{number} IS NOT PRIME"
    else:
        for i in range(2, number):
            if number % i == 0:
                soln = f"{number} IS NOT PRIME"
                
    return soln

print(is_prime())






