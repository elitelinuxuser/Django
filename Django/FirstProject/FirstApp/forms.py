from django import forms
from FirstApp.models import User

class NewForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
