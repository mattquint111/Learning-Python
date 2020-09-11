# Determine missing number in array

test_list = [0, 1, 2, 3, 4, 5, 6, 8, 9]

# Solution 1
def find_missing(list):

    for i in range(len(list)):
        if i not in list:
            return i

print(find_missing(test_list))


# Solution 2
print( sum(range(test_list[-1] + 1)) - sum(test_list))
