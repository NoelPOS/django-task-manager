from django.db import models

# Create your models here.

class Task(models.Model):
    """
    Task model for our CRUD application.
    Represents a task with title, description, completion status, and timestamps.
    """
    # CharField for short text (max 200 characters)
    title = models.CharField(max_length=200)
    
    # TextField for longer text (no character limit)
    description = models.TextField(blank=True, null=True)
    
    # BooleanField for true/false values
    completed = models.BooleanField(default=False)
    
    # DateTimeField to automatically record creation time
    created_at = models.DateTimeField(auto_now_add=True)
    
    # DateTimeField to automatically update on every save
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Orders tasks by creation date (newest first)
        ordering = ['-created_at']
    
    def __str__(self):
        # String representation shown in admin and other places
        return self.title
