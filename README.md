# Django CRUD Task Manager - Complete Tutorial

A comprehensive step-by-step guide to building a full-stack CRUD (Create, Read, Update, Delete) application using Django framework. This tutorial covers all Django basics from scratch, perfect for beginners.

## Quick Start (For Cloning This Repo)

```powershell
# 1. Clone the repository
git clone https://github.com/NoelPOS/django-task-manager.git
cd django-task-manager

# 2. Create virtual environment (Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)
python -m venv myenv

# 3. Activate virtual environment
.\myenv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (optional)
python manage.py createsuperuser

# 7. Run server
python manage.py runserver

# 8. Open http://127.0.0.1:8000/ in your browser
```

## Table of Contents
1. [Prerequisites & Setup](#prerequisites--setup)
2. [Understanding the Project Structure](#understanding-the-project-structure)
3. [Step-by-Step Build Instructions](#step-by-step-build-instructions)
4. [Django Concepts Explained](#django-concepts-explained)
5. [Testing the Application](#testing-the-application)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites & Setup

### 1. Install Visual Studio Code
- Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Install on your system

### 2. Install Python
- Download Python 3.8+ from [https://www.python.org/downloads/](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**
- Verify installation: Open terminal and run `python --version`

### 3. Install VS Code Extensions (Recommended)
Open VS Code and install these extensions:
- **Python** (by Microsoft) - Python language support
- **Pylance** (by Microsoft) - Fast Python language server
- **Django** (by Baptiste Darthenay) - Django template syntax highlighting
- **SQLite Viewer** (by Florian Klampfer) - View SQLite databases

To install extensions:
1. Click Extensions icon in VS Code sidebar (or press `Ctrl+Shift+X`)
2. Search for extension name
3. Click "Install"

---

## Understanding the Project Structure

After completing this tutorial, your project will look like this:

```
Django-starter/
│
├── myenv/                          # Virtual environment (isolated Python packages)
│
├── myproject/                      # Django project (main configuration)
│   ├── __init__.py                # Makes this a Python package
│   ├── settings.py                # Project settings (database, apps, etc.)
│   ├── urls.py                    # Main URL routing configuration
│   ├── wsgi.py                    # Web server gateway interface
│   └── asgi.py                    # Asynchronous server gateway interface
│
├── tasks/                          # Django app (specific functionality)
│   ├── migrations/                # Database migration files
│   │   └── 0001_initial.py       # First migration (creates Task table)
│   ├── templates/                 # HTML templates for this app
│   │   └── tasks/
│   │       ├── base.html         # Base template (inherited by others)
│   │       ├── task_list.html    # Display all tasks
│   │       ├── task_form.html    # Create/Update form
│   │       ├── task_detail.html  # Single task view
│   │       └── task_confirm_delete.html  # Delete confirmation
│   ├── __init__.py               # Makes this a Python package
│   ├── admin.py                  # Admin panel configuration
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Database models (Task model)
│   ├── forms.py                  # Form definitions (TaskForm)
│   ├── views.py                  # View functions (business logic)
│   ├── urls.py                   # App-specific URL patterns
│   └── tests.py                  # Unit tests (optional)
│
├── db.sqlite3                     # SQLite database file
├── manage.py                      # Django command-line utility
└── README.md                      # This file
```

---

## Step-by-Step Build Instructions

### Step 1: Create Project Directory
```powershell
# Create a new folder for your project
mkdir Django-starter
cd Django-starter
```

**Why?** Organizing your project in a dedicated folder keeps everything clean and manageable.

---

### Step 2: Create Virtual Environment
```powershell
# Create virtual environment named 'myenv'
python -m venv myenv
```

**Why Virtual Environment?**
- Isolates project dependencies from global Python installation
- Different projects can use different package versions
- Makes project portable and reproducible
- Prevents version conflicts

---

### Step 3: Activate Virtual Environment
```powershell
# Windows PowerShell
.\myenv\Scripts\Activate.ps1

# Windows Command Prompt (cmd)
myenv\Scripts\activate.bat
```

**You should see** `(myenv)` prefix in your terminal, indicating the environment is active.

**Why Activate?** All packages you install will only be available in this environment, not globally.

---

### Step 4: Install Django
```powershell
pip install django
```

**What This Does:**
- Downloads Django framework and its dependencies
- Installs them in your virtual environment
- Makes Django commands available

**Verify Installation:**
```powershell
python -m django --version
```

---

### Step 5: Create Django Project
```powershell
django-admin startproject myproject .
```

**Why the dot (.) at the end?**
- Creates project in current directory
- Without dot: creates extra nested folder
- With dot: cleaner structure

**What This Creates:**
- `myproject/` - Main configuration folder
- `manage.py` - Command-line utility for Django tasks

**Important Files Created:**
- `settings.py` - All project settings (database, apps, middleware)
- `urls.py` - URL routing (maps URLs to views)
- `wsgi.py` & `asgi.py` - Deployment configuration

---

### Step 6: Create Django App
```powershell
python manage.py startapp tasks
```

**Project vs App - What's the Difference?**
- **Project**: Entire website with all configuration
- **App**: Specific functionality (e.g., blog, shop, tasks)
- One project can have multiple apps
- Apps can be reused in different projects

**What This Creates:**
- `tasks/` folder with basic app structure
- `models.py` - Define database tables
- `views.py` - Handle requests and responses
- `admin.py` - Admin panel configuration
- `tests.py` - Write tests for your app

---

### Step 7: Register App in Settings
Open `myproject/settings.py` and add `'tasks'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Our custom app
]
```

**Why Register?**
- Django needs to know about your app
- Without registration, models won't work
- Templates won't be found
- URLs won't be recognized

---

### Step 8: Create Database Model
Open `tasks/models.py` and define the Task model:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

**Field Types Explained:**
- `CharField` - Short text (requires max_length)
- `TextField` - Long text (no length limit)
- `BooleanField` - True/False values
- `DateTimeField` - Date and time
  - `auto_now_add=True` - Set once when created
  - `auto_now=True` - Update every time object is saved

**Meta Class:**
- `ordering` - Default sort order (- means descending)

**__str__ Method:**
- Defines how object appears in admin and shell
- Returns human-readable representation

---

### Step 9: Create and Apply Migrations
```powershell
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

**What Are Migrations?**
- Version control for your database schema
- Tracks changes to models
- Can be applied/reversed
- Makes database changes safe and reversible

**makemigrations:**
- Reads your models
- Creates Python files describing changes
- Stored in `migrations/` folder

**migrate:**
- Executes migration files
- Creates/modifies database tables
- Applies changes in correct order

---

## 🎯 CHECKPOINT 1: Database Created!

**What You've Accomplished So Far:**
- ✅ Created Django project and app
- ✅ Registered app in settings
- ✅ Defined Task model
- ✅ Created and applied migrations
- ✅ **Database is now ready!**

**Test It Now:**

1. **Check that database file was created:**
   Look in your project folder - you should see a file named `db.sqlite3`
   - File size: Around 130+ KB
   - This is your SQLite database containing the Task table

2. **Verify migrations were applied:**
   ```powershell
   python manage.py showmigrations
   ```
   **Expected output:**
   ```
   tasks
    [X] 0001_initial
   ```
   The `[X]` means the migration was successfully applied!

3. **Test database access using Django shell:**
   ```powershell
   python manage.py shell
   ```
   Then type these commands in the shell:
   ```python
   from tasks.models import Task
   
   # Create a test task
   task = Task.objects.create(
       title="Test Task",
       description="Testing database connection"
   )
   
   # Verify it was saved
   print(f"Created task #{task.id}: {task.title}")
   
   # Count tasks in database
   count = Task.objects.count()
   print(f"Total tasks: {count}")
   
   # Exit shell
   exit()
   ```
   
   **Expected output:**
   ```
   Created task #1: Test Task
   Total tasks: 1
   ```

**What You CAN'T Do Yet:**
- ❌ View tasks in a browser (no URLs or templates yet)
- ❌ Create tasks via web interface (no forms hooked up yet)
- ❌ See task list on a webpage (templates coming in Step 13)

**What's Next:**
In Steps 10-13, you'll build the web interface (forms, views, URLs, templates) to interact with this database through your browser!

---

### Step 10: Create Forms
Create `tasks/forms.py`:

```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
```

**What Are Forms?**
- Handle user input
- Validate data automatically
- Generate HTML form fields
- Clean and sanitize data

**ModelForm:**
- Automatically creates form from model
- Fields match model fields
- Validation rules from model
- Saves directly to database

**Widgets:**
- Control HTML rendering
- Add CSS classes
- Customize appearance
- Add HTML attributes

---

### Step 11: Create Views
Edit `tasks/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def task_list(request):
    """Display all tasks"""
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    """Create new task"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    """Update existing task"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    """Delete task"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_detail(request, pk):
    """View single task"""
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
```

**View Function Components:**
- `request` - Contains all request data (GET/POST, user, etc.)
- `render()` - Combines template with data, returns HTML
- `redirect()` - Sends user to different URL
- `get_object_or_404()` - Gets object or shows 404 page

**Request Methods:**
- `GET` - Fetch data (show form, display page)
- `POST` - Submit data (create, update, delete)

---

## 🎯 CHECKPOINT 2: Backend Logic Complete!

**What You've Built So Far:**
- ✅ Database with Task model
- ✅ Forms for data validation
- ✅ View functions (business logic)
- ✅ **All Python code is ready!**

**What's Still Missing:**
- ❌ URL routing (Django doesn't know which URLs call which views)
- ❌ HTML templates (no web pages to display)
- ❌ Can't test in browser yet

**Quick Code Review:**

At this point, your project structure should look like this:

```
Django-starter/
├── db.sqlite3              ✅ Database created
├── manage.py               ✅ Django command tool
├── myproject/
│   ├── settings.py         ✅ tasks app registered
│   └── urls.py             ⏳ Will update in Step 12
└── tasks/
    ├── models.py           ✅ Task model defined
    ├── forms.py            ✅ TaskForm created
    ├── views.py            ✅ 5 view functions ready
    ├── urls.py             ❌ Doesn't exist yet (Step 12)
    └── templates/          ❌ Doesn't exist yet (Step 13)
```

**Verify Your Views File:**
Open `tasks/views.py` and make sure you have all 5 functions:
1. ✅ `task_list(request)` - Show all tasks
2. ✅ `task_create(request)` - Create new task
3. ✅ `task_update(request, pk)` - Update existing task
4. ✅ `task_delete(request, pk)` - Delete task
5. ✅ `task_detail(request, pk)` - View one task

**What Happens If You Start the Server Now:**
```powershell
python manage.py runserver
```
Then visit `http://127.0.0.1:8000/`

**You'll see:** "Page not found (404)" error

**Why?** Because:
1. No URLs are configured yet (Step 12)
2. No templates exist yet (Step 13)
3. Django doesn't know what to show!

**This is NORMAL!** You're building from the inside out:
- ✅ Database layer (models) - Done
- ✅ Business logic (views) - Done
- ⏳ **Routing (URLs) - Next in Step 12**
- ⏳ **Presentation (templates) - After that in Step 13**

**What's Next:**
Step 12 will connect URLs to your view functions, and Step 13 will create the beautiful web pages!

---

### Step 12: Configure URL Routing

URL routing is how Django maps web addresses (URLs) to view functions. We'll create two URL configuration files: one for our `tasks` app and one to connect everything in the main project.

#### 12a. Create `tasks/urls.py` (App-Level URLs)

**What You'll Do:**  
Create a new file called `urls.py` inside the `tasks` folder to define all the URL patterns for task-related pages.

**Steps:**
1. Navigate to the `tasks` folder in VS Code
2. Right-click on the `tasks` folder → **New File** → name it `urls.py`
3. Copy and paste the following code into `tasks/urls.py`:

```python
from django.urls import path
from . import views

"""
URL patterns for the tasks app.
Each path() connects a URL to a view function.
"""

urlpatterns = [
    # List all tasks - Homepage
    # When user visits: http://127.0.0.1:8000/
    # Django calls: views.task_list function
    path('', views.task_list, name='task_list'),
    
    # Create new task
    # When user visits: http://127.0.0.1:8000/create/
    # Django calls: views.task_create function
    path('create/', views.task_create, name='task_create'),
    
    # View single task details
    # When user visits: http://127.0.0.1:8000/task/5/
    # Django captures "5" as pk (primary key) and calls: views.task_detail(request, pk=5)
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    
    # Update existing task
    # When user visits: http://127.0.0.1:8000/task/5/update/
    # Django captures "5" and calls: views.task_update(request, pk=5)
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    
    # Delete task
    # When user visits: http://127.0.0.1:8000/task/5/delete/
    # Django captures "5" and calls: views.task_delete(request, pk=5)
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

**Understanding the Code:**

- **`from django.urls import path`** - Imports the `path()` function used to define URL patterns
- **`from . import views`** - Imports view functions from `views.py` in the same folder (the `.` means current directory)
- **`urlpatterns = [...]`** - List of URL patterns Django will check in order
- **`path('url-string', view_function, name='url-name')`** - Basic syntax:
  - **First argument** (`'url-string'`) - The URL pattern to match
  - **Second argument** (`view_function`) - The function to call when URL matches
  - **Third argument** (`name='url-name'`) - A unique name to reference this URL in templates
- **`<int:pk>`** - URL parameter that:
  - Captures an integer from the URL
  - Stores it in a variable named `pk` (primary key)
  - Passes it to the view function as a parameter
  - Example: `/task/5/` → `pk=5`, `/task/123/` → `pk=123`

**Why We Use Named URLs:**  
Instead of hardcoding URLs like `/task/5/update/`, we can use `{% url 'task_update' 5 %}` in templates. This makes code maintainable—if you change the URL pattern later, all links automatically update!

**Save the file** (`Ctrl+S` or `Cmd+S`)

---

#### 12b. Update `myproject/urls.py` (Project-Level URLs)

**What You'll Do:**  
Modify the main project's URL configuration to include all the URLs from your `tasks` app.

**Steps:**
1. Open `myproject/urls.py` in VS Code
2. **Replace the entire file content** with the following code:

```python
"""
URL configuration for myproject project.

This is the main URL router for the entire Django project.
It routes requests to the appropriate app-level URL configurations.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin interface
    # Access at: http://127.0.0.1:8000/admin/
    # This provides a built-in interface to manage your database
    path('admin/', admin.site.urls),
    
    # Include all URLs from tasks app
    # The empty string '' means tasks URLs will be at the root level
    # Example: http://127.0.0.1:8000/ (not http://127.0.0.1:8000/tasks/)
    # 
    # Alternative: path('tasks/', include('tasks.urls'))
    # Would make URLs like: http://127.0.0.1:8000/tasks/create/
    path('', include('tasks.urls')),
]
```

**Understanding the Code:**

- **`from django.urls import path, include`** - Imports both `path()` and `include()` functions
- **`include('tasks.urls')`** - Includes all URL patterns from `tasks/urls.py`
  - This keeps code modular and organized
  - Each app manages its own URLs
  - Makes apps reusable in other projects
- **`path('admin/', admin.site.urls)`** - Built-in Django admin interface
- **Empty string in `path('', include(...))`** - Makes task URLs available at root level
  - Task list: `http://127.0.0.1:8000/` (not `/tasks/`)
  - Create task: `http://127.0.0.1:8000/create/` (not `/tasks/create/`)

**Why Two URL Files?**
```
myproject/urls.py (Main Router)
    ├── /admin/          → Django admin
    └── /                → include('tasks.urls')
                              ├── /                    → task_list
                              ├── /create/            → task_create
                              ├── /task/5/            → task_detail
                              ├── /task/5/update/     → task_update
                              └── /task/5/delete/     → task_delete
```

This structure:
- **Keeps projects organized** - Each app manages its own routes
- **Makes apps reusable** - You can use the tasks app in another project
- **Avoids conflicts** - Different apps can have same URL names (namespaced)

**Save the file** (`Ctrl+S` or `Cmd+S`)

---

#### 12c. Verify URL Configuration

**What to Expect:**  
At this point, your URLs are configured but won't work yet because we haven't created the template files. However, we can verify that Django recognizes the URL patterns.

**Test It:**
1. Make sure your development server is running:
   ```powershell
   python manage.py runserver
   ```

2. You should see output like:
   ```
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).
   November 28, 2025 - 00:04:26
   Django version 5.2, using settings 'myproject.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

3. Open your browser and try visiting `http://127.0.0.1:8000/`

4. **Expected Result:**  
   You'll see an error like:
   ```
   TemplateDoesNotExist at /
   tasks/task_list.html
   ```
   
   **This is GOOD!** It means:
   - ✅ Django found the URL pattern (matched `''` to `task_list`)
   - ✅ Django called the `task_list` view function
   - ✅ The view function tried to render `tasks/task_list.html`
   - ❌ The template doesn't exist yet (we'll create it in Step 13)

5. Try other URLs to verify URL routing works:
   - `http://127.0.0.1:8000/create/` → Should show error for `task_form.html`
   - `http://127.0.0.1:8000/task/1/` → Should show error for `task_detail.html`
   - `http://127.0.0.1:8000/admin/` → Should show Django admin login page (this works!)

**Common Errors:**

| Error | Meaning | Solution |
|-------|---------|----------|
| `Page not found (404)` | Django can't find matching URL | Check that you saved both URL files |
| `ModuleNotFoundError: No module named 'tasks.urls'` | Django can't import tasks.urls | Make sure `tasks/urls.py` exists |
| `ImportError: cannot import name 'views'` | Can't import views | Verify `tasks/views.py` exists from Step 11 |
| `AttributeError: module 'tasks.views' has no attribute 'task_list'` | View function doesn't exist | Make sure you completed Step 11 (Create Views) |

---

**What's Next?**  
In Step 13, we'll create the HTML templates that Django is looking for. These templates will display your tasks and forms in a beautiful, user-friendly interface.

---

### Step 13: Create HTML Templates

Templates are HTML files that Django uses to generate web pages. We'll create 5 templates that work together to display your task manager application.

#### 13a. Create Folder Structure

**What You'll Do:**  
Create a nested folder structure where Django will look for your template files.

**Steps:**
1. Navigate to the `tasks` folder in VS Code
2. Create a new folder named `templates` inside `tasks`
3. Inside the `templates` folder, create another folder named `tasks`

**Final Structure:**
```
tasks/
├── templates/
│   └── tasks/          ← All HTML files go here
│       ├── base.html
│       ├── task_list.html
│       ├── task_form.html
│       ├── task_detail.html
│       └── task_confirm_delete.html
```

**Why Nested `tasks/templates/tasks/`?**
- Django searches ALL `templates/` folders in ALL installed apps
- Nesting prevents name conflicts between different apps
- When you reference templates in code, use `'tasks/base.html'` not just `'base.html'`
- Example: If you had a `blog` app, it could have `blog/templates/blog/base.html` without conflicting

---

#### 13b. Create Base Template (`base.html`)

**What This Does:**  
The base template contains common elements (navigation bar, footer, styling) that all other templates will inherit. This promotes DRY (Don't Repeat Yourself) principle.

**Steps:**
1. Inside `tasks/templates/tasks/` folder, create a new file named `base.html`
2. Copy and paste the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Task Manager{% endblock %}</title>
    
    <!-- Bootstrap CSS for styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar-brand {
            font-weight: bold;
        }
        .main-content {
            margin-top: 20px;
            margin-bottom: 40px;
        }
    </style>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'task_list' %}">📝 Task Manager</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_list' %}">All Tasks</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_create' %}">Create Task</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/admin/">Admin Panel</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Messages (for success/error notifications) -->
    <div class="container mt-3">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}
    </div>

    <!-- Main Content Area - child templates will fill this -->
    <div class="container main-content">
        {% block content %}
        {% endblock %}
    </div>

    <!-- Footer -->
    <footer class="bg-light text-center text-muted py-3 mt-auto">
        <div class="container">
            <p class="mb-0">Django CRUD Task Manager © 2025</p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Understanding the Code:**

- **`{% block title %}...{% endblock %}`** - Defines a replaceable section that child templates can override
- **`{% url 'task_list' %}`** - Django template tag that generates URL based on the name we defined in `urls.py`
  - Benefit: If you change URL pattern later, links update automatically
  - Much better than hardcoding `/` or `/create/`
- **`{% if messages %}`** - Displays success/error messages from views
  - Remember in `views.py` we used `messages.success(request, 'Task created!')`
  - This is where those messages appear
- **`{% for message in messages %}`** - Loops through all messages
- **`{{ message }}`** - Outputs the message text
- **`{{ message.tags }}`** - Gets message type (success, error, warning) for styling
- **Bootstrap Classes:**
  - `navbar`, `container`, `alert`, `btn` - Pre-built Bootstrap CSS classes
  - Makes the app look professional without writing custom CSS
- **`{% block content %}{% endblock %}`** - Empty block that child templates will fill with their specific content

**Save the file** (`Ctrl+S`)

---

#### 13c. Create Task List Template (`task_list.html`)

**What This Does:**  
Displays all your tasks in a grid layout with options to view, edit, or delete each task.

**Steps:**
1. Inside `tasks/templates/tasks/` folder, create `task_list.html`
2. Copy and paste the following code:

```html
{% extends 'tasks/base.html' %}

{% block title %}All Tasks - Task Manager{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>All Tasks</h2>
            <a href="{% url 'task_create' %}" class="btn btn-success">
                + New Task
            </a>
        </div>

        {% if tasks %}
            <div class="row">
                {% for task in tasks %}
                <div class="col-md-6 mb-3">
                    <div class="card {% if task.completed %}border-success{% endif %}">
                        <div class="card-body">
                            <div class="d-flex justify-content-between align-items-start">
                                <h5 class="card-title">
                                    {% if task.completed %}
                                        <span class="badge bg-success me-2">✓</span>
                                        <del>{{ task.title }}</del>
                                    {% else %}
                                        <span class="badge bg-warning text-dark me-2">⏳</span>
                                        {{ task.title }}
                                    {% endif %}
                                </h5>
                            </div>
                            
                            {% if task.description %}
                            <p class="card-text text-muted">
                                {{ task.description|truncatewords:20 }}
                            </p>
                            {% endif %}
                            
                            <div class="text-muted small mb-3">
                                <span>Created: {{ task.created_at|date:"M d, Y" }}</span>
                            </div>
                            
                            <div class="btn-group" role="group">
                                <a href="{% url 'task_detail' task.pk %}" class="btn btn-sm btn-info">
                                    View
                                </a>
                                <a href="{% url 'task_update' task.pk %}" class="btn btn-sm btn-primary">
                                    Edit
                                </a>
                                <a href="{% url 'task_delete' task.pk %}" class="btn btn-sm btn-danger">
                                    Delete
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="alert alert-info text-center">
                <h4>No tasks yet!</h4>
                <p>Create your first task to get started.</p>
                <a href="{% url 'task_create' %}" class="btn btn-primary">Create Task</a>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

**Understanding the Code:**

- **`{% extends 'tasks/base.html' %}`** - Inherits structure from `base.html`
- **`{% if tasks %}`** - Checks if any tasks exist in database
- **`{% for task in tasks %}`** - Loops through each task from the view's context
  - Remember: `task_list` view sends `{'tasks': tasks}` to template
- **`{% if task.completed %}`** - Conditional styling based on task status
- **`{{ task.title }}`** - Outputs the task's title
- **`{{ task.description|truncatewords:20 }}`** - Template filter that limits description to 20 words
- **`{{ task.created_at|date:"M d, Y" }}`** - Formats date as "Nov 28, 2025"
- **`{% url 'task_detail' task.pk %}`** - Generates URL like `/task/5/`
  - `task.pk` is the task's primary key (ID)
  - This gets passed as the `pk` parameter to the view
- **`{% else %}`** - Shown when no tasks exist
- **Bootstrap Grid:**
  - `col-md-6` - Each task card takes 50% width on medium+ screens
  - Creates 2-column layout
  - Automatically stacks on mobile devices

**Save the file**

---

#### 13d. Create Task Form Template (`task_form.html`)

**What This Does:**  
Provides a form to create new tasks or update existing tasks. The same template handles both operations.

**Steps:**
1. Inside `tasks/templates/tasks/` folder, create `task_form.html`
2. Copy and paste the following code:

```html
{% extends 'tasks/base.html' %}

{% block title %}{{ action }} Task - Task Manager{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h3 class="mb-0">{{ action }} Task</h3>
            </div>
            <div class="card-body">
                <!-- Form submission -->
                <!-- method="post" sends data to server -->
                <!-- action="" submits to current URL -->
                <form method="post" action="">
                    <!-- CSRF token - required for security in Django POST forms -->
                    {% csrf_token %}
                    
                    <!-- Display form errors if any -->
                    {% if form.errors %}
                        <div class="alert alert-danger">
                            <strong>Please correct the errors below:</strong>
                            {{ form.errors }}
                        </div>
                    {% endif %}
                    
                    <!-- Render form fields -->
                    <div class="mb-3">
                        <label for="{{ form.title.id_for_label }}" class="form-label">
                            {{ form.title.label }}
                        </label>
                        {{ form.title }}
                        {% if form.title.errors %}
                            <div class="text-danger">{{ form.title.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">
                            {{ form.description.label }}
                        </label>
                        {{ form.description }}
                        {% if form.description.errors %}
                            <div class="text-danger">{{ form.description.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3 form-check">
                        {{ form.completed }}
                        <label for="{{ form.completed.id_for_label }}" class="form-check-label">
                            {{ form.completed.label }}
                        </label>
                        {% if form.completed.errors %}
                            <div class="text-danger">{{ form.completed.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <!-- Submit buttons -->
                    <div class="d-flex justify-content-between">
                        <button type="submit" class="btn btn-success">
                            {{ action }} Task
                        </button>
                        <a href="{% url 'task_list' %}" class="btn btn-secondary">
                            Cancel
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

**Understanding the Code:**

- **`{{ action }}`** - Variable passed from view (either "Create" or "Update")
- **`<form method="post" action="">`** - HTML form that submits via POST method
  - `action=""` means submit to same URL
- **`{% csrf_token %}`** - **CRITICAL SECURITY FEATURE**
  - Cross-Site Request Forgery protection
  - Django requires this in all POST forms
  - Without it, form submission will fail with 403 Forbidden error
- **`{{ form.title }}`** - Renders the title input field
  - Django automatically generates HTML: `<input type="text" name="title" class="form-control" />`
  - Styling comes from `widgets` we defined in `forms.py`
- **`{{ form.title.label }}`** - Outputs "Title" label text
- **`{{ form.title.id_for_label }}`** - Gets the HTML id attribute for the input
- **`{% if form.errors %}`** - Shows validation errors
- **How This Template Works for Both Create and Update:**
  - Create: View passes empty form + `action="Create"`
  - Update: View passes form with existing data + `action="Update"`
  - Same template, different context!

**Save the file**

---

#### 13e. Create Task Detail Template (`task_detail.html`)

**What This Does:**  
Shows complete information about a single task, including creation and last updated timestamps.

**Steps:**
1. Inside `tasks/templates/tasks/` folder, create `task_detail.html`
2. Copy and paste the following code:

```html
{% extends 'tasks/base.html' %}

{% block title %}{{ task.title }} - Task Manager{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header bg-info text-white d-flex justify-content-between align-items-center">
                <h3 class="mb-0">Task Details</h3>
                {% if task.completed %}
                    <span class="badge bg-success">Completed ✓</span>
                {% else %}
                    <span class="badge bg-warning text-dark">Pending ⏳</span>
                {% endif %}
            </div>
            <div class="card-body">
                <h4 class="card-title">{{ task.title }}</h4>
                
                {% if task.description %}
                    <div class="mb-3">
                        <h6 class="text-muted">Description:</h6>
                        <p class="card-text">{{ task.description }}</p>
                    </div>
                {% else %}
                    <p class="text-muted fst-italic">No description provided.</p>
                {% endif %}
                
                <hr>
                
                <div class="row">
                    <div class="col-md-6">
                        <p class="mb-1"><strong>Created:</strong></p>
                        <p class="text-muted">{{ task.created_at|date:"F d, Y g:i A" }}</p>
                    </div>
                    <div class="col-md-6">
                        <p class="mb-1"><strong>Last Updated:</strong></p>
                        <p class="text-muted">{{ task.updated_at|date:"F d, Y g:i A" }}</p>
                    </div>
                </div>
                
                <hr>
                
                <div class="d-flex gap-2">
                    <a href="{% url 'task_update' task.pk %}" class="btn btn-primary">
                        Edit Task
                    </a>
                    <a href="{% url 'task_delete' task.pk %}" class="btn btn-danger">
                        Delete Task
                    </a>
                    <a href="{% url 'task_list' %}" class="btn btn-secondary">
                        Back to List
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

**Understanding the Code:**

- **`{{ task.title }}`** - Accesses task object passed from `task_detail` view
  - View sends: `{'task': task}`
  - Template uses: `{{ task.title }}`, `{{ task.description }}`, etc.
- **`{{ task.created_at|date:"F d, Y g:i A" }}`** - Formats as "November 28, 2025 12:30 PM"
  - `F` = Full month name
  - `d` = Day (01-31)
  - `Y` = 4-digit year
  - `g:i A` = Hour:Minutes AM/PM
- **`{% if task.description %}`** - Only shows description section if description exists
  - Database field has `blank=True, null=True` so it's optional
- **`d-flex gap-2`** - Bootstrap flexbox with gap between buttons

**Save the file**

---

#### 13f. Create Delete Confirmation Template (`task_confirm_delete.html`)

**What This Does:**  
Shows a confirmation page before permanently deleting a task. This prevents accidental deletions.

**Steps:**
1. Inside `tasks/templates/tasks/` folder, create `task_confirm_delete.html`
2. Copy and paste the following code:

```html
{% extends 'tasks/base.html' %}

{% block title %}Delete Task - Task Manager{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card border-danger">
            <div class="card-header bg-danger text-white">
                <h3 class="mb-0">⚠️ Confirm Deletion</h3>
            </div>
            <div class="card-body">
                <p class="lead">Are you sure you want to delete this task?</p>
                
                <div class="alert alert-warning">
                    <strong>Task:</strong> {{ task.title }}
                    {% if task.description %}
                        <br><strong>Description:</strong> {{ task.description|truncatewords:15 }}
                    {% endif %}
                </div>
                
                <p class="text-muted">This action cannot be undone.</p>
                
                <!-- Delete confirmation form -->
                <form method="post" action="">
                    {% csrf_token %}
                    <div class="d-flex justify-content-between">
                        <button type="submit" class="btn btn-danger">
                            Yes, Delete Task
                        </button>
                        <a href="{% url 'task_list' %}" class="btn btn-secondary">
                            Cancel
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

**Understanding the Code:**

- **`border-danger`**, **`bg-danger`** - Red Bootstrap classes to indicate danger
- **Form with only CSRF token:**
  - No input fields needed
  - Just confirmation via POST request
  - GET request shows confirmation page
  - POST request actually deletes the task
- **`{{ task.description|truncatewords:15 }}`** - Shows first 15 words of description
- **Cancel button:**
  - Links back to task list
  - Doesn't submit form, so task isn't deleted

**Save the file**

---

#### 13g. Verify Templates Work

**What to Expect:**  
Your app should now be fully functional! Let's test it.

**Steps:**
1. Make sure the development server is running:
   ```powershell
   python manage.py runserver
   ```

2. Open your browser and go to `http://127.0.0.1:8000/`

3. **Expected Result:**  
   You should see a beautiful page with:
   - ✅ Blue navigation bar with "📝 Task Manager" logo
   - ✅ Navigation links (All Tasks, Create Task, Admin Panel)
   - ✅ Message saying "No tasks yet!" with a "Create Task" button
   - ✅ Footer at the bottom

4. **Test Creating a Task:**
   - Click "+ New Task" or "Create Task"
   - You'll see a form with:
     - Title field (text input)
     - Description field (text area)
     - Completed checkbox
     - "Create Task" button
     - "Cancel" button
   - Fill in:
     - Title: "My First Task"
     - Description: "This is a test task to verify everything works!"
     - Leave "Completed" unchecked
   - Click "Create Task"
   - **Expected:** Redirected to task list with green success message "Task created successfully!"
   - **Expected:** Your task appears with:
     - ⏳ Warning badge (because it's not completed)
     - Title: "My First Task"
     - Description (truncated to 20 words)
     - Created date
     - View, Edit, Delete buttons

5. **Test Viewing a Task:**
   - Click "View" button
   - **Expected:** See full task details including:
     - Complete title and description
     - Created timestamp
     - Last updated timestamp
     - Completed status badge
     - Edit, Delete, Back to List buttons

6. **Test Updating a Task:**
   - Click "Edit Task"
   - **Expected:** Form pre-filled with existing data
   - Change something (e.g., check "Completed")
   - Click "Update Task"
   - **Expected:** Redirected to task list with "Task updated!" message
   - **Expected:** Task now shows ✓ green badge and title is crossed out

7. **Test Deleting a Task:**
   - Click "Delete" on any task
   - **Expected:** Confirmation page with:
     - ⚠️ Red warning header
     - Task details shown
     - "This action cannot be undone" message
     - "Yes, Delete Task" and "Cancel" buttons
   - Click "Yes, Delete Task"
   - **Expected:** Redirected to task list with "Task deleted!" message
   - **Expected:** Task no longer appears in list

**Common Issues:**

| Issue | Solution |
|-------|----------|
| Templates not found | Check folder structure is exactly: `tasks/templates/tasks/*.html` |
| CSS/Styling not working | Check internet connection (Bootstrap loads from CDN) |
| Forms don't submit | Make sure you included `{% csrf_token %}` |
| URLs not working | Verify `tasks` app is in `INSTALLED_APPS` in `settings.py` |
| Messages not showing | Check `base.html` has the messages block |

**What You've Built:**
- ✅ Complete CRUD functionality (Create, Read, Update, Delete)
- ✅ Professional UI with Bootstrap
- ✅ Template inheritance (DRY principle)
- ✅ Dynamic URLs
- ✅ Form validation
- ✅ Success/error messages
- ✅ Responsive design (works on mobile!)

**Template Inheritance Summary:**
```
base.html (parent template)
├── Provides: navbar, footer, messages, styling
├── Defines: {% block title %}, {% block content %}
│
├── task_list.html extends base.html
│   └── Overrides: title, content (shows all tasks)
│
├── task_form.html extends base.html
│   └── Overrides: title, content (create/update form)
│
├── task_detail.html extends base.html
│   └── Overrides: title, content (single task view)
│
└── task_confirm_delete.html extends base.html
    └── Overrides: title, content (deletion confirmation)
```


**Django Template Syntax Quick Reference:**

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{% %}` | Logic/Control Flow | `{% if %} {% for %} {% block %}` |
| `{{ }}` | Output Variables | `{{ task.title }}` |
| `{# #}` | Comments | `{# This is a comment #}` |
| `{% extends 'base.html' %}` | Template Inheritance | Inherit from parent template |
| `{% block name %}...{% endblock %}` | Define/Override Block | Create replaceable sections |
| `{% url 'name' %}` | Reverse URL Lookup | Generate URL from URL name |
| `{% url 'name' param %}` | URL with Parameter | Generate `/task/5/` from name |
| `{% if condition %}` | Conditional | Show content if true |
| `{% for item in list %}` | Loop | Iterate over list |
| `{% csrf_token %}` | CSRF Security | Required in all POST forms |
| `{% load static %}` | Load Static Files | Enable `{% static %}` tag |
| `{{ var|filter }}` | Apply Filter | Transform variable output |
| `{{ date|date:"M d, Y" }}` | Date Formatting | Nov 28, 2025 |
| `{{ text|truncatewords:20 }}` | Truncate Text | Limit to 20 words |
| `{{ text|upper }}` | Uppercase | CONVERT TO UPPERCASE |
| `{{ text|lower }}` | Lowercase | convert to lowercase |
| `{{ number|add:5 }}` | Add to Number | Add 5 to number |

---

### Step 14: Register Model in Admin
Edit `tasks/admin.py`:

```python
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at']
    list_filter = ['completed', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['completed']
```

**Admin Customization:**
- `list_display` - Columns shown in list view
- `list_filter` - Add filter sidebar
- `search_fields` - Enable search
- `list_editable` - Edit directly in list view
- `readonly_fields` - Prevent editing certain fields

---

### Step 15: Create Superuser
```powershell
python manage.py createsuperuser
```

Follow prompts:
- Username: `admin`
- Email: `admin@example.com` (can be fake for development)
- Password: Enter secure password (min 8 characters)
- Password confirmation: Re-enter password

**What Is Superuser?**
- Full access to admin panel
- Can create/edit/delete any data
- Manage users and permissions
- Access all registered models

---

## 🎯 CHECKPOINT 3: Full Application Complete!

**🎉 Congratulations! You've built a complete Django CRUD application!**

**What You Can Do RIGHT NOW:**

### 1️⃣ **Test the Public Web Application**

Start the server if not running:
```powershell
python manage.py runserver
```

**Visit:** `http://127.0.0.1:8000/`

**You Should See:**
- ✅ Beautiful blue navigation bar
- ✅ "All Tasks" page
- ✅ Ability to create, view, edit, and delete tasks
- ✅ Success/error messages
- ✅ Responsive design

**Try These Actions:**
1. ✅ Click "New Task" → Create a task
2. ✅ Click "View" → See task details
3. ✅ Click "Edit" → Update a task
4. ✅ Check "Completed" → See ✓ badge and strikethrough
5. ✅ Click "Delete" → Confirm deletion

---

### 2️⃣ **Test the Admin Panel** (NEW!)

**Visit:** `http://127.0.0.1:8000/admin/`

**Login with:**
- Username: The username you just created (e.g., `admin`)
- Password: The password you entered

**After Login, You Should See:**
- Django administration dashboard
- "TASKS" section with "Tasks" link
- Click on "Tasks" to manage tasks

**Admin Features You Can Use:**

| Feature | What It Does | Try It |
|---------|--------------|--------|
| **List View** | See all tasks in a table | Click "Tasks" |
| **Quick Edit** | Check/uncheck "Completed" without opening task | Toggle checkboxes in list |
| **Add Task** | Create new task | Click "ADD TASK +" button |
| **Filter Sidebar** | Filter by completed status or date | Use right sidebar filters |
| **Search** | Search tasks by title/description | Use search box at top |
| **Edit Task** | Click any task title | Modify and save |
| **Delete Task** | Select tasks → Actions dropdown → Delete | Bulk delete multiple tasks |

**Cool Admin Features:**
- ✅ **Auto-save timestamps** - See exact created/updated times
- ✅ **Bulk actions** - Delete multiple tasks at once
- ✅ **Filtering** - Find tasks quickly
- ✅ **Search** - Search across title and description
- ✅ **Direct editing** - Toggle completion status from list view

---

### 3️⃣ **Compare: Public App vs Admin Panel**

You now have **TWO interfaces** to manage tasks:

| Feature | Public App | Admin Panel |
|---------|-----------|-------------|
| **Purpose** | End-user interface | Management/admin interface |
| **URL** | `http://127.0.0.1:8000/` | `http://127.0.0.1:8000/admin/` |
| **Access** | Anyone can visit | Requires admin login |
| **Design** | Custom Bootstrap UI | Django's built-in UI |
| **Best For** | Daily task management | Quick admin tasks, bulk operations |
| **You Built** | Everything from scratch! | Django provides automatically |

---

### 4️⃣ **Verify Everything Works**

**Checklist:**
- [ ] Can create tasks in public app ✅
- [ ] Can view task list ✅
- [ ] Can update tasks ✅
- [ ] Can delete tasks ✅
- [ ] See success messages ✅
- [ ] Can login to admin panel ✅
- [ ] Can manage tasks in admin ✅
- [ ] Search works in admin ✅
- [ ] Filters work in admin ✅
- [ ] Tasks show in both interfaces ✅

**Test Data Sync:**
1. Create a task in the **public app**
2. Go to **admin panel** → Refresh → You should see the same task!
3. Edit the task in **admin panel**
4. Go back to **public app** → Refresh → See the changes!

This proves both interfaces use the **same database**! 🎯

---

**What You've Accomplished:**
- ✅ Complete CRUD application with professional UI
- ✅ Database-driven with SQLite
- ✅ Form validation and error handling
- ✅ URL routing with named patterns
- ✅ Template inheritance (DRY principle)
- ✅ Django admin panel customization
- ✅ User authentication (superuser)
- ✅ Success/error messaging system
- ✅ Responsive Bootstrap design
- ✅ **Production-ready Django skills!**

**You Can Now:**
- 📚 Add more features (categories, due dates, priorities)
- 🎨 Customize the design further
- 🔐 Add user authentication to public app
- 🚀 Deploy to a hosting platform
- 🛠️ Build other Django applications using these skills!

---

### Step 16: Run Development Server
```powershell
python manage.py runserver
```

**Access Your App:**
- Main app: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

**Stop Server:** Press `Ctrl+C` in terminal

---

## Django Concepts Explained

### 1. MTV Pattern (Model-Template-View)
Django uses MTV architecture (similar to MVC):

- **Model** - Database layer (defines data structure)
- **Template** - Presentation layer (HTML with template tags)
- **View** - Business logic layer (processes requests)

**Flow:**
1. User requests URL
2. Django finds matching URL pattern
3. Calls associated view function
4. View queries database via models
5. View renders template with data
6. Django returns HTML response

### 2. Models (Database)
- Define database structure using Python classes
- Each model class = one database table
- Each attribute = one database column
- ORM (Object-Relational Mapping) translates Python to SQL

**Common Model Fields:**
```python
CharField(max_length=200)           # Short text
TextField()                         # Long text
IntegerField()                      # Integer numbers
BooleanField(default=False)        # True/False
DateTimeField(auto_now_add=True)   # Timestamp
ForeignKey(OtherModel)             # Relationship
```

**Querying Database:**
```python
Task.objects.all()                  # Get all tasks
Task.objects.get(pk=1)             # Get one task by ID
Task.objects.filter(completed=True) # Get completed tasks
Task.objects.create(title="New")   # Create new task
```

### 3. Views (Logic)
- Functions that receive requests and return responses
- Process form data, query database, apply business logic
- Return rendered template or redirect

**Function-Based Views:**
```python
def my_view(request):
    # Process request
    data = {'key': 'value'}
    return render(request, 'template.html', data)
```

### 4. Templates (HTML)
- HTML files with Django template language
- Display dynamic content
- Includes template tags and filters

**Template Syntax:**
```django
<!-- Variables -->
{{ variable_name }}

<!-- For loop -->
{% for item in items %}
    {{ item.name }}
{% endfor %}

<!-- If statement -->
{% if condition %}
    <!-- content -->
{% endif %}

<!-- URL linking -->
<a href="{% url 'url_name' %}">Link</a>
<a href="{% url 'url_name' object.pk %}">Link with parameter</a>
```

### 5. Forms
- Handle user input securely
- Validate data automatically
- Render HTML form fields

**Using Forms in Views:**
```python
# Display form (GET)
form = TaskForm()

# Process form (POST)
if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success_page')
```

**Form in Template:**
```django
<form method="post">
    {% csrf_token %}  <!-- Security token -->
    {{ form.as_p }}   <!-- Render form -->
    <button type="submit">Submit</button>
</form>
```

### 6. URLs (Routing)
- Map URLs to view functions
- Extract parameters from URLs
- Name URLs for reverse lookup

**URL with Parameter:**
```python
path('task/<int:pk>/', views.task_detail, name='task_detail')
```
- Matches: `/task/5/`, `/task/123/`
- Passes `pk=5` or `pk=123` to view function

### 7. Django Admin
- Automatic admin interface
- Manage database through web interface
- Customizable for each model

**Benefits:**
- No need to build admin pages manually
- Full CRUD operations
- User-friendly interface
- Permission system built-in

### 8. Migrations
- Version control for database schema
- Track model changes over time
- Apply changes safely

**Migration Workflow:**
1. Change model in `models.py`
2. Run `makemigrations` (creates migration file)
3. Run `migrate` (applies changes to database)
4. Migration file stored in version control

### 9. Static Files (CSS, JS, Images)
For static files, configure in `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Use in templates:
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### 10. Messages Framework
- Display one-time notifications to users
- Success, error, warning, info messages

```python
from django.contrib import messages
messages.success(request, 'Task created!')
messages.error(request, 'Something went wrong!')
```

---

## Testing the Application

### 1. Access Main Application
1. Start server: `python manage.py runserver`
2. Open browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
3. You should see the Task List page

### 2. Test CRUD Operations

**CREATE:**
1. Click "New Task" button
2. Fill in title and description
3. Click "Create Task"
4. Verify redirect to task list with success message

**READ:**
1. View all tasks on homepage
2. Click "View" on any task
3. See complete task details

**UPDATE:**
1. Click "Edit" on any task
2. Modify fields
3. Click "Update Task"
4. Verify changes saved

**DELETE:**
1. Click "Delete" on any task
2. Confirm deletion on confirmation page
3. Verify task removed from list

### 3. Test Admin Panel
1. Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Login with superuser credentials
3. Click "Tasks" under "TASKS" section
4. Create, edit, delete tasks through admin interface
5. Test filters and search functionality

---

## Troubleshooting

### Virtual Environment Not Activating
**Problem:** `Activate.ps1` script error  
**Solution:** Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy RemoteSigned
```

### Django Not Found
**Problem:** `ModuleNotFoundError: No module named 'django'`  
**Solution:** 
- Make sure virtual environment is activated (you see `(myenv)`)
- Reinstall Django: `pip install django`

### Migration Errors
**Problem:** Database conflicts or migration issues  
**Solution:**
```powershell
# Delete db.sqlite3 file
# Delete migrations folder contents except __init__.py
python manage.py makemigrations
python manage.py migrate
```

### Template Not Found
**Problem:** `TemplateDoesNotExist`  
**Solution:**
- Check template path: `tasks/templates/tasks/template_name.html`
- Verify app is in `INSTALLED_APPS`
- Check template name in view matches file name

### Static Files Not Loading
**Problem:** CSS/JS not working  
**Solution:**
- Add `{% load static %}` at top of template
- Use `{% static 'path/to/file' %}`
- Run `python manage.py collectstatic` for production

### Port Already in Use
**Problem:** Port 8000 already in use  
**Solution:**
```powershell
# Use different port
python manage.py runserver 8080

# Or find and stop process using port 8000
```

---

## Next Steps

### Enhance Your Application
1. **Add User Authentication**
   - User registration/login
   - User-specific tasks
   - Permissions

2. **Improve UI**
   - Custom CSS
   - JavaScript interactions
   - Better responsive design

3. **Add Features**
   - Task categories
   - Due dates
   - Priority levels
   - Task assignments
   - File attachments

4. **Testing**
   - Write unit tests
   - Integration tests
   - Test coverage

5. **Deployment**
   - Deploy to Heroku/PythonAnywhere
   - Configure production settings
   - Use PostgreSQL instead of SQLite

### Learning Resources
- Official Django Documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- Django Tutorial: [https://docs.djangoproject.com/en/stable/intro/tutorial01/](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- Django Girls Tutorial: [https://tutorial.djangogirls.org/](https://tutorial.djangogirls.org/)

---

## Summary

You've successfully built a complete Django CRUD application! You learned:

✅ Setting up Python virtual environment  
✅ Installing and configuring Django  
✅ Creating Django projects and apps  
✅ Defining database models  
✅ Creating and applying migrations  
✅ Building forms for user input  
✅ Creating views for business logic  
✅ Configuring URL routing  
✅ Building templates with Django template language  
✅ Customizing Django admin panel  
✅ Implementing full CRUD operations  
✅ Using Django's messages framework  
✅ Understanding MTV architecture  

**Congratulations!** You now have a solid foundation in Django development. Keep building and exploring! 🚀
