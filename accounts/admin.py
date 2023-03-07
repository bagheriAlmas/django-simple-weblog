from django.contrib import admin

from accounts.models import CustomUser

admin.site.register(CustomUser)
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm  # dokmeye add kardan yek user
#     form = CustomUserChangeForm  # formi ke haminjuri aval be ma neshun mide
#     model = CustomUser
#     list_display = ['username', 'age', 'is_staff', 'email']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('age', 'phone', 'avatar'), }),)  # baraye ChangeForm
#
#     add_fieldsets = (
#                         (
#                             None, {'fields': ('first_name', 'last_name',), }
#                         ),
#                     ) + UserAdmin.add_fieldsets + (
#                         (
#                             None, {'fields': ( 'age', 'phone', 'avatar',), }
#                         ),
#                     )
#
#     # baraye CreationForm
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
