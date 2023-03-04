from django import forms
from django.contrib.auth.models import User
from . models import Profile

class username_updater(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class DP_uploader(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp']

