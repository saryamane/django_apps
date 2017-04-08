from django import forms
from usersignupapp.models import Users

class NewUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
