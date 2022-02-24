from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
