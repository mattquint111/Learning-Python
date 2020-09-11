# Find smallest element in array

test_array = [-1, 0, 1, 2, 3, 4, 5, 100]

# Solution 1

def return_smallest(list):
    smallest_number = list[0]

    for number in list:
        if number < smallest_number:
            smallest_number = number
    
    return smallest_number

print(return_smallest(test_array))


# Solution 2

print(min(test_array))