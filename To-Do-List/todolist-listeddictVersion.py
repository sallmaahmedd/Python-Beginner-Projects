
import os
import json

fileName="ToDoList.txt"
tasks=[]

if os.path.exists(fileName):
    with open(fileName, "r") as file:
        tasks = json.load(file)

def view():
    if not tasks:
        print("No Tasks Yet!")
    else:
        for index, task_dict in enumerate(tasks, start=1):
            status = "Done" if task_dict["done"] else "Not done"
            print(f"{index}. {task_dict['task']} - {status}")

while True:
    print("""Menu:
          1.View
          2.Add
          3.Update
          4.Remove
          5.Done
          6.Quit""")
    
    choice=input("Enter the operation you want to do: ").lower()

    if choice in ("view","1","1.view"):
        view()

    elif choice in ("add", "2.add", "2"):
        new_task = input("Enter your task: ")
        if new_task.strip() == "":
            print("Task cannot be empty")
        else:
            """ appending a dict literal:{"task": new_task, "done": False}.
                Every new task automatically starts as not-done """
            tasks.append({"task": new_task, "done": False})
            print(f"{new_task} added as a new task!")

    elif choice in ("update", "3.update", "3"):
        if not tasks:
            print("Nothing to update!")
        else:
            view()
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_text = input("Enter the new task text: ")
                """ ["task"] reaches into that dict and updates just the "task" field, leaving "done" untouched
                    so you're now updating one field of a structured record and not replacing the whole thing """
                tasks[task_number - 1]["task"] = new_text
                print(f"Task {task_number} updated to: {new_text}")
            else:
                print("No task with that number")

    elif choice in ("remove", "4.remove", "4"):
        if not tasks:
            print("Nothing to remove!")
        else:
            view()
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                """ removed_task is now a dict so I want to show its text only and not the whole {"task", "done": ...} """
                print(f"Removed: {removed_task["task"]}")
            else:
                print("No task with that number")

    elif choice in ("done", "5.done", "5"):
        if not tasks:
            print("No tasks to mark!")
        else:
            view()
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                print(f"Task {task_number} marked as done!")
            else:
                print("No task with that number")

    elif choice in ("6","6.quit","quit"):
            with open(fileName,"w") as file:
                json.dump(tasks, file)
                print("Goodbye! Your To-Do list is saved!")
                break
    else:
            print("Invalid choice, try again!")
    