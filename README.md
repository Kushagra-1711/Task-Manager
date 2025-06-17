# 📝 Task Manager (Console-based)

A simple command-line Task Manager built using Python. It allows users to **add**, **view**, **complete**, and **delete** tasks. Tasks are stored persistently in a local text file.

---

## 🚀 Features

- ✅ Add new tasks
- 👀 View all tasks
- ✔️ Mark tasks as complete
- ❌ Delete tasks
- 💾 Save tasks to a file (`tasks.txt`)

---

## 🛠 How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the script as `task_manager.py`.
3. Open terminal or command prompt in the project folder.
4. Run the script using:

```bash```
python task_manager.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Menu on Running


--- Task Manager ---
1. Add Task
2. View Task
3. Mark Task Completed
4. Delete a Task
5. Exit
Enter your choice:

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

How to Use (Examples)
▶️ Add a Task

Enter your choice: 1
Enter the title: Buy groceries
Task 'Buy groceries' was added.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

👀 View Tasks

Enter your choice: 2
[1] | Buy groceries - incomplete
[2] | Submit assignment - complete

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✔️ Mark a Task as Complete

Enter your choice: 3
Enter the Task Id to mark it as complete: 1
Task 'Buy groceries' marked as complete.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

❌ Delete a Task

Enter your choice: 4
Enter the Task Id to delete it: 2
Task 'Submit assignment' deleted successfully.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🗃 File Structure
bash

project-folder/
│
├── task_manager.py       # Main Python script
├── tasks.txt             # File storing all tasks (auto-created)
└── README.md             # Project description

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
