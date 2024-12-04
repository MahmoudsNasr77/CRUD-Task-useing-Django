from django import forms
from .models import task
class TaskForm(forms.ModelForm):
    class Meta:
        model=task
        fields=['title','descrption','category','dueDate']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }