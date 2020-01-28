from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, F'Account Created! Please login now.')
            return redirect('login')
    else:
        form = UserForm()
    
    return render(request, 'user/register.html', {'form':form})
