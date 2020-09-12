# TO DO List Using Dictionaries

# flag to signal if program should keep running or quit
active = True
# create empty list that will hold to-do items
tasks = []
# program wrapped in while loop to keep running until user quits
while active:
    # message giving the user list of choices to pick from
    menu_message = "\nTO-DO List app, please select an option from the following choices:\n"
    menu_message += "\nPress 1 to add task"
    menu_message += "\nPress 2 to delete task"
    menu_message += "\nPress 3 to view all tasks"
    menu_message += "\nPress q to quit\n"
    print(menu_message)
    # ask user for command choice
    user_choice = input("Enter choice: ")
    # code to run if user chooses 1 - add task
    if user_choice == '1':
        # get user input for task title and priority level
        task_title = input("Enter task name: ")
        task_priority = input("Enter task priority level (high/medium/low): ")
        #create task dictionary using user input and add to tasks array
        task = {'title' : task_title, 'priority': task_priority}
        task_copy = task.copy()
        tasks.append(task_copy)
        print(f"\nTASK: {task_title} / PRIORITY: {task_priority} added to task list")
        
    # code to run if user chooses 2 - delete task
    elif user_choice == '2':
        # get title of task to delete from user
        task_to_del = input("Enter name of task to delete: ")
        # go through all task dictionaries and delete task with chosen title
        for item in tasks:
            if item['title'] == task_to_del:
                tasks.remove(item)
                print(f"TASK: {task_to_del}, removed from TO-DO list")
    
    # code to run if user chooses 3 - view all tasks
    elif user_choice == '3':
        print("CURRENT TASKS:")
        # loop through all task dicts and print out title and priority
        for item in tasks:
            print(f"\n TASK NAME = {item['title']}, PRIORITY LEVEL = {item['priority']}")

    # code to run if user chooses q - quit app
    elif user_choice == 'q':
        print('GOODBYE')   
        active = False