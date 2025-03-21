from django import forms
from django.contrib.auth.models import User
from .models import Vote

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class VoteForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        category = kwargs.pop('category')
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(category=category)

    class Meta:
        model = Vote
        fields = ('company',)