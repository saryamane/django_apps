from django.shortcuts import render
from django.http import HttpResponse
from usersignupapp.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'usersignupapp/index.html')

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {"users":user_list}
    # return render(request, 'usersignupapp/user_signup.html', context=user_dict)
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form is invalid')
    return render(request, 'usersignupapp/user_signup.html', {'form':form})
