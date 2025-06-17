#Task Manger Source Code

import os

#File to store tasks
FILE_NAME = "tasks.txt"

#Load tasks from file
def load_tasks():
    tasks = {}
    #check if file path exists
    if os.path.exists(FILE_NAME):
        #opening in read mode and then adding it to empty dictionary
        with open(FILE_NAME, "r") as f1:
            for line in f1:
                task_id, title, status = line.strip().split()
                tasks[int(task_id)] = {'title' : title, 'status' : status}
    return tasks


#save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f1:
        for task_id, task in tasks.item():
            f1.write(f"{task_id} | {task['title']} | {task['status']}")
            

#add a new task          
def add_task(tasks):
    title = input("Enter the title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title" : title, "status": "incomplete"}
    print(f"Task '{title}' was added")
    
    
#view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.item():
            print(f"[{task_id}] | {task['title']} - {task['status']}")
            
            
    
#Mark task as complete from incomplete
def mark_task_complete(tasks):
    task_id = int(input("Enter the Task Id to mark it as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task {tasks[task_id]["title"]} marked as complete")
    else:
        print("Task Id not found")
        
#Delete a task
def delete_a_task(tasks):
    task_id = int(input("Enter the Task Id to delete it: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Following task id has been deleted: {deleted_task}")
        # print(f"Task {tasks[task_id]["title"]} deleted sucessfully")
    else:
        print("Task Id not found")
        
        
#Main Menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\n Task Manager: ")
        print("1. Add Task\n")
        print("2. View Task\n")
        print("3. Mark Task Completed\n")
        print("4. Delete a Task\n")
        print("5. Exit")
        
        n = int(input("Dear user enter your choice: "))
        
        if n==1:
            add_task(tasks)
            
        elif n==2:
            view_tasks(tasks)
            
        elif n==3:
            mark_task_complete(tasks)
            
        elif n==4:
            delete_a_task(tasks)
            
        elif n==5:
            save_tasks(tasks)
            print("Goodbye")
            break
        
        else:
            print("Invalid Choice try again")
            
    
    if __name__ == "__main__":
        main()
        
