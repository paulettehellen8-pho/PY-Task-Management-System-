from datetime import datetime

def validate_task_title(title):
    if not title or not title.strip():
        return False, "Title cannot be empty."
    elif len(title) > 50:
        return False, "Title cannot exceed 50 characters."
    else:
        return True, ""
    
def validate_task_description(description):
    if not description or not description.strip():
        return False, "Description cannot be empty."
    elif len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    else:
        return True, ""   
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, ""
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")