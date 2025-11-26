from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    ModelForm for Task model.
    Automatically creates form fields based on the Task model.
    """
    class Meta:
        # Specify which model this form is for
        model = Task
        
        # Specify which fields to include in the form
        # '__all__' includes all fields, or you can list specific fields
        fields = ['title', 'description', 'completed']
        
        # Customize form widgets (HTML input elements)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description (optional)',
                'rows': 4
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        
        # Custom labels for fields
        labels = {
            'title': 'Task Title',
            'description': 'Description',
            'completed': 'Mark as completed'
        }
