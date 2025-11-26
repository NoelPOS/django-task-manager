# Django CRUD Task Manager - Complete Tutorial

A comprehensive step-by-step guide to building a full-stack CRUD (Create, Read, Update, Delete) application using Django framework. This tutorial covers all Django basics from scratch, perfect for beginners.

## Quick Start (For Cloning This Repo)

```powershell
# 1. Clone the repository
git clone https://github.com/NoelPOS/django-task-manager.git
cd django-task-manager

# 2. Create virtual environment
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

### Step 12: Configure URLs
Create `tasks/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

Edit `myproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include tasks URLs
]
```

**URL Patterns Explained:**
- `path('url/', view_function, name='url_name')`
- `<int:pk>` - Captures integer from URL, passes to view as `pk`
- `name=` - Used for reverse URL lookup in templates
- `include()` - Includes URLs from another file

**Why Two URL Files?**
- `myproject/urls.py` - Main routing (project-level)
- `tasks/urls.py` - App-specific routes (reusable)
- Keeps code organized and modular

---

### Step 13: Create Templates
Create folder structure: `tasks/templates/tasks/`

**Why nested tasks/tasks/?**
- Django looks in all `templates/` folders
- Nested prevents name conflicts
- Use as `tasks/base.html` in code

#### 13a. Base Template (`base.html`)
Contains common elements (navbar, footer) inherited by other templates.

#### 13b. Task List (`task_list.html`)
Shows all tasks with Create/Edit/Delete buttons.

#### 13c. Task Form (`task_form.html`)
Used for both creating and updating tasks.

#### 13d. Task Detail (`task_detail.html`)
Shows complete task information.

#### 13e. Delete Confirmation (`task_confirm_delete.html`)
Confirms before deleting.

**Template Inheritance:**
```django
{% extends 'tasks/base.html' %}  <!-- Inherit from base -->
{% block content %}              <!-- Override content block -->
    <!-- Your content here -->
{% endblock %}
```

**Template Tags:**
- `{% %}` - Logic (if, for, block, extends)
- `{{ }}` - Variables (output data)
- `{# #}` - Comments (not rendered)

**Common Template Filters:**
- `{{ task.created_at|date:"M d, Y" }}` - Format date
- `{{ task.description|truncatewords:20 }}` - Limit words
- `{{ task.title|upper }}` - Uppercase text

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
