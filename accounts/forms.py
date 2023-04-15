from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        with open("accounts/wordlist.txt", 'r') as f:
            blacklist = f.read().splitlines()

        for bad_word in blacklist:
            if bad_word in username:
                raise forms.ValidationError("Please, change - Username - and this time use a PROPER language")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        with open("accounts/wordlist.txt", 'r') as f:
            blacklist = f.read().splitlines()

        for bad_word in blacklist:
            if bad_word in first_name:
                raise forms.ValidationError("Please, change - First name - and this time use a PROPER language")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')

        with open("accounts/wordlist.txt", 'r') as f:
            blacklist = f.read().splitlines()

        for bad_word in blacklist:
            if bad_word in last_name:
                raise forms.ValidationError("Please, change - Last name - -and this time use a PROPER language")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        with open("accounts/wordlist.txt", 'r') as f:
            blacklist = f.read().splitlines()

        for bad_word in blacklist:
            if bad_word in email:
                raise forms.ValidationError("Please, change - Email - and this time use a PROPER language")
        return email


    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #
    #     with open("accounts/wordlist.txt", 'r') as f:
    #         blacklist = f.read().splitlines()
    #
    #     for bad_word in blacklist:
    #         if bad_word in username:
    #             raise forms.ValidationError("Please, use a proper language")
    #     return username

        #
        # for bad_word in blacklist:
        #     if bad_word in username or first_name or last_name or email:
        #         raise forms.ValidationError("Please, try again and this time use a PROPER language")
        # return username or first_name or last_name or email

class LoginForm(AuthenticationForm):
    fields = ('username', 'password1', 'password2')
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=16)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):

    bio = forms.CharField()

    class Meta:
        model = Profile
        fields = ['bio']
