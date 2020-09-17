# Activity: Writing JSON File
import json

users = []

while True:
    name = input("Enter your name (or enter 'q' to quit): ")
    if name == 'q':
        break
    age = int(input("Enter your age: "))
    
    user = {"name": name, "age": age}
    users.append(user)

    with open("user_data.json", 'w') as write_file:
        json.dump(users, write_file)

with open('user_data.json') as f:
    user_data = json.load(f)

print(user_data)
