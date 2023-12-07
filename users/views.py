from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} Has Created")
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.POST:
        u_forms = UserUpdateForm(request.POST,instance=request.user)
        p_forms = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if p_forms.is_valid() and u_forms.is_valid():
            p_forms.save()
            u_forms.save()
            messages.success(request, 'your profile has been updated')
            redirect('profile')
    else:
        u_forms = UserUpdateForm(instance=request.user)
        p_forms = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_forms': u_forms,
        'p_forms': p_forms
    }
    return render(request, 'users/profile.html', context)
