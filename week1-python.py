# Python: dictionaries & modules

# Activity - Creating a Dictionary
#
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")

# my_dict = {}
# my_dict['f_name'] = first_name
# my_dict['l_name'] = last_name
# my_dict['message'] = f"My name is {my_dict['l_name']}, {my_dict['f_name']}"

# print(my_dict['message'])
# print(my_dict)

# Activity - Nested Dictionaries
#

nested_dict = {
    'first_name' : 'Matt',
    'last_name' : 'Quint',
    'addresses' : [],
}    

address1 = {
    'street' : '11 W 53rd St',
    'state' : 'NY',
    'city' : 'New York City',
    'zip_code' : '10019',
}
nested_dict['addresses'].append(address1)

address2 = {
    'street' : '1000 5th Ave',
    'state' : 'NY',
    'city' : 'New York City',
    'zip_code' : '10028',
} 
nested_dict['addresses'].append(address2)

print(nested_dict)
# Activity = Multi Nested Dictionary Based on JSON Structure
#
my_json = []
