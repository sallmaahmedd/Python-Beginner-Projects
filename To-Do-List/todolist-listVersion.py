#A to-do list program to add,update and remove tasks
#when choosing to quit, your list is saved to a text file
#brings in Python's built-in module for operating-system related things
import os

filename="tasks.txt"

""" Loading the existing tasks(if there's any) """
tasks=[]
if os.path.exists(filename):
    """ "r":opens the file in read mode, "with":automatically closes the file once the indented block finishes """
    with open(filename,"r") as file:
        """files are iterable, just like lists so looping over an open file gives you one line at a time """
        for line in file:
            """every line read from a file includes the invisible newline character (\n) at the end
            .strip() removes that and any stray whitespace """
            tasks.append(line.strip()) 



""" enumerate is for position tracking, it produces a sequence of pairs, one per item in the list. """
""" for index, task is for unpacking! instead of the loop variables
    (the variables between for and in, receiving new values for each iteration, so you can use them inside the loop body)
    receiving each whole pair as a tuple, it splits each pair into two separate named variables  """
def view():
    for index,task in enumerate(tasks, start=1):
        print(f"{index}.{task}")

            
while True:
    print("""Menu:
          1.View
          2.Add
          3.Update
          4.Remove
          5.Quit""")
    
    choice=input("Enter the operation you want to do: ").lower()


    if choice=="view" or choice=="1" or choice=="1.view":
        """ Empty list evaluates to False in boolean and non-empty is True """
        if not tasks:
            print("No Tasks Yet!")
        else:
            view()

    elif choice in ("add","2.add","2"):
        new_task=input("Enter your task: ")
        if new_task.strip() == "":
            print("Task cannot be empty")
        else:
            tasks.append(new_task)
            print(f"{new_task} is added as a new task!")

    elif choice in ("update","3.update","3"):
        if not tasks:
            print("Nothing to update!")
        else:
            view()
            task_to_update=int(input("Enter the number of the task you want to update: "))
            if 1<= task_to_update <=len(tasks):
                post_update_task=input("Enter the new task: ")
                """ since the list is indexed starting from 0 and we start from 1"""
                tasks[task_to_update-1]=post_update_task
                print(f"Task numbered: {task_to_update} is updated to {post_update_task}!")
            else:
                print("There's no task with that number!")

    elif choice in ("4","4.remove","remove"):
        if not tasks:
                    print("Nothing to remove!")
        else:
            view()
            task_to_remove=int(input("Enter the number of the task you want to remove: "))
            if 1<= task_to_remove <=len(tasks):
                """ .pop() removes the item at the index and returns the value that was removed """
                removed_task=tasks.pop(task_to_remove-1)
                print(f"Task: {removed_task} is removed!")
            else:
                print("There's no task with that number!")

    elif choice in ("5","5.quit","quit"):

        """ "w":means write, which creates the file if it doesn't exist or completely overwrites it if it does 
        so that the file always reflect the current list instead of adding to the old one """
        with open(filename,"w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Goodbye! Your To-Do list is saved!")
        break
    else:
        print("Invalid choice, try again!")
