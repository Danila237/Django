from django.shortcuts import render
# Create your views here.

def index(request):
    data = {
        'name': 'Ruby',
    }
    return render(request, 'app_one/index.html', data)

def about(request):
    dataB = {
        'values': ['Web', 'Application'],
    }
    return render(request, 'app_one/about.html', dataB)

def contact(request):
    return render(request, 'app_one/contact.html')
