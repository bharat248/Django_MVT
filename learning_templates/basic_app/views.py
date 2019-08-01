from django.shortcuts import render
from basic_app.models import user

# Create your views here.
def relative_url_templates(request):
    return render(request,'basic_app/relative_url_templates.html')

def other(request):
    return render(request,'basic_app/other.html')

def user_data(request):
    User = user.objects.order_by('first_name')
    return render(request,'basic_app/data.html',context = {'user':User})
