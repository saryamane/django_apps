from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Topic, AccessRecord, WebPage

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request, 'myapp/index.html', context=date_dict)

def user_signup(request):
    return HttpResponse('<em>This is the signup page</em>')

def help_page(request):
    help_dict = {'help_content':'This is going to be injected in the help text'}
    return render(request, 'myapp/help_page.html', context=help_dict)
