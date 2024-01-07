from django import forms
from .models import user

class StudentReg(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']