from django.shortcuts import render
# from FirstApp.models import User
from FirstApp.forms import NewForm

# Create your views here.
def index(request):
    return render(request,'FirstApp/index.html')

def users(request):

    form = NewForm()

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Invalid")

    return render(request,'FirstApp/users.html',{'form':form})
