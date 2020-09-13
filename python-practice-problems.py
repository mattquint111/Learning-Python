# Beginner Python Exercises
from datetime import datetime
from random import randint

# 1. character input

def when_turn_100(name, age):
    current_year = datetime.today().year
    year_100 = current_year + 100 - age
    print(f"Hello {name.title()}, you will turn 100 in the year {year_100} ")

#when_turn_100('matt', 33)

# 2.  odd or even
def odd_or_even():
    number = int(input("Enter a number: "))
     
    if number % 2 == 0:
        if number % 4 == 0:
            print(f"{number}: is even and divisible by 4")
        else:
            print(f"{number}: is even")
    else:
        print(f"{number}: is odd")
#odd_or_even()

# 3. list less than ten
def lst_less_than_10(lst):
    soln = []
    for number in lst:
        if number < 10:
            soln.append(number)
    
    return soln

# 4. divisors
def divisors(num):
    soln = []
    for i in range(1, num):
        if num % i == 0:
            soln.append(i)
    
    return soln

# 5. list overlap
def list_overlap(lst1, lst2):
    soln_list = []

    for i in lst1:
        if i in lst2 and i not in soln_list:
            soln_list.append(i)
    
    return sorted(soln_list)

def random_list(rand_range, list_size):
    random_lst = []
    for i in range(list_size):
        n = randint(1, rand_range)
        random_lst.append(n)
    
    return random_lst

# 6. string list

