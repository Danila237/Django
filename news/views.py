from django.shortcuts import render, redirect
from .models import Articl
from .forms import ArticlForm
from django.views.generic import DetailView
# Create your views here.

def news_home(request):
    news = Articl.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def NewsDetailView(DetailView):
    model = Articl
    template_name = 'news/details_view.html'
    context_object_name = 'articl'
    return render(DetailView, model, template_name, context_object_name)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная запись формы'

    form = ArticlForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)
