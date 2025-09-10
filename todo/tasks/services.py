from .forms import TaskForm
from .models import Task


def create_task_from_form(form: TaskForm) -> Task:
    """Create and return a new Task instance from a validated form."""
    return form.save()


def update_task_from_form(form: TaskForm) -> Task:
    """Update and return an existing Task instance from a validated form."""
    return form.save()


def toggle_task_completion(task: Task) -> Task:
    """Toggle the 'completed' status of a Task and save it."""
    task.completed = not task.completed
    task.save()
    return task
