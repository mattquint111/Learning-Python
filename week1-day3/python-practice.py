friends = ['Joe', 'John', 'Jason', 'Jeremy', 'Jill', 'Julia']

# Print array items 1
# for index in friends:
#     print(index)

# # Print array items 2
# for index in range(0, len(friends)):
#     print(friends[index])

# # Print array items 3
# for index in range(len(friends)):
#     print(friends[index])

# # Print in reverse
# for index in range(len(friends)-1, -1, -1):
#     print(friends[index])

names = []
# ask for name and print out
# name.append(input("Enter name: "))
# print(name[0])

# ask for name 5 times and print out that name
for i in range(5):
    names.append(input("Enter name: "))
print(names)