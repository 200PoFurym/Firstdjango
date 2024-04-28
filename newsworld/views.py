from django.shortcuts import render

from newsworld.models import News


# Create your views here.
def home_page(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, template_name='index.html', context=context)

