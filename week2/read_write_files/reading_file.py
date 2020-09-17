# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# # with open('test_txt_file.txt', 'w') as f:
# #     f.write('this is test text in the file')

# with open('test_txt_file.txt') as f:
#     file_content = f.read()

# just create a new file
# my_file = open('new_file.txt', 'x')
# my_file.close()

# ACTIVITY 1: Ask user for input for their favorite dish and write name of dish to file

# with open('fav_dish.txt', 'w') as f:
#     favorite = input("Enter your favorite dish: ")
#     f.write(favorite)

# with open('fav_dish.txt', 'w') as f:
#     while True:
#         fav = input("Enter favorite dish (type 'q' to quit): ")
#         if fav == 'q':
#             break
#         else:
#             f.write(fav + '\n')

# ACTIVITY 2: 