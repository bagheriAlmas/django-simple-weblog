from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


@login_required
def user_update_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'pages/edit_profile.html', {'form': form})


# def user_register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm
#     return render(request, 'registration/register.html', {'form': form})


def user_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})