# Remove Duplicates

# Solution 1:
names = ['Alex', 'John', 'Mary', 'Steve', 'John', 'Steve']

def remove_dupes(list):
    unique_list = []

    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Solution 2:
unique_names_set = set(names)
unique_list = list(unique_names_set)
print(sorted(unique_list))

