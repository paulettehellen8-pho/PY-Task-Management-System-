from datetime import datetime

# Import validation functions
from task_manager.validation import(
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # valid, error = validate_task_title(title)
    # if not valid:
    #     print(f"Error: {error}")
    #     return

    # valid, error = validate_task_description(description)
    # if not valid:
    #     print(f"Error: {error}")
    #     return

    # valid, error = validate_due_date(due_date)
    # if not valid:
    #     print(f"Error: {error}")
    #     return

    validations = [
        (validate_task_title, title),
        (validate_task_description, description),
        (validate_due_date, due_date)
    ]

    for validate_func, value in validations:
        valid, error = validate_func(value)
        if not valid:
            print(f"Error: {error}")
            return

    print("No error")

    task={
        "title":title,
        "description":description,
        "due_date":due_date,
        "completed": False
    }
    tasks.append(task)
    #print(f"Task '{title}' added successfully!")
    print("Task added successfully")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"]=True
        #print(f"Task '{tasks[index]['title']}' marked as complete!")
        print("Task marked as complete")
    else:
        print("Invalid task index.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending=[(i,t) for i, t in enumerate(tasks) if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    for i, task in pending:
        print("Pending task no error")
        print(f"{i+1}. {task['title']} - due {task['due_date']}: {task['description']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed= len([t for t in tasks if t["completed"]])
    progress = (completed/len(tasks))*100
    return progress