from django.urls import path
from . import views

"""
URL patterns for the tasks app.
Each path() connects a URL to a view function.
"""

urlpatterns = [
    # List all tasks - Homepage
    # path('url-pattern', view_function, name='url-name')
    path('', views.task_list, name='task_list'),
    
    # Create new task
    path('create/', views.task_create, name='task_create'),
    
    # View single task details
    # <int:pk> captures an integer from URL and passes it as 'pk' parameter
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    
    # Update existing task
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    
    # Delete task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
