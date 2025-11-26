from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Task model.
    Customizes how tasks appear in the Django admin panel.
    """
    # Fields to display in the list view
    list_display = ['title', 'completed', 'created_at', 'updated_at']
    
    # Fields that can be used to filter the list
    list_filter = ['completed', 'created_at']
    
    # Fields that are searchable
    search_fields = ['title', 'description']
    
    # Fields that are read-only (can't be edited)
    readonly_fields = ['created_at', 'updated_at']
    
    # Enable editing the completed field directly from list view
    list_editable = ['completed']
