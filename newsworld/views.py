from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView

from news.form import RegisterForm, LoginForm
from newsworld.models import News, NewsCategory


# Create your views here.
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        if get_news:
            exact_news = News.objects.filter(news_name__icontains=get_news)
            context = {'news': news, 'categories': categories, 'search_news': exact_news }
            return render(request, 'index.html', context=context)
    else:
        context = {'news': news, 'categories': categories}
        return render(request, template_name='index.html', context=context)

def single_news(request, id):
    news = News.objects.get(id=id)
    context = {'news': news}
    return render(request, 'single_news.html', context=context)


class MyFormView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'


class MyLoginFormView(CreateView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return redirect('/')

