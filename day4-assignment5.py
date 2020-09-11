# Duplicates array

test_array = [1,2,3,4,5]

# Solution 1
def duplicate_array(list):
    soln = list

    for i in list:
        soln.append(i)
    
    return soln

# Solution 2
double_array = test_array + test_array
print(double_array)
