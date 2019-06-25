from django import forms

from user.models import LoginUser


class LoginUserForm(forms.ModelForm):
    login_auth_str = forms.CharField(max_length=100,
                                     widget=forms.PasswordInput,
                                     label='口令')

    class Meta:
        model = LoginUser
        fields = '__all__'