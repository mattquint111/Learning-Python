# Assignment 2 - Grocery App
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_lists = []


class GroceryList:
    def __init__(self, store, items):
        self.store = store
        self.items = items
    
    def __str__(self):
        return f"{self.store}"

def create_user():
    user_name = input("Enter name of user: ")
    return Customer(user_name)


def app_options():
    print("""
    ***** GROCERY APP *****
    --------------------------
    1. Create shopping list
    2. Add item to shopping list
    3. Display shopping lists
    4. Delete shopping list
    5. Quit
    --------------------------    
    """)
    

user = create_user()

flag = True
while flag:
    app_options()
    user_choice = int(input("Enter number of option: "))

    if user_choice == 5:
        flag = False
    
    elif user_choice == 1:
        store_name = input("Enter name of store: ").title()
        items = []
        
        while True:
            item = input("Enter item to add to list or type 'stop' to end list: ")
            if item == 'stop':
                break
            else:
                items.append(item)
        store_name = GroceryList(store_name, items)
        user.shopping_lists.append(store_name)
        print(user.shopping_lists[0])
    
    elif user_choice == 2:
        print("CURRENT SHOPPING LISTS:")
        for i in range(len(user.shopping_lists)):
            print(f"{i+1}. {user.shopping_lists[i].store}")

        list_to_add = int(input("Enter number of list to add to: "))
        
        while True:
            new_item = input("Enter item to add to list or enter 'stop' to end: ")
            if new_item == 'stop':
                break
            else:
                user.shopping_lists[list_to_add - 1].items.append(new_item)
    
    elif user_choice == 3:
        #print out all shopping lists
        for i in range(len(user.shopping_lists)):
            print(f"STORE: {user.shopping_lists[i].store}\nITEMS: {user.shopping_lists[i].items}\n-------------------")


    elif user_choice == 4:
        print("CURRENT SHOPPING LISTS:")
        for i in range(len(user.shopping_lists)):
            print(f"{i+1}. {user.shopping_lists[i].store}")
        
        list_to_delete = int(input("Enter number of list to delete: "))
        print(f"DELETING LIST: {user.shopping_lists[i - 1].store}")
        user.shopping_lists.pop(i - 1)