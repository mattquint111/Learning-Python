# HARD Assignment : print out pyramid

# initial conditions
# pyramid_size = 9
# level = 1
# char_count = 1
# char = '*'
# space_count = 8
# space = ' '

# while level <= pyramid_size:
#     print( (space * space_count) + (char * char_count) )
#     level += 1
#     char_count += 2
#     space_count -= 1

# print pyramid of any size with any character
def print_pyramid(char, size):
    pyramid_size = size
    level = 1
    char_count = 1
    char = char
    space_count = size - 1
    space = ' '
    
    while level <= pyramid_size:
        print((space * space_count) + (char * char_count))
        level += 1
        char_count += 2
        space_count -= 1

def print_pyramid_inv(char, size):
    pyramid_size = size
    level = 1
    char_count = size * 2
    char = char
    space_count = 0
    space = ' '
    
    while level <= pyramid_size:
        print((space * space_count) + (char * char_count))
        level += 1
        char_count -= 2
        space_count += 1


def print_diamond(char, size):
    print_pyramid(char, size)
    print_pyramid_inv(char, size)

print_diamond('$',15)