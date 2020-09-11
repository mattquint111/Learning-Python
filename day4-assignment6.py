# HARD Assignment : print out pyramid

# initial conditions
pyramin_size = 9
level = 1
char_count = 1
char = '*'
space_count = 8
space = ' '

while level <= pyramin_size:
    print( (space * space_count) + (char * char_count))
    level += 1
    char_count += 2
    space_count -= 1