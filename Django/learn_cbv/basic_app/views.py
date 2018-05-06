from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from django.utils.decorators import method_decorator
from . import models
from django.urls import reverse_lazy
from basic_app.forms import UserForm,UserProfileForm
#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    @method_decorator(login_required(login_url='/basic_app/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    @method_decorator(login_required(login_url='/basic_app/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    @method_decorator(login_required(login_url='/basic_app/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        success_url = reverse_lazy('basic_app:list')


#Copied

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

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'basic_app/register.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'basic_app/special.html')

                else:
                    HttpResponse("Account inactive")
            else:
                print("Some tried to login and failed")
                print("Username: {} and Password {}".format(username,password))
                return HttpResponse("invalid login:")

        else:
            return render(request,'basic_app/login.html',{'txt':'Please Login!'})
    else:
        return render(request,'basic_app/login.html',{'txt':''})

#Logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        txt = 'You are logged out'
        return render(request,'basic_app/login.html',context  = {'txt':txt})
    else:
        txt = 'Please login!'

def special(request):
    if not request.user.is_authenticated:
        return render(request,'basic_app/login.html')
    else:
        return render(request,'basic_app/special.html')
