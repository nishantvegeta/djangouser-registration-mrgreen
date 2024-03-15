from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

#authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout



def homepage(request):
    return render(request, 'crm/index.html')



def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("my_login")
    context = {'registerform': form}
    return render(request, 'crm/register.html', context=context)



def my_login(request):
    form =  LoginForm() 

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if  form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
    
    context = {'loginform': form }

    return render(request, 'crm/my_login.html',context)


def userlogout(request):
    auth.logout(request)
    return redirect("")



def dashboard(request):

    return render(request, 'crm/dashboard.html')