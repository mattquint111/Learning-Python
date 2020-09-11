# Find largest element in array

test_array = [-1, 0, 1, 2, 3, 4, 5, 100]

# Solution 1

def return_largest(list):
    largest_number = list[0]

    for number in list:
        if number > largest_number:
            largest_number = number
    
    return largest_number

print(return_largest(test_array))


# Solution 2

print(max(test_array))