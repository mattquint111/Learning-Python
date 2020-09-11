# Assignment 1 - Factorial
#number = int(input("Enter a non-negative number: "))

# def factorial():
#     soln = 1

#     for i in range(1, number+1):
#         soln *= i
        
#     return soln

#print(factorial())

# Recursive factorial function 
def factorial2(n):
    # default solution for n == 0 (n! == 1)
    soln = 1
    
    if n == 0:
        return soln
    else:
        # call factorial2() until n-1 == 0
        soln = n * factorial2(n - 1)
    
    return soln  
# 3! == 6
print(factorial2(5))