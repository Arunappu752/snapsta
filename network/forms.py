from django import forms
from django.contrib.auth.forms import UserChangeForm
from . models import User

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True)
    new_profile_pic = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    new_cover = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'profile_pic',
            'cover',
        )