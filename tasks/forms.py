from django import forms
from .models import task

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'category', 'dueDate']  # Add fields as necessary

    # Add form-control class to each field
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
    dueDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
