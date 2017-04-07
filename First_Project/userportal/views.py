from django.shortcuts import render
from userportal.models import User

# Create your views here.

def index(request):
    return render(request, 'userportal/index.html')

def user_signup(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'userportal/user_signup.html', context=user_dict)
