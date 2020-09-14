# Assignment 2 - Grocery App
#create customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_lists = [] #empty list to hold grocery list objects

#class to create grocery list objects
class GroceryList:
    def __init__(self, store, items):
        self.store = store
        self.items = items
    
    def __str__(self):
        return f"{self.store}"
#function to create user object when app starts
def create_user():
    user_name = input("Enter name of user: ")
    return Customer(user_name)

#print out app options for user
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
    
#call function to create user object before starting main loop
user = create_user()
#flag to run app until user chooses to quit
flag = True
while flag:
    app_options()
    #get user input for app choice
    user_choice = int(input("Enter number of option: "))
    #quit out of app
    if user_choice == 5:
        flag = False
    #create a new list
    elif user_choice == 1:
        #get name of store to create list for
        store_name = input("Enter name of store: ").title()
        items = []
        #will continue to ask for items to add to grocery list until user types 'stop'
        while True:
            item = input("Enter item to add to list or type 'stop' to end list: ")
            if item == 'stop':
                break
            else:
                #add input items to empty list 
                items.append(item)
        #create new GroceryList object with user input for name and items
        store_name = GroceryList(store_name, items)
        #add grocery list object to list of object in main user object
        user.shopping_lists.append(store_name)
        
    # add new items to selected grocery list
    elif user_choice == 2:
        #print out all current lists and ask for user choice to input new items
        print("CURRENT SHOPPING LISTS:")
        for i in range(len(user.shopping_lists)):
            print(f"{i+1}. {user.shopping_lists[i].store}")
        # user choice for list
        list_to_add = int(input("Enter number of list to add to: "))
        #conitnue adding new items to list until user chooses 'stop'
        while True:
            new_item = input("Enter item to add to list or enter 'stop' to end: ")
            if new_item == 'stop':
                break
            else:
                user.shopping_lists[list_to_add - 1].items.append(new_item)
    # Print out all current grocery lists and items for each store
    elif user_choice == 3:
        #loop through all lists and print out all info
        for i in range(len(user.shopping_lists)):
            print(f"STORE: {user.shopping_lists[i].store}\nITEMS: {user.shopping_lists[i].items}\n-------------------")

    #delete a created shopping list from user object
    elif user_choice == 4:
        #print out current lists to choose from
        print("CURRENT SHOPPING LISTS:")
        for i in range(len(user.shopping_lists)):
            print(f"{i+1}. {user.shopping_lists[i].store}")
        #takes user choice and removes that grocery list object from user object
        list_to_delete = int(input("Enter number of list to delete: "))
        print(f"DELETING LIST: {user.shopping_lists[i - 1].store}")
        user.shopping_lists.pop(i - 1)
