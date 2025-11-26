from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    """
    READ operation - Display all tasks.
    This view fetches all tasks from database and renders them in a template.
    """
    # Get all tasks from database (already ordered by -created_at from model Meta)
    tasks = Task.objects.all()
    
    # Render template with context data
    # 'tasks' variable will be available in the template
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    """
    CREATE operation - Add a new task.
    Handles both GET (show form) and POST (process form) requests.
    """
    if request.method == 'POST':
        # POST request - user submitted the form
        # Create form instance with submitted data
        form = TaskForm(request.POST)
        
        # Validate form data
        if form.is_valid():
            # Save the new task to database
            form.save()
            
            # Show success message to user
            messages.success(request, 'Task created successfully!')
            
            # Redirect to task list page
            # redirect() returns HttpResponseRedirect
            return redirect('task_list')
    else:
        # GET request - show empty form
        form = TaskForm()
    
    # Render form template
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


def task_update(request, pk):
    """
    UPDATE operation - Edit an existing task.
    pk (primary key) identifies which task to update.
    """
    # Get task by primary key, or return 404 if not found
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # POST request - user submitted the form
        # Create form instance with submitted data AND existing task instance
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            # Update the task in database
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        # GET request - show form pre-filled with existing task data
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form, 
        'action': 'Update',
        'task': task
    })


def task_delete(request, pk):
    """
    DELETE operation - Remove a task.
    Uses confirmation page to prevent accidental deletion.
    """
    # Get task to delete
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # User confirmed deletion
        task_title = task.title  # Store for message
        task.delete()  # Delete from database
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect('task_list')
    
    # GET request - show confirmation page
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def task_detail(request, pk):
    """
    READ operation - Display a single task's details.
    """
    # Get specific task
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
