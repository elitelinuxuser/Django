from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

loggedin=False
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


#Registration
def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'basic_app/register.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                global loggedin
                loggedin=True
                return render(request,'basic_app/special.html',{'logged_in':loggedin})

            else:
                HttpResponse("Account inactive")
        else:
            print("Some tried to login and failed")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("invalid login:")

    else:
        return render(request,'basic_app/login.html',{})

#Logout
@login_required
def user_logout(request):
    logout(request)
    global loggedin
    loggedin=False
    return render(request,'basic_app/special.html',{'logged_in':loggedin})

def special(request):
    if loggedin==False:
        return render(request,'basic_app/login.html')
    elif loggedin==True:
        return render(request,'basic_app/special.html')
