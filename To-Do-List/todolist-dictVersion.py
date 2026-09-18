import os
import json

file_name="to-do-list.txt"
tasks={}
next_id = 1

"""This works, but it's a little fragile, because what if a task contains a comma and you only split once? 
   The task text "eggs, bread" would survive but there's a better way to do it"""

"""if os.path.exists(file_name,"r"):
    with open(file_name,"r")as file:
        for line in file:
        
                <splits a string into pieces wherever a comma appears,
                and the 1 means "only split on the first comma" 
                which is important, because if someone's task text contains a comma "Buy milk, eggs, bread", 
                you don't want it accidentally chopped into extra pieces.>

            id_str, task_text=line.strip().split(",",1)

            <everything read from a file is text, so the ID needs converting back to an integer>

            tasks[int(id_str)]=task_text
"""



""" Python has a built-in module, json, designed for saving structured data like dicts to a file and loading it back, 
    without you manually inventing a text format """

if os.path.exists(file_name):
    with open(file_name,"r")as file:
        tasks=json.load(file)

def view():
    if not tasks:
        print("No Tasks Yet!")
    else:
        """ tasks.items() gives (key, value) pairs directly, since a dict already has built-in identifiers (the keys)
            you don't need to manufacture a position number like what's done with lists."""
        for id,task in tasks.items():
                print(f"{id}.{task}")

while True:
    choice=input("Enter the operation you want to do: ").lower()

    if choice in ("view","1","1.view"):
        view()

    elif choice in ("add","2.add","2"):
            new_task=input("Enter your task: ")
            if new_task.strip() == "":
                print("Task cannot be empty")
            else:
                tasks[next_id]=new_task
                print(f"{new_task} is added as task {next_id}")
                next_id+=1

    elif choice in ("update","3.update","3"):
            if not tasks:
                print("Nothing to update!")
            else:
                view()
                task_id=int(input("Enter the ID of the task you want to update: "))
                if task_id in tasks:
                    post_update_task=input("Enter the new task: ")
                    tasks[task_id]=post_update_task
                    print(f"Task with ID: {task_id} is updated to {post_update_task}!")
                else:
                    print("There's no task with that ID!")

    elif choice in ("4","4.remove","remove"):
            if not tasks:
                        print("Nothing to remove!")
            else:
                view()
                task_id=int(input("Enter the ID of the task you want to remove: "))
                if task_id in tasks:
                    removed_task=tasks.pop(task_id)
                    print(f"Task: {removed_task} is removed!")
                else:
                    print("There's no task with that ID!")

    elif choice in ("5","5.quit","quit"):
        with open(file_name,"w") as file:
            json.dump(tasks, file)
            print("Goodbye! Your To-Do list is saved!")
            break
    else:
        print("Invalid choice, try again!")
