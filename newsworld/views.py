from django.shortcuts import render
from django.views.generic import FormView

from news.form import RegisterForm
from newsworld.models import News


# Create your views here.
def home_page(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, template_name='index.html', context=context)


class MyFormView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'