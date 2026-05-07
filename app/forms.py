from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'status',
            'due_date',
            'assigned_to',
            'project'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),

            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'due_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'assigned_to': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'project': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }