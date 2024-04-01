from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            if user:
                raise forms.ValidationError("Email already exists.")
        except User.DoesNotExist:
            return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if 'email' not in self._errors:
            try:
                user = User.objects.get(email=email)
                if user:
                    msg = "Email already exists."
                    self.add_error('email', msg)
            except User.DoesNotExist:
                pass

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput())