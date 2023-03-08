# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = CustomUser
#         # fields = UserCreationForm.Meta.fields + ('age','phone','nationality',)
#         fields = ['username', 'email', 'phone', 'nationality', 'age','avatar']
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'about_me', 'avatar')
        exclude = ('password',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'about_me', 'avatar')
        exclude = ('password',)


