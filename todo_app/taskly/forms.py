from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    class Meta:
        model = Todo
        fields = ['title', 'details', 'due_date', 'is_completed'] 
        labels = {
            'title': 'Task Title',
            'details': 'Task Details',
            'due_date': 'Due Date and Time',
            'is_completed': 'Completed',
        }
        help_texts = {
            'due_date': 'Select the date and time by which the task should be completed.',
        }