from django import forms
from django.contrib.auth.models import User
from . import models


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = models.Reception
        fields = ('reception_date_time',)


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ('feedback_text', )


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают')
        return cd['password1']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('phone',)
