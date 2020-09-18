# Algorithms
# 1. perfect squares
def perfect_squares(a, b):
    numbers = list(range(a, b+1))
    return [num ** 2 for num in numbers]

# print(perfect_squares(1, 10))

# 2. 'a' to the power 'b'
def power_of(a, b):
    return a ** b

# print(power_of(3,4))

# 3. Calculate vowels in sentence
def calc_vowels(sentence):
    sentence = sentence.lower()
    vowels = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for char in sentence:
        if char in vowels:
            vowels[char] += 1
    return vowels

# print(calc_vowels('The elephant is walking in the enclosure!'))

# 4. Fibonacci numbers
def calc_fib(n):
    soln = 0
    if n == 0:
        soln += 0
    elif n == 1:
        soln += 1
    else:
        soln += calc_fib(n-1) + calc_fib(n-2)
    return soln

def print_fib_list(n):
    fib_list = []
    for i in range(n+1):
        fib_list.append(calc_fib(i))
    return fib_list

# print(print_fib_list(12))

# 5. QUESTION
def theSum(n):
    multiples = []
    soln_sum = 0
    for i in range(n):
        if i % 7 == 0 or i % 11 == 0:
            multiples.append(i)
    
    for i in multiples:
        soln_sum += i
    print(multiples)
    return soln_sum

print(theSum(1000))