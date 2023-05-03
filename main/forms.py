from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'auto-focus': True, 'class': 'form-control',
               'placeholder': 'Current Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class ResumeForm(forms.ModelForm):
    class Meta:
        model =Resume
        fields ='__all__'
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter your first name'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter your last'}),
                    'address': forms.Textarea(attrs={'class': 'form-control col-12 mb-4 form-control multisteps-form__input', 'placeholder': 'Enter your address','rows':3}),
                    'age': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter your age'}),
                    'dob': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter your DOB' ,'type':'date'}),
                    'sscSchoolName': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter ssc school name'}),
                    'sscPercentage': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter ssc school marks'}),
                    'hscSchoolName': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter hsc schoolname'}),
                    'hscPercentage': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter hsc school marks'}),
                    'graduationCollegeName': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter graduation college name'}),
                    'graduationPercentage': forms.TextInput(attrs={'class': 'form-control multisteps-form__input', 'placeholder': 'Enter graduation marks'}),
                    'experience': forms.Textarea(attrs={'class': 'form-control col-12 mb-4 form-control multisteps-form__input', 'placeholder': 'Enter your experience','rows':3}),
                    'career_objective': forms.Textarea(attrs={'class': 'form-control col-12 mb-4 form-control multisteps-form__input', 'placeholder': 'Enter your cerrer objective','rows':3}),
                    'skills': forms.Textarea(attrs={'class': 'form-control col-12 mb-4 form-control multisteps-form__input', 'placeholder': 'Enter your skills'}),
                    'contacts': forms.Textarea(attrs={'class': 'form-control col-12 mb-4 form-control multisteps-form__input', 'placeholder': 'Enter your contacts'}),
                    
                    }
