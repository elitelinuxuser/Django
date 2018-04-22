from django.shortcuts import render
from FirstApp.models import User

# Create your views here.
def index(request):
    return render(request,'FirstApp/index.html')

def users(request):
    my_list = User.objects.order_by('first_name')
    my_dict = {'users':my_list}
    return render(request,'FirstApp/users.html',context = my_dict)
