from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'hidden', 
            }
        ))
    date_of_birth = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'date', 
            }
        ))
    nationality = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text', 
            'placeholder': 'Asset-Name',
            'class': ""
            }
        ))
    class Meta:
        model = Student
        fields = '__all__'   