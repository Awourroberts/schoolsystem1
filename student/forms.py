
from.models import Student
from django import forms

class StudentRegistrationForms(forms.ModelForm):
    class Meta:
        model= Student
        fields="__all__"
        widgets={
            'gender':forms.Select(),
            'nationality':forms.Select()

        }