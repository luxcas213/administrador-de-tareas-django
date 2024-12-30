from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    importance = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '10'})
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'importance']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
